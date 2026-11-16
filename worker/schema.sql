-- The store: the record, where a deletion can be honoured. Applied with
--   npx --yes wrangler@latest d1 execute mts-store --remote --file worker/schema.sql
-- Every statement is idempotent, so the file can be applied again after a change.

CREATE TABLE IF NOT EXISTS runs (
  id TEXT PRIMARY KEY, source TEXT NOT NULL DEFAULT 'x',
  started_at TEXT NOT NULL, finished_at TEXT, status TEXT, reason TEXT,
  agent TEXT, model TEXT, method TEXT, requests_rev TEXT,
  reads INTEGER, reads_left INTEGER, plan TEXT,
  received_at TEXT NOT NULL, posts INTEGER, observations INTEGER
);
CREATE INDEX IF NOT EXISTS runs_started ON runs(started_at);

-- The capture as delivered, gzipped. A purge rewrites it; it is otherwise never changed.
CREATE TABLE IF NOT EXISTS captures (
  run_id TEXT PRIMARY KEY, gz BLOB NOT NULL, bytes INTEGER NOT NULL, updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
  id TEXT PRIMARY KEY, source TEXT NOT NULL DEFAULT 'x',
  url TEXT, created_at TEXT, lang TEXT, text TEXT,
  author_handle TEXT, author_name TEXT, author_followers INTEGER, author_verified TEXT, author_kind TEXT,
  media TEXT, reply_to TEXT, quotes TEXT, media_source TEXT, note TEXT, flags TEXT,
  desk TEXT, beat TEXT, topic TEXT, lead TEXT,
  first_run TEXT, last_run TEXT, purged_at TEXT
);
CREATE INDEX IF NOT EXISTS posts_desk ON posts(desk);
CREATE INDEX IF NOT EXISTS posts_purged ON posts(purged_at);

-- Every run a record appeared in, so a purge can find every file that holds it.
CREATE TABLE IF NOT EXISTS post_runs (post_id TEXT, run_id TEXT, PRIMARY KEY (post_id, run_id));

CREATE TABLE IF NOT EXISTS observations (
  post_id TEXT, at TEXT, run_id TEXT, state TEXT,
  views INTEGER, likes INTEGER, reposts INTEGER, quotes INTEGER, replies INTEGER, bookmarks INTEGER, approx INTEGER,
  PRIMARY KEY (post_id, at)
);
-- No index by time. Until 2026-11-16 there was one (observations_at), and it was a third of what every
-- observation cost to write: 21,000 of the 100,000 rows a day the free plan allows the whole account, for a
-- reading by time that nothing used. A reader that wants a window asks for its runs (runs_started) and reads
-- each run's capture. On the free plan the index cannot be rebuilt once dropped (450,000 rows); on a paid plan
-- it is one statement.
DROP INDEX IF EXISTS observations_at;
-- The readings that found a post unavailable (a handful a run): where the deletion sweep starts, without
-- reading the table.
CREATE INDEX IF NOT EXISTS observations_gone ON observations(post_id) WHERE state = 'unavailable';

CREATE TABLE IF NOT EXISTS sweeps (
  run_id TEXT, sweep_id TEXT, kind TEXT, desk TEXT, method TEXT, window_hours INTEGER, status TEXT, reason TEXT, post_ids TEXT,
  PRIMARY KEY (run_id, sweep_id)
);

-- X's hourly post counts per standing query. A later run's count for the same hour replaces an earlier one.
CREATE TABLE IF NOT EXISTS volume_points (
  key TEXT, desk TEXT, query TEXT, start TEXT, count INTEGER, run_id TEXT,
  PRIMARY KEY (key, start)
);
CREATE INDEX IF NOT EXISTS volume_desk_start ON volume_points(desk, start);

CREATE TABLE IF NOT EXISTS trends (run_id TEXT, region TEXT, rank INTEGER, name TEXT, post_count INTEGER, story TEXT, post_ids TEXT, PRIMARY KEY (run_id, region, rank));
CREATE TABLE IF NOT EXISTS context (run_id TEXT, post_id TEXT, replies TEXT, quotes TEXT, PRIMARY KEY (run_id, post_id));
CREATE TABLE IF NOT EXISTS answers (run_id TEXT, request_id TEXT, status TEXT, post_ids TEXT, note TEXT, PRIMARY KEY (run_id, request_id));

-- Gate 2 in the store: what X said about each post, when, and when its words were purged.
CREATE TABLE IF NOT EXISTS checks (
  post_id TEXT PRIMARY KEY, result TEXT, detail TEXT, checked_at TEXT, handle TEXT, run TEXT, purged_at TEXT
);
CREATE INDEX IF NOT EXISTS checks_checked_at ON checks(checked_at);
-- Posts X said are gone whose purge is not yet recorded: a purge cut short is finished by the next sweep.
CREATE INDEX IF NOT EXISTS checks_owed ON checks(post_id) WHERE result = 'missing' AND purged_at IS NULL;

-- One row per deletion sweep: what it asked X and what it did.
CREATE TABLE IF NOT EXISTS sweep_log (
  at TEXT PRIMARY KEY, checked INTEGER, ok INTEGER, missing INTEGER, mismatch INTEGER, withheld INTEGER, errors INTEGER, purged INTEGER, note TEXT
);

-- Where the sweep's round of every post stands: the rowid of the last post it asked X about, and the laps done.
CREATE TABLE IF NOT EXISTS sweep_round (
  id INTEGER PRIMARY KEY CHECK (id = 1), last_rowid INTEGER NOT NULL DEFAULT 0, laps INTEGER NOT NULL DEFAULT 0, updated_at TEXT
);

-- Rows the store has written, by UTC day. Cloudflare's free plan counts rows written across every database on
-- the account (the agents' board is the other one) and refuses all writes past 100,000 a day until 00:00 UTC,
-- so the store counts its own and stops delivering at its share (contract/budget.json, store).
CREATE TABLE IF NOT EXISTS spend (day TEXT PRIMARY KEY, written INTEGER NOT NULL DEFAULT 0) WITHOUT ROWID;

-- The board's first home (14 November 2026, messages 1 to 4). It moved the same day to its own
-- service, agents.seansooch.dev, which holds a copy with the same ids. Kept as the record; nothing writes here.
CREATE TABLE IF NOT EXISTS board (
  id INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL,
  from_agent TEXT NOT NULL, to_agent TEXT NOT NULL, channel TEXT NOT NULL, kind TEXT NOT NULL,
  re INTEGER, subject TEXT NOT NULL, body TEXT, refs TEXT, status TEXT
);
CREATE INDEX IF NOT EXISTS board_re ON board(re);
CREATE TABLE IF NOT EXISTS board_cursors (agent TEXT PRIMARY KEY, last_id INTEGER NOT NULL, seen_at TEXT NOT NULL);
