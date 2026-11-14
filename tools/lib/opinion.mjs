// The paper's one opinion a day (contract/PAPER.md, "The opinion"). Written outside this repo by
// Soochiebot, so nothing about it is trusted: checkOpinion lists every rule it breaks, in words.
// Pure: no file, no clock, no network.

export const OPINION_SCHEMA = 'mts.opinion/1';
const KEYS = ['schema', 'date', 'published', 'model', 'head', 'text', 'cites'];
const WORDS = [120, 400];

const ch = (...codes) => codes.map((c) => String.fromCodePoint(c)).join('');
const DASHES = ch(0x2012, 0x2013, 0x2014, 0x2015, 0x2212);
const QUOTES = '"' + ch(0x201C, 0x201D, 0x201E, 0xAB, 0xBB, 0x2018, 0x201A, 0x201B, 0x2039, 0x203A);
const ADDRESS = /[A-Za-z][A-Za-z0-9+.-]*:\/\/|\bwww\.|\b[A-Za-z0-9-]+\.[A-Za-z]{2,}\/\S|\b[A-Za-z0-9-]+\.(com|org|net|io|dev|gov|edu|co|ai|app)\b/i;
const PICTO = /\p{Extended_Pictographic}/u;
const DOSE = /(?:\d|\b(?:half|one|two|three|four|five|six|seven|eight|nine|ten|twenty|fifty|hundred)\b)\s*(?:mg|mcg|[µμ]g|mL|ml|IU|mEq|milligrams?|micrograms?|units? of insulin)(?![A-Za-z])/i;
const YEAR = /^(19|20)\d\ds?$/;
const NAMED = new Set(['9/11', '7-Eleven']);

function realDay(s) {
  if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const d = new Date(`${s}T00:00:00Z`);
  return !Number.isNaN(d.getTime()) && d.toISOString().slice(0, 10) === s;
}

// The numbers a sentence types for itself. An editorial has none: the figures are on the page beside
// it, from the record. A year and a name that starts with a letter (GPT-5) are not numbers.
export function typedNumbers(s) {
  const out = [];
  for (const token of s.split(/\s+/)) {
    if (!/\d/.test(token)) continue;
    const core = token.replace(/^[^0-9A-Za-z$]+|[^0-9A-Za-z%]+$/g, '').replace(/['’]s$/, '');
    if (!core || YEAR.test(core) || /^[A-Za-z]/.test(core) || NAMED.has(core)) continue;
    out.push(core);
  }
  return out;
}

function words(where, s) {
  if (typeof s !== 'string' || !s.trim()) return [`${where} is not text`];
  const bad = [];
  if ([...DASHES].some((c) => s.includes(c)) || s.includes('--')) bad.push(`${where} has a dash that is not a hyphen`);
  if ([...QUOTES].some((c) => s.includes(c)) || /(?:^|[\s(])'(?=[A-Za-z])/.test(s)) bad.push(`${where} has a quotation mark (nothing is quoted)`);
  if (ADDRESS.test(s)) bad.push(`${where} has a web address typed into it`);
  if (PICTO.test(s)) bad.push(`${where} has an emoji or a pictograph`);
  if (/[<>]/.test(s)) bad.push(`${where} has markup in it`);
  if (/[\u0000-\u001f\u007f]/.test(s)) bad.push(`${where} has a line break or a control character`);
  if (DOSE.test(s)) bad.push(`${where} reads as a dose`);
  for (const n of typedNumbers(s)) bad.push(`${where} types the number ${n} (an editorial has none of its own)`);
  return bad;
}

// Every rule of the opinion that `op` breaks. `day` is the edition's day; `known` holds every story id
// and post id in that edition, which is all an opinion may cite.
export function checkOpinion(op, day, known) {
  if (!op || typeof op !== 'object' || Array.isArray(op)) return ['it is not an opinion (one JSON object)'];
  const bad = [];
  const extra = Object.keys(op).filter((k) => !KEYS.includes(k));
  const missing = KEYS.filter((k) => !(k in op));
  if (extra.length) bad.push(`it has a key the format does not name: ${extra.join(', ')}`);
  if (missing.length) return [...bad, `it lacks: ${missing.join(', ')}`];
  if (op.schema !== OPINION_SCHEMA) bad.push(`its schema is not ${OPINION_SCHEMA}`);
  if (op.date !== day) bad.push(`its date is not ${day}, the edition it is for`);
  if (!realDay(op.published) || op.published <= op.date) bad.push('published is not a real day after the day it covers');
  if (typeof op.model !== 'string' || !op.model.trim() || op.model.length > 60) bad.push('model is not a name of 60 characters or fewer');
  bad.push(...words('the head', op.head));
  if (typeof op.head === 'string' && (op.head.length < 20 || op.head.length > 100)) bad.push('the head is not 20 to 100 characters');
  if (!Array.isArray(op.text) || op.text.length < 1 || op.text.length > 4) {
    bad.push('text is not a list of one to four paragraphs');
  } else {
    op.text.forEach((p, i) => bad.push(...words(`paragraph ${i + 1} of the text`, p)));
    const count = op.text.filter((p) => typeof p === 'string').reduce((n, p) => n + p.split(/\s+/).filter(Boolean).length, 0);
    if (count < WORDS[0]) bad.push(`it is ${count} words: the least is ${WORDS[0]}`);
    if (count > WORDS[1]) bad.push(`it is ${count} words: the most is ${WORDS[1]}`);
  }
  if (!Array.isArray(op.cites) || !op.cites.length || !op.cites.every((c) => typeof c === 'string')) {
    bad.push('cites is not a list of the stories and posts it rests on');
  } else {
    for (const c of op.cites) if (!known.has(c)) bad.push(`it cites ${c}, which is not in this edition`);
  }
  return bad;
}
