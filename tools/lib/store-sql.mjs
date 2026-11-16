// The store's SQL as text, and the arithmetic of what it costs: every statement the Worker
// (worker/index.mjs) sends to D1 when a capture arrives or a sweep runs. It lives apart from the
// Worker so tests/store-sql.test.mjs can run the same text in SQLite.
//
// Why cost is counted at all. The account is on Cloudflare's free D1 plan. It counts rows written
// across every database on the account, one per table row and one more per index the row enters, and
// past 100,000 in a UTC day it refuses every write until 00:00 UTC. The agents' board is the other
// database on the account, so a store that overspends silences the agents. The store therefore writes
// only what changed, knows the cost of a capture before writing it, keeps the day's spend in one row
// (`spend`), and stops at its share. The numbers are contract/budget.json's `store`.

export const ROWS_PER_STATEMENT = 400;
export const MAX_BOUND = 90;   // D1 refuses a statement with more than 100 bound values

export const COLS = {
  runs: ['id', 'source', 'started_at', 'finished_at', 'status', 'reason', 'agent', 'model', 'method', 'requests_rev', 'reads', 'reads_left', 'plan', 'received_at', 'posts', 'observations'],
  posts: ['id', 'source', 'url', 'created_at', 'lang', 'text', 'author_handle', 'author_name', 'author_followers', 'author_verified', 'author_kind', 'media', 'reply_to', 'quotes', 'media_source', 'note', 'flags', 'desk', 'beat', 'topic', 'lead', 'first_run', 'last_run'],
  post_runs: ['post_id', 'run_id'],
  observations: ['post_id', 'at', 'run_id', 'state', 'views', 'likes', 'reposts', 'quotes', 'replies', 'bookmarks', 'approx'],
  sweeps: ['run_id', 'sweep_id', 'kind', 'desk', 'method', 'window_hours', 'status', 'reason', 'post_ids'],
  volume_points: ['key', 'desk', 'query', 'start', 'count', 'run_id'],
  trends: ['run_id', 'region', 'rank', 'name', 'post_count', 'story', 'post_ids'],
  context: ['run_id', 'post_id', 'replies', 'quotes'],
  answers: ['run_id', 'request_id', 'status', 'post_ids', 'note'],
  checks: ['post_id', 'result', 'detail', 'checked_at', 'handle', 'run'],
};

// A record delivered again (the text was edited, a note appeared) replaces the old one, except a purged one.
const POST_UPSERT = `ON CONFLICT(id) DO UPDATE SET ${COLS.posts.filter((c) => !['id', 'source', 'first_run'].includes(c)).map((c) => `${c} = excluded.${c}`).join(', ')} WHERE posts.purged_at IS NULL AND excluded.last_run > posts.last_run`;
// Every run delivers a week of hourly counts for its desks, and all but the newest hours are the
// counts already held. Only an hour that is new, or that X counts differently now, is written.
const VOLUME_UPSERT = 'ON CONFLICT(key, start) DO UPDATE SET count = excluded.count, run_id = excluded.run_id WHERE excluded.count IS NOT volume_points.count';
const CHECK_UPSERT = 'ON CONFLICT(post_id) DO UPDATE SET result = excluded.result, detail = excluded.detail, checked_at = excluded.checked_at';

// One INSERT per table from a JSON array. "WHERE true" is SQLite's documented way to keep an
// INSERT ... SELECT from reading the upsert clause's ON as a join.
export function insertSql(table, mode = 'INSERT OR IGNORE', onConflict = '') {
  const cols = COLS[table];
  const picks = cols.map((c) => `json_extract(value, '$.${c}')`).join(', ');
  return `${mode} INTO ${table} (${cols.join(', ')}) SELECT ${picks} FROM json_each(?1) WHERE true ${onConflict}`.trim();
}

function sliced(table, rows, mode, onConflict) {
  const sql = insertSql(table, mode, onConflict);
  const out = [];
  for (let i = 0; i < rows.length; i += ROWS_PER_STATEMENT) out.push({ table, sql, params: [JSON.stringify(rows.slice(i, i + ROWS_PER_STATEMENT))] });
  return out;
}

// A capture's rows (tools/lib/store-rows.mjs) as statements, in slices, so a capture of any size is a
// short batch. The Worker adds the gzipped file itself and sends them as one transaction.
export function ingestStatements(rows) {
  return [
    ...sliced('runs', [rows.run], 'INSERT'),
    ...sliced('posts', rows.posts, 'INSERT', POST_UPSERT),
    ...sliced('post_runs', rows.post_runs),
    ...sliced('observations', rows.observations),
    ...sliced('sweeps', rows.sweeps ?? [], 'INSERT OR REPLACE'),
    ...sliced('volume_points', rows.volume_points ?? [], 'INSERT', VOLUME_UPSERT),
    ...sliced('trends', rows.trends ?? [], 'INSERT OR REPLACE'),
    ...sliced('context', rows.context ?? [], 'INSERT OR REPLACE'),
    ...sliced('answers', rows.answers ?? [], 'INSERT OR REPLACE'),
  ];
}

export const checksStatement = (answers) => ({ table: 'checks', sql: insertSql('checks', 'INSERT', CHECK_UPSERT), params: [JSON.stringify(answers)] });

// Rows D1 counts for one new row of each table: the table and each index every row enters
// (worker/schema.sql; a test holds the two together). A partial index takes only the rows it names.
export const BTREES = { runs: 3, captures: 2, posts: 4, post_runs: 2, observations: 3, sweeps: 2, volume_points: 3, trends: 2, context: 2, answers: 2 };

// The most a capture can cost to deliver. The true cost is lower when counts or records are unchanged.
export function writeCost(rows) {
  let n = BTREES.runs + BTREES.captures;
  for (const t of ['posts', 'post_runs', 'observations', 'sweeps', 'volume_points', 'trends', 'context', 'answers']) n += (rows[t]?.length ?? 0) * BTREES[t];
  return n;
}

// Would this delivery take the store past its share of the day?
export const heldBy = ({ spent, cost, allowance }) => spent + cost > allowance;
export const dayOf = (iso) => iso.slice(0, 10);
export const resetsAt = (iso) => { const d = new Date(iso); return new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate() + 1)).toISOString().replace('.000Z', 'Z'); };
export const secondsUntil = (then, now) => Math.max(0, Math.ceil((Date.parse(then) - Date.parse(now)) / 1000));
export const chunks = (list, n = MAX_BOUND) => Array.from({ length: Math.ceil(list.length / n) }, (_, i) => list.slice(i * n, i * n + n));

export const SPEND_OF = 'SELECT written FROM spend WHERE day = ?1';
export const SPEND_ADD = 'INSERT INTO spend (day, written) VALUES (?1, ?2) ON CONFLICT(day) DO UPDATE SET written = written + excluded.written';

// The deletion sweep, in three short reads. None of them walks the posts table: the first sweep did,
// once an hour, and read 119,000 rows each time by November 2026.
//   owed   posts X said are gone whose purge was not finished: purged now, no question asked
//   gone   posts a reading found unavailable, not yet purged, not asked about in the last day (?1)
//   round  every other post in the order it arrived, from where the last sweep stopped (?1), so each
//          is asked about again once per lap
export const PICK_OWED = "SELECT post_id AS id FROM checks INDEXED BY checks_owed WHERE result = 'missing' AND purged_at IS NULL LIMIT ?1";
export const PICK_GONE = `SELECT DISTINCT o.post_id AS id
  FROM observations o INDEXED BY observations_gone
  CROSS JOIN posts p ON p.id = o.post_id
  LEFT JOIN checks c ON c.post_id = o.post_id
  WHERE o.state = 'unavailable' AND p.purged_at IS NULL AND (c.checked_at IS NULL OR c.checked_at < ?1)
  LIMIT ?2`;
export const PICK_ROUND = 'SELECT rowid AS n, id FROM posts NOT INDEXED WHERE rowid > ?1 AND purged_at IS NULL ORDER BY rowid LIMIT ?2';
export const ROUND_GET = 'SELECT last_rowid FROM sweep_round WHERE id = 1';
export const ROUND_SET = 'INSERT INTO sweep_round (id, last_rowid, laps, updated_at) VALUES (1, ?1, ?2, ?3) ON CONFLICT(id) DO UPDATE SET last_rowid = excluded.last_rowid, laps = laps + excluded.laps, updated_at = excluded.updated_at';

// Which posts one sweep asks X about: the gone first, then the round, no post twice, `limit` in all.
// `asked` is how many round rows were requested; fewer came back when the round reached the newest post.
// mark: where the round resumes (null leaves it where it was; 0 starts a new lap).
export function sweepAsks({ gone, round, limit, asked = limit }) {
  const ids = [];
  const seen = new Set();
  const take = (id) => { if (!seen.has(id)) { seen.add(id); ids.push(id); } };
  for (const g of gone) { if (ids.length >= limit) break; take(g.id); }
  let mark = null;
  let reached = 0;
  for (const r of round) {
    if (ids.length >= limit) break;
    take(r.id);
    mark = r.n;
    reached++;
  }
  const wrapped = reached === round.length && round.length < asked;
  return { ids, mark: wrapped ? 0 : mark, wrapped };
}
