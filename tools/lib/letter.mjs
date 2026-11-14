// The Newsletter: one letter a day by Soochiebot, from that day's edition (contract/NEWSLETTER.md). It is
// written outside this repo by a program, so nothing about it is trusted: checkLetter lists every rule it
// breaks, in words. Pure: no file, no clock, no network.

export const LETTER_SCHEMA = 'mts.letter/1';
const KEYS = ['schema', 'date', 'published', 'model', 'subject', 'summary', 'lead', 'notes', 'read', 'sources', 'figures'];
export const LETTER_WORDS = [200, 800];
const NOTE_MOST = 120;

const ch = (...codes) => codes.map((c) => String.fromCodePoint(c)).join('');
const DASHES = ch(0x2012, 0x2013, 0x2014, 0x2015, 0x2212);
const QUOTES = '"' + ch(0x201C, 0x201D, 0x201E, 0xAB, 0xBB, 0x2018, 0x201A, 0x201B, 0x2039, 0x203A);
// An address a reader could follow: a scheme, a www, or a host with a path. A name with a dot in it
// (Crypto.com Arena) is not one.
const ADDRESS = /[A-Za-z][A-Za-z0-9+.-]*:\/\/|\bwww\.|\b[A-Za-z0-9-]+\.[A-Za-z]{2,}\/\S/i;
const PICTO = /\p{Extended_Pictographic}|\p{So}/u;
// A quantity of a drug. The short units are matched as written (mL, IU), so ML engineers and an IU win are not doses.
const DOSE = /(?:\d|\b(?:half|one|two|three|four|five|six|seven|eight|nine|ten|twenty|fifty|hundred)\b)\s*(?:mg|mcg|[µμ]g|mL|ml|IU(?! win| loss| game| fans)|mEq|[Mm]illigrams?|[Mm]icrograms?|[Uu]nits?\/kg|[Uu]nits? of insulin)(?![A-Za-z])/;
export const BRACE = /\{([a-z][a-z0-9_]*)\}/g;
const KEY = /^[a-z][a-z0-9_]*$/;
const STORY = /^\d{4}-\d{2}-\d{2}(-[a-z0-9]+)+$/;
const POST_ID = /^\d{10,20}$/;
const HANDLE = /^[A-Za-z0-9_]{1,15}$/;
const FIGURE = /^[+-]?[$]?\d[\d,.:/-]*( ?(%|[KMBT]|x|percent|thousand|million|billion|trillion))?$/;
const YEAR = /^(19|20)\d\ds?$/;
const CURRENCY = '$' + ch(0xA3, 0xA5, 0x20AC);
// Letters after digits that make a quantity, not a name: 40pts and 35mph are numbers, 49ers and 4chan are not.
const UNITS = new Set(['mph', 'kph', 'pts', 'min', 'mins', 'sec', 'secs', 'yds', 'lbs', 'pct', 'pc', 'percent', 'mil', 'bil', 'usd', 'eur', 'gbp',
  'yrs', 'hrs', 'days', 'games', 'wins', 'points', 'yards', 'votes', 'seats', 'views', 'times', 'fold']);
const SCALES = new Set(['K', 'M', 'B', 'T', 'BN', 'MM', 'X']); // 40K and 5B are numbers; 5G, 3D and 2FA are names
const SCALE_WORDS = new Set(['hundred', 'thousand', 'million', 'billion', 'trillion', 'percent', 'pct', 'bn', 'mn']);
const NAMED_NUMBERS = new Set(['9/11', '7-Eleven']);
// A capitalised word that is not a name, so the number after it is a count: "About 40 people", not "Game 7".
const NOT_NAMES = new Set(('about around roughly nearly almost over under some only just the a an at in on by with for from to after before and '
  + 'but then now still all another up down top plus minus between among of its their his her our that this these those '
  + 'more less fewer exactly approximately within when while if as since until per each every both than').split(' '));
const reEsc = (s) => s.replace(/[.*+?^${}()|[\]\\/-]/g, '\\$&');
const TRIM = new RegExp(`^[^0-9A-Za-z${reEsc(CURRENCY)}]+|[^0-9A-Za-z%]+$`, 'g');

function realDay(s) {
  if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const d = new Date(`${s}T00:00:00Z`);
  return !Number.isNaN(d.getTime()) && d.toISOString().slice(0, 10) === s;
}
const words = (s) => s.split(/\s+/).filter(Boolean).length;
const inWords = (n) => ['no', 'one', 'two', 'three', 'four', 'five'][n] ?? String(n);

// The numbers a sentence types for itself, which the format refuses: every number is a figure with a source.
// Not a number: a year (2026, the 1990s); a name that starts with a letter (GPT-5, F-35, COVID-19); a name that
// starts with digits (49ers, 4chan, 5G, 3D); and a plain version or ordinal straight after a name (Gemini 4,
// Fable 5.2, Game 7, November 12). Anything else with a digit is: 35.7M, 12%, $40B, 31-17, ~40%, +12, 12-point,
// 40-year-old, 40pts, 7th, a count after an ordinary word (about 40 people), and a number before a scale word
// (Tesla 40 billion). A net with holes a careful writer could find (top-10, Lions 31, cut 2000 jobs): the
// reviewer and the figures list are the rest.
export function typedNumbers(s) {
  const out = [];
  const tokens = s.replace(BRACE, 'figure').split(/\s+/).filter(Boolean);
  tokens.forEach((token, i) => {
    if (!/\d/.test(token)) return;
    const core = token.replace(TRIM, '').replace(/['’]s$/, '');
    if (!core || YEAR.test(core) || /^[A-Za-z]/.test(core) || NAMED_NUMBERS.has(core)) return;
    const tail = /^\d+([A-Za-z]+)$/.exec(core);
    if (tail && ((tail[1].length >= 3 && !UNITS.has(tail[1].toLowerCase())) || (tail[1] === tail[1].toUpperCase() && !SCALES.has(tail[1])))) return;
    const before = i ? tokens[i - 1] : '';
    const after = i + 1 < tokens.length ? tokens[i + 1].replace(/[^A-Za-z]+/g, '').toLowerCase() : '';
    const named = /[A-Z]/.test(before) && /[A-Za-z0-9]$/.test(before) && !NOT_NAMES.has(before.toLowerCase()) && !SCALE_WORDS.has(after);
    if (/^\d+(\.\d+)*$/.test(core) && named) return;
    out.push(core);
  });
  return out;
}

// What is wrong with one string of a letter. Sentences (numbers true) may not hold a number of their own.
export function textProblems(where, s, numbers = true) {
  if (typeof s !== 'string' || !s.trim()) return [`${where} is not text`];
  const bad = [];
  if ([...DASHES].some((c) => s.includes(c)) || s.includes('--')) bad.push(`${where} has a dash that is not a hyphen`);
  if ([...QUOTES].some((c) => s.includes(c)) || /(?:^|[\s(])'(?=[A-Za-z])/.test(s)) bad.push(`${where} has a quotation mark (nothing is quoted)`);
  if (ADDRESS.test(s)) bad.push(`${where} has a web address typed into it`);
  if (PICTO.test(s) || /[️‍]/.test(s)) bad.push(`${where} has an emoji or a pictograph`);
  if (/[<>]/.test(s)) bad.push(`${where} has markup in it`);
  if (DOSE.test(s)) bad.push(`${where} reads as a dose`);
  if (/[\u0000-\u001f\u007f]/.test(s)) bad.push(`${where} has a line break or a control character`);
  if (numbers) {
    for (const n of typedNumbers(s)) bad.push(`${where} types the number ${n} (make it a figure and ask for it in braces)`);
    const rest = s.replace(BRACE, '');
    if (rest.includes('{') || rest.includes('}')) bad.push(`${where} has a brace that is not a figure`);
  }
  return bad;
}

// Every rule of contract/NEWSLETTER.md that `letter` breaks. `stem` is the day its file is named for; `desks`
// the desk ids it may name; `known.story(id)` says whether a story is in that day's edition, `known.post(id)` whether
// a post is one X confirmed that the record holds and may show. That is all a letter may cite.
export function checkLetter(letter, stem, desks, known) {
  if (!letter || typeof letter !== 'object' || Array.isArray(letter)) return ['it is not a letter (one JSON object)'];
  const bad = [];
  const extra = Object.keys(letter).filter((k) => !KEYS.includes(k));
  const missing = KEYS.filter((k) => !(k in letter));
  if (extra.length) bad.push(`it has a key the format does not name: ${extra.join(', ')}`);
  if (missing.length) return [...bad, `it lacks: ${missing.join(', ')}`];

  function shaped(where, obj, keys) {
    if (!obj || typeof obj !== 'object' || Array.isArray(obj)) { bad.push(`${where} is not an object`); return false; }
    const more = Object.keys(obj).filter((k) => !keys.includes(k));
    const less = keys.filter((k) => !(k in obj));
    if (more.length) bad.push(`${where} has a key the format does not name: ${more.join(', ')}`);
    if (less.length) bad.push(`${where} lacks: ${less.join(', ')}`);
    return !less.length;
  }

  if (letter.schema !== LETTER_SCHEMA) bad.push(`its schema is not ${LETTER_SCHEMA}`);
  if (!realDay(letter.date) || letter.date !== stem) bad.push('its date is not the day its file is named for');
  if (!realDay(letter.published) || (realDay(letter.date) && letter.published <= letter.date)) bad.push('published is not a real day after the day it covers');
  bad.push(...textProblems('model', letter.model, false));
  if (typeof letter.model === 'string' && letter.model.length > 60) bad.push('model is longer than 60 characters');
  if (typeof letter.subject === 'string' && (letter.subject.length < 20 || letter.subject.length > 90)) bad.push('its subject is not 20 to 90 characters');
  if (typeof letter.summary === 'string' && letter.summary.length > 220) bad.push('its summary is longer than 220 characters');
  for (const where of ['subject', 'summary']) {
    if (typeof letter[where] === 'string' && new RegExp(BRACE.source).test(letter[where])) bad.push(`the ${where} asks for a figure: figures belong in the body, beside their source`);
  }

  const sources = letter.sources && typeof letter.sources === 'object' && !Array.isArray(letter.sources) ? letter.sources : {};
  const figures = letter.figures && typeof letter.figures === 'object' && !Array.isArray(letter.figures) ? letter.figures : {};
  if (sources !== letter.sources || figures !== letter.figures) bad.push('sources and figures are objects, each entry under a key');
  for (const [k, src] of Object.entries(sources)) {
    const where = `source ${k}`;
    if (!KEY.test(k)) bad.push(`${where}: its key is not plain lowercase`);
    if (!src || typeof src !== 'object' || ('story' in src) === ('post' in src)) { bad.push(`${where} must be either a story or a post`); continue; }
    if (!shaped(where, src, 'story' in src ? ['story'] : ['post', 'handle'])) continue;
    if ('story' in src) {
      if (typeof src.story !== 'string' || !STORY.test(src.story)) bad.push(`${where}: story is not the id of one of the situation's stories`);
      else if (!known.story(src.story)) bad.push(`${where}: the story ${src.story} is not in this day's edition`);
    } else {
      if (typeof src.post !== 'string' || !POST_ID.test(src.post)) bad.push(`${where}: post is not the id of a post on X`);
      else if (!known.post(src.post)) bad.push(`${where}: the post ${src.post} is not one X confirmed that the record may show`);
      if (typeof src.handle !== 'string' || !HANDLE.test(src.handle)) bad.push(`${where}: handle is not an account name`);
    }
  }
  const values = {};
  for (const [k, fig] of Object.entries(figures)) {
    const where = `figure ${k}`;
    if (!KEY.test(k)) bad.push(`${where}: its key is not plain lowercase`);
    if (!shaped(where, fig, ['value', 'of', 'source'])) continue;
    if (typeof fig.value === 'string' && FIGURE.test(fig.value)) values[k] = fig.value;
    else bad.push(`${where}: value is not a number as a reader writes one (35.7M, 12%, $40 billion, 31-17)`);
    bad.push(...textProblems(`${where}: of`, fig.of, false));
    if (typeof fig.of === 'string' && fig.of.length > 60) bad.push(`${where}: of is longer than 60 characters`);
    if (typeof fig.source !== 'string' || !(fig.source in sources)) bad.push(`${where} names ${JSON.stringify(fig.source)}, which is not a source`);
    if (k in values && typeof fig.of === 'string' && DOSE.test(`${values[k]} ${fig.of}`)) bad.push(`${where} reads as a dose`);
  }

  const prose = [['the subject', letter.subject], ['the summary', letter.summary]];
  const body = [];
  const cited = [];
  function cites(where, obj, least) {
    const got = obj.cites;
    if (!Array.isArray(got) || !got.every((c) => typeof c === 'string')) { bad.push(`${where}: cites is not a list of source keys`); return; }
    for (const c of got) if (!(c in sources)) bad.push(`${where} cites ${JSON.stringify(c)}, which is not a source`);
    if (got.length < least) bad.push(`${where} cites nothing`);
    cited.push(...got);
  }
  function paragraphs(where, text, most) {
    if (!Array.isArray(text) || text.length < 1 || text.length > most) { bad.push(`${where}: text is not a list of one to ${inWords(most)} paragraphs`); return; }
    text.forEach((p, i) => { prose.push([`${where} paragraph ${i + 1}`, p]); body.push(p); });
  }

  if (shaped('the lead', letter.lead, ['desk', 'head', 'text', 'cites'])) {
    const lead = letter.lead;
    if (typeof lead.desk !== 'string' || !desks.has(lead.desk)) bad.push(`the lead names a desk that is not one: ${JSON.stringify(lead.desk)}`);
    prose.push(['the lead heading', lead.head]);
    paragraphs('the lead', lead.text, 3);
    cites('the lead', lead, 1);
  }
  const notes = Array.isArray(letter.notes) ? letter.notes : [];
  if (notes.length < 2 || notes.length > 4) bad.push(`it has ${notes.length < 20 ? inWords(notes.length) : 'too many'} notes, not two to four`);
  const seen = letter.lead && typeof letter.lead.desk === 'string' ? [letter.lead.desk] : [];
  notes.slice(0, 8).forEach((note, i) => {
    const where = `note ${i + 1}`;
    if (!shaped(where, note, ['desk', 'head', 'text', 'cites'])) return;
    if (typeof note.desk !== 'string' || !desks.has(note.desk)) bad.push(`${where} names a desk that is not one: ${JSON.stringify(note.desk)}`);
    else if (seen.includes(note.desk)) bad.push(`${where} uses the desk ${note.desk} twice`);
    seen.push(note.desk);
    prose.push([`${where} heading`, note.head], [where, note.text]);
    body.push(note.text);
    if (typeof note.text === 'string' && words(note.text) > NOTE_MOST) bad.push(`${where} is longer than ${NOTE_MOST} words`);
    cites(where, note, 1);
  });
  if (shaped('the read', letter.read, ['text', 'cites'])) {
    paragraphs('the read', letter.read.text, 2);
    cites('the read', letter.read, 0);
  }

  const asked = new Set();
  for (const [where, s] of prose) {
    bad.push(...textProblems(where, s));
    if (typeof s !== 'string') continue;
    for (const [, key] of s.matchAll(BRACE)) {
      asked.add(key);
      if (!(key in figures)) bad.push(`${where} asks for {${key}}, which is not a figure`);
    }
    if (!DOSE.test(s) && DOSE.test(s.replace(BRACE, (_, k) => values[k] ?? ''))) bad.push(`${where} reads as a dose`);
  }
  for (const k of Object.keys(sources)) if (!cited.includes(k)) bad.push(`source ${k} is cited nowhere`);
  for (const k of Object.keys(figures)) if (!asked.has(k)) bad.push(`figure ${k} is asked for nowhere`);
  const count = body.filter((s) => typeof s === 'string').reduce((n, s) => n + words(s), 0);
  if (count > LETTER_WORDS[1]) bad.push(`it is ${count} words: the most is ${LETTER_WORDS[1]}`);
  if (count < LETTER_WORDS[0]) bad.push(`it is ${count} words: the least is ${LETTER_WORDS[0]}`);
  return bad;
}
