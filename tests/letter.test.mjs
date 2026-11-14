// The Newsletter's rules (contract/NEWSLETTER.md, tools/lib/letter.mjs). A letter is written outside this repo
// by a program; every rule here has a case that breaks it, and an unbroken letter as the control.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { checkLetter, typedNumbers } from '../tools/lib/letter.mjs';

const DAY = '2026-11-12';
const desks = new Set(['business', 'ai', 'sports', 'tech', 'music', 'gaming', 'world']);
const ids = new Set(['2026-11-12-a-made-up-story', '2120640219871384044']);
const known = { story: (id) => ids.has(id), post: (id) => ids.has(id) };
const pad = (s, n) => s + ' More words in the same plain voice.'.repeat(n);

function letter() {
  return {
    schema: 'mts.letter/1', date: DAY, published: '2026-11-13', model: 'Test Model 5',
    subject: 'A made up day for the tests to read', summary: 'One sentence that says what the day was about.',
    lead: { desk: 'business', head: 'The lead heading',
      text: [pad('The first paragraph of the lead, about GPT-5 and the F-35 in 2026.', 14), 'The second paragraph says the post drew {views} views.'],
      cites: ['story', 'post'] },
    notes: [
      { desk: 'ai', head: 'The AI heading', text: pad('A note about the AI desk.', 6), cites: ['story'] },
      { desk: 'sports', head: 'The sports heading', text: pad('A note about the sports desk.', 6), cites: ['post'] },
    ],
    read: { text: [pad('What the day adds up to, in **one** paragraph.', 8)], cites: [] },
    sources: { story: { story: '2026-11-12-a-made-up-story' }, post: { post: '2120640219871384044', handle: 'Some_Account' } },
    figures: { views: { value: '35.7M', of: 'views on the post', source: 'post' } },
  };
}
const check = (l) => checkLetter(l, DAY, desks, known);

test('the unbroken letter has no problem', () => {
  assert.deepEqual(check(letter()), []);
});

test('a letter that breaks a rule is refused, and the rule is named', () => {
  const em = String.fromCharCode(0x2014), en = String.fromCharCode(0x2013), lq = String.fromCharCode(0x201C), rq = String.fromCharCode(0x201D);
  const lead = (s) => (l) => l.lead.text.push(s);
  const broken = {
    'an em dash': [lead(`One thing ${em} then another.`), 'dash'],
    'an en dash in the subject': [(l) => { l.subject = `A made up day ${en} for the tests`; }, 'dash'],
    'a double hyphen': [lead('One thing -- then another.'), 'dash'],
    'a quotation': [lead(`He said ${lq}never${rq} and left.`), 'quotation'],
    'a straight quotation': [(l) => { l.notes[0].text += ' He said "never".'; }, 'quotation'],
    'a single quotation': [lead("He said 'never' and left."), 'quotation'],
    'a typed count': [lead('It drew 35.7M views.'), 'the number 35.7M'],
    'a typed share': [lead('It rose 12% on the day.'), 'the number 12%'],
    'a typed score': [lead('They won 31-17 at home.'), 'the number 31-17'],
    'a typed sum': [(l) => l.read.text.push('The deal is worth $40B.'), 'the number $40B'],
    'a number behind a sign': [lead('It rose (~40%) on the day.'), 'the number 40%'],
    'an age': [lead('The 40-year-old said so.'), 'the number 40-year-old'],
    'an ordinal': [lead('It is their 7th win.'), 'the number 7th'],
    'a count after an ordinary word': [lead('There were roughly 40 people.'), 'the number 40 '],
    'a sum after a name': [lead('It cost Tesla 40 billion in a day.'), 'the number 40 '],
    'a figure in the subject': [(l) => { l.subject = 'A made up day that drew {views} views'; }, 'the subject asks for a figure'],
    'an address': [lead('Read it at example.xyz/page now.'), 'address'],
    'a scheme': [lead('Read it at https://example.com now.'), 'address'],
    'an emoji': [lead('Big day ' + String.fromCodePoint(0x1F680)), 'emoji'],
    'a pictograph': [lead('Big day ' + String.fromCodePoint(0x2B50)), 'emoji'],
    'markup': [lead('A <b>bold</b> claim.'), 'markup'],
    'a dose in words': [lead('They gave five mg at once.'), 'dose'],
    'a dose as a figure': [(l) => { l.figures.dose = { value: '500', of: 'what was given', source: 'post' }; l.lead.text.push('They gave {dose} mg at once.'); }, 'dose'],
    'a key the format does not name': [(l) => { l.mood = 'grim'; }, 'mood'],
    'a label on a source': [(l) => { l.sources.story.label = 'The story'; }, 'label'],
    'a story not in the edition': [(l) => { l.sources.story.story = '2026-11-12-another-story'; }, 'not in this day'],
    'a post the record does not hold': [(l) => { l.sources.post.post = '2120640219871384045'; }, 'not one X confirmed'],
    'a story that is not an id': [(l) => { l.sources.story.story = '../../etc/passwd'; }, 'story is not the id'],
    'a handle that is not one': [(l) => { l.sources.post.handle = 'some/account'; }, 'handle'],
    'a source that is both': [(l) => { l.sources.post.story = '2026-11-12-a-made-up-story'; }, 'either'],
    'a desk that is not one': [(l) => { l.lead.desk = 'gossip'; }, 'gossip'],
    "a note on the lead's desk": [(l) => { l.notes[1].desk = 'business'; }, 'twice'],
    'one note': [(l) => { l.notes.pop(); }, 'two to four'],
    'a cite with no source': [(l) => l.lead.cites.push('ghost'), 'ghost'],
    'a source nothing cites': [(l) => { l.sources.spare = { story: '2026-11-12-a-made-up-story' }; }, 'spare'],
    'a lead that cites nothing': [(l) => { l.lead.cites = []; l.notes[0].cites.push('post'); }, 'the lead cites nothing'],
    'a figure nothing asks for': [(l) => { l.figures.extra = { value: '9', of: 'things', source: 'post' }; }, 'extra'],
    'a brace with no figure': [lead('It drew {reposts} reposts.'), 'reposts'],
    'a figure that is not a number': [(l) => { l.figures.views.value = 'a great many'; }, 'value'],
    'a day that is not the file': [(l) => { l.date = '2026-11-11'; }, 'file'],
    'published before its day': [(l) => { l.published = '2026-11-12'; }, 'published'],
    'a note too long': [(l) => { l.notes[0].text = pad('Long.', 30); }, 'longer than 120'],
    'too many words': [lead(pad('Padding.', 120)), 'the most is 800'],
    'too few words': [(l) => { l.lead.text = ['Short.']; l.read.text = ['Short.']; l.figures = {}; l.notes.forEach((n) => { n.text = 'Short.'; }); }, 'the least is 200'],
    'another schema': [(l) => { l.schema = 'mts.letter/2'; }, 'schema'],
    'a paragraph that is not text': [(l) => { l.lead.text = [{ html: 'x' }]; }, 'is not text'],
  };
  for (const [what, [change, names]] of Object.entries(broken)) {
    const l = letter();
    change(l);
    const bad = check(l);
    assert.ok(bad.some((b) => b.includes(names)), `${what}: expected a problem naming "${names}", got ${JSON.stringify(bad)}`);
  }
});

test('a name with digits in it is not a typed number', () => {
  for (const said of ['It runs on GPT-5 and the F-35 flies.', 'This was COVID-19 again in the 2020s.', 'Google shipped Gemini 4 today.',
    'The Lions won Game 7 at home.', 'It happened on November 12 in Detroit.', 'The 49ers and the 76ers both won.', 'It spread on 4chan first.',
    'The carriers sell 5G and the film is in 3D.', "It was 2026's largest deal.", 'Gemini 4 arrives today.', 'They met at 7-Eleven, years after 9/11.',
    'It was at Crypto.com Arena.', 'The ML team at IU shipped it.']) {
    assert.deepEqual(typedNumbers(said), [], said);
    const l = letter();
    l.read.text = [l.read.text[0] + ' ' + said];
    assert.deepEqual(check(l), [], said);
  }
});

test('a figure is a number as a reader writes one', () => {
  for (const value of ['35.7M', '12%', '$40 billion', '31-17', '-3.2%', '+4', '$1.2T', '3x', '1977-78']) {
    const l = letter();
    l.figures.views.value = value;
    assert.deepEqual(check(l), [], value);
  }
  for (const value of ['a lot', '', 'about 40', '<b>4</b>']) {
    const l = letter();
    l.figures.views.value = value;
    assert.ok(check(l).some((b) => b.includes('value is not a number')), value);
  }
});

test('a file that is not a letter is refused', () => {
  for (const v of [null, [], 'a letter', 4]) assert.deepEqual(check(v), ['it is not a letter (one JSON object)']);
});
