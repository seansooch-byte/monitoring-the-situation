// INVENTED stories, used only to test the design before the grabber's first capture.
// No real person, company, team or event is described here, and the build refuses to
// produce a deployable site from this data. Every handle starts with "demo_".
//
// start: hours before "now" that the first post went up. Each post: at (minutes after the
// start), v (views it levels off at), tau (hours to reach about two thirds of that).

export const STORIES = [
  {
    slug: 'old-lighthouse-webcam', desks: ['offbeat'], beat: 'nature', standing: 'established', start: 61,
    title: 'A lighthouse webcam catches the same seal on the same rock for the ninth day',
    dek: 'This invented story is more than two days old, so it belongs in the archive and not on the bulletin.',
    what: ['A harbour webcam has shown one seal returning to one rock at the same hour for nine days.'],
    why: 'People have started setting alarms for it.',
    posts: [{ role: 'origin', at: 0, v: 900000, tau: 9, handle: 'demo_harbourcam', name: 'Harbour Cam', kind: 'creator', followers: 21000, text: 'day nine. same rock.', media: [{ type: 'photo', description: 'A seal lying on a rock below a lighthouse', duration_s: null }] }],
  },
  {
    slug: 'dog-walks-onto-forecast', desks: ['offbeat', 'internet'], beat: 'animals', standing: 'established', start: 9.5,
    title: 'A dog walks onto a live weather forecast and stays for the whole thing',
    dek: 'A local forecaster kept going for four minutes with a retriever asleep on the map. The clip is the most viewed thing on the platform today.',
    what: ['A regional station was halfway through its evening forecast when a golden retriever wandered into frame, lay down in front of the map and did not move. The forecaster stepped around it, finished the seven day outlook and signed off without mentioning it.', 'The station says the dog belongs to a camera operator and has been in the building before, though not on air.'],
    why: 'Nothing is at stake and nobody is arguing. People are passing it along because the forecaster never breaks, and replies have turned into a contest of captions for the dog.',
    posts: [
      { role: 'origin', at: 0, v: 21400000, tau: 3.2, handle: 'demo_tvclips', name: 'Clips From The Desk', kind: 'aggregator', followers: 812000, text: 'he just. kept. doing the weather', media: [{ type: 'video', description: 'A studio weather forecast; a golden retriever lies in front of the map while the forecaster points over it', duration_s: 244 }] },
      { role: 'reply', at: 38, v: 2900000, tau: 2.5, handle: 'demo_marnie', name: 'marnie', kind: 'person', followers: 4100, text: 'the dog is the only one in that building who knows it is not going to rain <3 & he is right' },
      { role: 'official', at: 95, v: 3600000, tau: 4, handle: 'demo_station6', name: 'Channel 6 Weather', kind: 'news', followers: 96000, text: 'His name is Biscuit. He has been promoted to chief meteorologist effective immediately.' },
    ],
  },
  {
    slug: 'calendar-typo-moves-yields', desks: ['markets', 'politics'], beat: 'rates', standing: 'disputed', start: 6.2,
    title: 'Did a typo on a central bank calendar move bond yields for nine minutes?',
    dek: 'A screenshot of a meeting date listed a week early spread fast, and yields jumped. Traders disagree about whether one caused the other.',
    what: ['A screenshot of a central bank events page showed the next rate meeting a week earlier than scheduled. The page was corrected within minutes. In the same window, two year yields rose sharply and then gave most of it back.', 'The bank has confirmed the page carried the wrong date briefly and says the schedule never changed.'],
    why: 'It is a clean story about markets running on screenshots, which both the people who love that idea and the people who hate it want to share.',
    worlds: [
      { name: 'Trading desks', sees: 'A market so wound up about the next meeting that a web page typo was enough to set it off. The move is the story, and it is funny.', post: 0 },
      { name: 'Macro skeptics', sees: 'The move had started before the screenshot existed, on a weak auction. The typo story is being told backwards because it is more fun.', post: 1 },
    ],
    common: 'The wrong date was real and was live for about six minutes. Yields did rise in that window. The first post with the screenshot went up roughly two minutes after the rise began, which fits the skeptics better than the joke does, but no one has shown what the earliest traders were reacting to.',
    next: 'The bank publishes its page change log on Fridays.',
    posts: [
      { role: 'origin', at: 0, v: 4800000, tau: 1.8, handle: 'demo_basispoint', name: 'basis point enjoyer', kind: 'person', followers: 61000, text: 'the 2y just moved 9bp because someone fat fingered a calendar invite. this is the most important market in the world', media: [{ type: 'photo', description: 'Screenshot of an events page listing a rate meeting; one date is circled in red', duration_s: null }] },
      { role: 'voice', at: 24, v: 1300000, tau: 2.2, handle: 'demo_curvewatch', name: 'Curve Watch', kind: 'person', followers: 38000, text: 'Check your timestamps. The selloff starts at :41, the screenshot is posted at :43. Tail on the auction was the trigger. Fun story though.' },
      { role: 'official', at: 71, v: 900000, tau: 3, handle: 'demo_bankpress', name: 'Reserve Press Office', kind: 'official', followers: 240000, text: 'An events page briefly displayed an incorrect date this morning. The published meeting schedule is unchanged.' },
    ],
  },
  {
    slug: 'leaf-blower-vote', desks: ['politics', 'life'], beat: 'states', standing: 'established', start: 13,
    title: 'A town bans leaf blowers before 9 a.m. and the whole country has an opinion',
    dek: 'A three minute clip of a council meeting has become a fight about what local government is for.',
    what: ['A town council voted five to two to bar gas leaf blowers before nine in the morning. A resident filmed the public comment period, where a landscaper and a night shift nurse spoke back to back.', 'The rule carries a warning for a first complaint and a small fine after that.'],
    why: 'The clip has two sympathetic people on opposite sides, which lets everyone pick the half that proves their point.',
    worlds: [
      { name: 'Seen as overreach', sees: 'A council telling working people when they are allowed to do their jobs. The landscaper is the one being quoted, and the fine is described as a tax on small crews.', post: 1 },
      { name: 'Seen as common courtesy', sees: 'A modest noise rule of the kind most towns already have. The nurse is the one being quoted, and the vote is described as neighbours solving a neighbour problem.', post: 2 },
    ],
    common: 'Both speakers are in the same unedited clip and each side is sharing half of it. The rule covers gas blowers only, starts in the spring, and the first complaint is a warning. Nobody at the meeting proposed a ban on the work itself.',
    posts: [
      { role: 'origin', at: 0, v: 6100000, tau: 5, handle: 'demo_townhall', name: 'Meeting Clips', kind: 'aggregator', followers: 133000, text: 'Public comment on the leaf blower ordinance. Watch both speakers.', media: [{ type: 'video', description: 'A council chamber; a man in a work jacket speaks at a lectern, then a woman in scrubs', duration_s: 187 }] },
      { role: 'voice', at: 64, v: 3900000, tau: 4, handle: 'demo_freetown', name: 'Leave Us Alone', kind: 'person', followers: 210000, text: '"I start at 7 because my customers leave at 8." Fined for working. This is what they do with a majority.' },
      { role: 'voice', at: 102, v: 3300000, tau: 4.5, handle: 'demo_nightshift', name: 'tired RN', kind: 'person', followers: 18000, text: '"I get home at 7:40 and I have to be back at 7." She asked for 80 minutes of quiet. That is the tyranny.' },
    ],
  },
  {
    slug: 'sped-up-demo', desks: ['ai', 'tech'], beat: 'labs', standing: 'developing', start: 4.4,
    title: 'A lab is accused of speeding up its robot demo',
    dek: 'Frame counts from a wall clock in the background suggest the video runs at roughly twice real speed. The lab has not answered.',
    what: ['A small lab posted a ninety second video of a robot arm folding laundry. Within the hour, viewers noticed a wall clock in the background whose second hand moves about twice as fast as it should.', 'The lab has not replied to questions. The video is still up.'],
    why: 'Demo videos have burned this audience before, and a clock in the background is the kind of evidence anyone can check for themselves.',
    worlds: [
      { name: 'Builders', sees: 'Speeding up a demo is normal and usually labelled. The folding itself is real progress, and the pile-on is from people who have never shipped hardware.', post: 2 },
      { name: 'Skeptics', sees: 'An unlabelled speed-up is the whole problem. If the clock had not been in frame nobody would know, and that is why demos are not trusted.', post: 1 },
    ],
    common: 'The clock does run fast: three separate frame counts put the video between 1.8 and 2.1 times real speed. The post does not say the video was sped up. Whether the robot can do the task at all is not in dispute.',
    next: 'Whether the lab posts the raw footage.',
    posts: [
      { role: 'origin', at: 0, v: 3900000, tau: 1.6, handle: 'demo_foldlab', name: 'Foldwork', kind: 'brand', followers: 27000, text: 'One arm. One camera. One take. Laundry is solved.', media: [{ type: 'video', description: 'A robot arm folds three shirts on a table; a wall clock is visible behind it', duration_s: 90 }] },
      { role: 'quote', at: 41, v: 5200000, tau: 1.4, handle: 'demo_framecount', name: 'count the frames', kind: 'person', followers: 9400, text: 'One take, sure. Now watch the clock on the wall. That second hand does a full lap in 31 seconds.' },
      { role: 'voice', at: 88, v: 1100000, tau: 2, handle: 'demo_actuator', name: 'ships hardware', kind: 'person', followers: 52000, text: 'Everyone speeds up demos. Label it, yes. But the grasp on that third shirt is the hard part and it is real.' },
    ],
  },
  {
    slug: 'kick-off-both-uprights', desks: ['sports'], beat: 'college-football', standing: 'established', start: 3.1,
    title: 'A 61 yard kick hits both uprights and the crossbar before going in',
    dek: 'It won a college game as time ran out, and the sideline angle has more views than the broadcast one.',
    what: ['With two seconds left a kicker tried from 61 yards. The ball struck the left upright, the right upright and the crossbar, and dropped through. Officials signalled good after a short conference.'],
    why: 'It looks impossible on the first watch and people are replaying it to count the bounces.',
    posts: [
      { role: 'origin', at: 0, v: 8700000, tau: 1.2, handle: 'demo_sideline', name: 'Sideline Cam', kind: 'creator', followers: 310000, text: 'LEFT. RIGHT. BAR. GOOD. I have never seen anything like this', media: [{ type: 'video', description: 'Field level view behind the goalposts; a football bounces off both posts and the crossbar and falls through', duration_s: 14 }] },
      { role: 'reply', at: 12, v: 1900000, tau: 1, handle: 'demo_physicsta', name: 'your physics TA', kind: 'person', followers: 2300, text: 'I will be using this on the midterm and none of you are getting it right' },
    ],
  },
  {
    slug: 'cold-plunge-vagus', desks: ['medicine', 'life'], beat: 'wellness', standing: 'false', start: 11,
    title: 'No, a cold plunge does not "reset" your vagus nerve',
    dek: 'A thread with a confident diagram has six million views. The physiology in it is not real.',
    what: ['A wellness account posted a thread claiming that thirty seconds of cold water "reboots the vagus nerve" and "clears stored cortisol". It includes a diagram of a nerve with an on and off switch.', 'Cold water on the face does briefly slow the heart, which is a known reflex. Nothing is reset, and cortisol is not stored.'],
    why: 'It promises a large benefit for thirty seconds of effort, and the diagram looks like something from a textbook.',
    worlds: [
      { name: 'Wellness accounts', sees: 'A simple daily habit backed by "nervous system science", shared with personal stories of feeling calmer afterwards.', post: 0 },
      { name: 'Clinicians', sees: 'A real reflex stretched into an invented mechanism, with a diagram that would fail a first year exam.', post: 1 },
    ],
    common: 'People who say they feel more alert after cold water are describing something real. The explanation attached to it is made up: there is no reset, and no stored cortisol to clear. Sudden cold immersion can be dangerous for people with heart conditions.',
    posts: [
      { role: 'origin', at: 0, v: 6200000, tau: 4, handle: 'demo_glowstate', name: 'Glow State', kind: 'creator', followers: 480000, text: '30 seconds of cold water REBOOTS your vagus nerve and flushes stored cortisol. Doctors will not tell you this. Thread', media: [{ type: 'photo', description: 'A drawn diagram of a nerve running from head to abdomen with a switch labelled ON and OFF', duration_s: null }] },
      { role: 'quote', at: 130, v: 2400000, tau: 3, handle: 'demo_autonomic', name: 'an actual neurologist', kind: 'person', followers: 44000, text: 'The diving reflex is real and it is neat. Nothing reboots. Cortisol is not stored anywhere. Please do not jump into ice water if you have a heart condition.' },
    ],
  },
  {
    slug: 'title-screen-typo', desks: ['gaming'], beat: 'studios', standing: 'established', start: 16,
    title: 'A studio delays its game by a day to fix a typo on the title screen',
    dek: 'Players found the misspelling in the launch trailer. The studio moved the release rather than patch it later.',
    what: ['A launch trailer showed the title screen with the word "adventure" spelled wrong. The studio announced a one day delay and posted the corrected screen.'],
    why: 'Delays usually come with an apology; this one came with a joke at the studio\'s own expense.',
    posts: [
      { role: 'origin', at: 0, v: 2700000, tau: 6, handle: 'demo_emberforge', name: 'Emberforge Games', kind: 'brand', followers: 150000, text: 'We are delaying launch by 24 hours. We spelled "adventure" wrong on the title screen and we cannot live like this.' },
    ],
  },
  {
    slug: 'smart-lock-outage', desks: ['tech', 'business'], beat: 'security', standing: 'developing', start: 2.2,
    title: 'A login outage is locking people out of their own front doors',
    dek: 'A smart lock maker\'s sign-in service went down an hour ago. Owners without a physical key are posting from their porches.',
    what: ['A smart lock company\'s account service stopped answering a little over an hour ago. Locks that need the app to open are not responding. The company says it is investigating and that keypad codes still work.'],
    why: 'Every post is a photo of someone standing outside their own house, which is hard to scroll past.',
    next: 'The company\'s status page promises an update on the hour.',
    posts: [
      { role: 'origin', at: 0, v: 1900000, tau: 0.9, handle: 'demo_porchlife', name: 'dev on a porch', kind: 'person', followers: 12000, text: 'I am an engineer. I chose this. I am locked out of my house because a login server is down. There is a lesson here and I refuse to learn it', media: [{ type: 'photo', description: 'A front door with an electronic lock showing a red light, photographed from a porch chair', duration_s: null }] },
      { role: 'official', at: 22, v: 700000, tau: 1, handle: 'demo_latchly', name: 'Latchly Support', kind: 'brand', followers: 31000, text: 'We are investigating sign-in errors. Keypad codes and physical keys continue to work. Updates on our status page.' },
    ],
  },
  {
    slug: 'stadium-wrong-lyric', desks: ['music'], beat: 'live', standing: 'established', start: 18.5,
    title: 'Sixty thousand people sing the wrong lyric and the singer gives up',
    dek: 'A fan video from the upper deck caught the moment the crowd overruled the song.',
    what: ['At a stadium show the crowd sang a well known chorus with a wrong word, loudly enough that the singer stopped, laughed, and sang it their way for the rest of the night.'],
    why: 'It is a happy clip, and the wrong lyric is arguably better.',
    posts: [
      { role: 'origin', at: 0, v: 5400000, tau: 5.5, handle: 'demo_upperdeck', name: 'row 38', kind: 'person', followers: 900, text: 'the entire stadium decided the lyric was wrong and she just went with it', media: [{ type: 'video', description: 'Wide view of a stadium concert from a high seat; the crowd sings and the performer stops and laughs', duration_s: 52 }] },
    ],
  },
  {
    slug: 'paid-wedding-seat', desks: ['life', 'internet'], beat: 'etiquette', standing: 'established', start: 7.8,
    title: 'A wedding invitation asks guests to pay for their own seat',
    dek: 'The invitation lists three ticket tiers. The names have been cropped out; the argument has not.',
    what: ['Someone posted a wedding invitation, with names removed, that asks guests to choose between a standard seat, a seat with dinner, and a seat near the front. Prices are printed beside each.'],
    why: 'Everyone has been to a wedding, so everyone has a position.',
    private: true,
    posts: [
      { role: 'origin', at: 0, v: 7300000, tau: 2.8, handle: 'demo_plusone', name: 'not attending', kind: 'person', followers: 26000, text: 'I have been invited to a wedding with TIERS. Tier 3 gets "ceremony view (partial)".', media: [{ type: 'photo', description: 'A printed invitation with names blacked out and a table of three priced options', duration_s: null }] },
      { role: 'reply', at: 31, v: 2200000, tau: 2, handle: 'demo_etiquette', name: 'Aunt Protocol', kind: 'creator', followers: 190000, text: 'A wedding is hosted. If there is a price list it is an event, and you may decline an event without a gift.' },
    ],
  },
  {
    slug: 'telescope-face', desks: ['science'], beat: 'astronomy', standing: 'established', start: 20,
    title: 'A crater that looks like a face, and why it stops looking like one at noon',
    dek: 'A new orbital image has people seeing a smile. Astronomers posted the same crater under a higher sun.',
    what: ['A newly released image of a crater shows two pits and a curved ridge that read as a face. Researchers replied with a second image of the same ground taken with the sun overhead, in which the face is gone.'],
    why: 'The before and after pair is satisfying, and it arrives with its own explanation.',
    posts: [
      { role: 'origin', at: 0, v: 3100000, tau: 7, handle: 'demo_orbitdaily', name: 'Orbit Daily', kind: 'aggregator', followers: 540000, text: 'it is smiling at us', media: [{ type: 'photo', description: 'A grey crater seen from above with two dark pits and a curved ridge below them', duration_s: null }] },
      { role: 'quote', at: 150, v: 1200000, tau: 5, handle: 'demo_shadowlen', name: 'planetary geologist', kind: 'person', followers: 31000, text: 'Same crater, sun 60 degrees higher. The "eyes" are shadows in two small pits. Still a very good crater.', media: [{ type: 'photo', description: 'The same crater evenly lit; no face is visible', duration_s: null }] },
    ],
  },
  {
    slug: 'typo-coin', desks: ['markets'], standing: 'developing', start: 5.0,
    title: 'A token named after a typo gains and loses most of its value in three hours',
    dek: 'It started as a joke about a misspelled announcement. The chart is now the joke.',
    what: ['After an exchange misspelled a word in an announcement, someone launched a token using the misspelling as its name. It rose quickly, and has since fallen by about four fifths from its peak.'],
    why: 'The people who bought early are posting screenshots, and so are the people who bought late.',
    posts: [
      { role: 'origin', at: 0, v: 1600000, tau: 1.1, handle: 'demo_ctdegen', name: 'liquidity enjoyer', kind: 'person', followers: 73000, text: 'someone launched a coin called the typo and it is up 40x. we are so back', media: [{ type: 'photo', description: 'A price chart rising steeply on a dark background', duration_s: null }] },
      { role: 'quote', at: 170, v: 1400000, tau: 1.5, handle: 'demo_exitliq', name: 'bought the top', kind: 'person', followers: 5200, text: 'update: it is so over', media: [{ type: 'photo', description: 'The same chart, now showing a steep fall', duration_s: null }] },
    ],
  },
  {
    slug: 'rhyming-ruling', desks: ['justice', 'ideas'], beat: 'lawsuits', standing: 'established', start: 14.5,
    title: 'A judge rules on a parking dispute partly in rhyme',
    dek: 'Four pages of the eleven page order are in couplets. The ruling itself is ordinary.',
    what: ['A small claims order in a dispute over a shared driveway includes four pages written in rhyming couplets. The outcome, a split of towing costs, is routine.'],
    why: 'Lawyers are sharing it with their favourite lines, and everyone else is sharing it because it is short.',
    posts: [
      { role: 'origin', at: 0, v: 1500000, tau: 6, handle: 'demo_docketnerd', name: 'reads the docket', kind: 'person', followers: 58000, text: '"The driveway is shared, as the deed makes plain / and neither may block it for personal gain." Small claims court is undefeated.', media: [{ type: 'photo', description: 'A page of a court order with indented rhyming lines', duration_s: null }] },
    ],
  },
  {
    slug: 'hail-doorbell', desks: ['disaster'], beat: 'storms', standing: 'developing', start: 1.4,
    title: 'Doorbell cameras catch hail the size of golf balls',
    dek: 'A fast moving storm line is producing large hail. The clips are arriving faster than the warnings.',
    what: ['A line of storms is dropping large hail across several towns. Residents are posting doorbell and dash camera footage. Forecasters have issued warnings for the counties ahead of the line.'],
    why: 'The footage is loud and close, and it is still happening.',
    next: 'The storm line reaches the next county within the hour.',
    posts: [
      { role: 'origin', at: 0, v: 950000, tau: 0.8, handle: 'demo_doorcam', name: 'our front step', kind: 'person', followers: 300, text: 'RIP to my car', media: [{ type: 'video', description: 'Doorbell camera view of a driveway as large hailstones strike a parked car', duration_s: 21 }] },
      { role: 'official', at: 9, v: 410000, tau: 0.7, handle: 'demo_wxoffice', name: 'County Weather Office', kind: 'official', followers: 88000, text: 'Hail up to 1.75 inches reported with this line. If you are in its path, move indoors and away from windows.' },
    ],
  },
  {
    slug: 'four-hour-logo', desks: ['business', 'internet'], beat: 'brands', standing: 'established', start: 22,
    title: 'A cereal brand\'s new logo lasts four hours',
    dek: 'The redesign dropped the mascot. By lunch the old box was back.',
    what: ['A cereal maker unveiled a simplified logo without its cartoon mascot. After a morning of complaints and jokes, the company posted the old box with the caption "we heard you".'],
    why: 'People enjoy winning an argument with a company, especially quickly.',
    posts: [
      { role: 'origin', at: 0, v: 4200000, tau: 4, handle: 'demo_crunchco', name: 'Crunch & Co.', kind: 'brand', followers: 220000, text: 'A fresh look for a new era.', media: [{ type: 'photo', description: 'A cereal box with a plain wordmark and no mascot', duration_s: null }] },
      { role: 'official', at: 240, v: 3800000, tau: 3, handle: 'demo_crunchco', name: 'Crunch & Co.', kind: 'brand', followers: 220000, text: 'we heard you', media: [{ type: 'photo', description: 'The earlier cereal box with a cartoon mascot', duration_s: null }] },
    ],
  },
  {
    slug: 'ferry-strike-reply', desks: ['world'], beat: 'europe', standing: 'developing', start: 8.6,
    title: 'A ferry strike strands thousands, and one port authority reply makes it worse',
    dek: 'Crews walked off over rosters. An official account told a stranded traveller to "consider it a longer holiday".',
    what: ['Ferry crews at a busy port began a strike over scheduling, cancelling sailings for the day. A traveller asking for help was told by the port authority\'s account to "consider it a longer holiday". The reply was deleted after forty minutes.'],
    why: 'The strike is the news; the reply is why people far from the port are sharing it.',
    posts: [
      { role: 'origin', at: 0, v: 2600000, tau: 2.6, handle: 'demo_stuckport', name: 'at the terminal', kind: 'person', followers: 1700, text: 'Asked the port when we can leave. Their actual reply:', media: [{ type: 'photo', description: 'Screenshot of a reply from an official account that reads "consider it a longer holiday"', duration_s: null }] },
      { role: 'official', at: 96, v: 800000, tau: 2, handle: 'demo_portauth', name: 'Harbour Authority', kind: 'official', followers: 41000, text: 'An earlier reply from this account did not reflect how seriously we take today\'s disruption. We apologise. Rebooking is free.' },
    ],
  },
];
