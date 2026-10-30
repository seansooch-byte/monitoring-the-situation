import re
p='build_capture.py'; s=open(p).read()
def R(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
R("'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt',",
  "'watch0': 'watch0.txt', 'watch1': 'watch1.txt', 'watch2': 'watch2.txt', 'watch3': 'watch3.txt', 'watch4': 'watch4.txt', 'watch5': 'watch5.txt',")
R("for batch in ('watch0','watch1','watch2','watch3'):","for batch in ('watch0','watch1','watch2','watch3','watch4','watch5'):",2)
R("if d['id'] in ('politics','entertainment','sports','internet')]","]  # 0406Z top-up: every desk was due (hourly four plus the two- and four-hour desks)")
# watch method text
a=s.index("(this 0406Z run, the 04Z slot, is not a fourth hour;"); b=s.index("{len(watch_ids)} ids read,",a)
s=s[:a]+"(this 0406Z run, the 04Z slot, is not a fourth hour; the watch.json ids, then every pulse- and story-cited post, then the six-hour and still-gaining tiers: 540 ids, under the 800 cap of the 12:00 to 05:00 UTC band (contract/GRABBER.md as of e87da973); the first 400 were read in the first pass and the other 140, among them the 43 story-cited posts not on the pulse, in a top-up two reads later in the same run; none left out; the flat-post every-sixth-run rule was not yet applied, so no flat post was set aside); "+s[a+len(s[a:b]):]
s=s.replace("4 reads; fields created_at,public_metrics","6 reads; fields created_at,public_metrics",1)
# reason text
a=s.index("f'Night run (12:06 AM ET"); b=s.index("'\n",a)
s=s[:a]+"f'Night run (12:06 AM ET Oct 28 / 04:06 UTC Oct 28, the 04Z slot; 12:00-05:00 UTC band): {READS_USED} X reads this run ({READS_BEFORE} to {READS_AFTER} left today; 0305Z ended at 915), parallel batches of up to 15, no 429 refusals. The first pass followed the old pacing (about 20 reads, 400 re-reads, desks and volume cut); contract/GRABBER.md changed at e87da973 (800 re-reads by day, every due desk swept, five desks of volume, under 30 reads with desks due is a failure), so a top-up in the same run read the 15 due two- and four-hour desks, the other 140 re-read ids and five volume series, 25 more reads, two over the band\\'s 42. "+s[b:]
a=s.index("f'Watch {len(watch_returned)} of {len(watch_ids)}"); b=s.index("trends US (1 read;",a)
s=s[:a]+"f'Watch {len(watch_returned)} of {len(watch_ids)} ({len(watch_unavailable)} unavailable; 04Z is not a fourth hour: the watch.json ids, then every post cited on the pulse or in a published story, then the six-hour and still-gaining tiers; 540 ids, all read, none left out by the 800 cap; 6 reads); "+s[b:]
a=s.index("f'4 desk reads: hourly politics"); b=s.index("'\n",a)
s=s[:a]+"f'19 desk reads, every desk in desks.json order: the hourly politics, entertainment, sports and internet in the first pass, then world, defense, justice, disaster, markets, business, ai, tech, science, medicine, music, gaming, ideas, life and offbeat in the top-up (the two-hour desks last ok 2026-10-20T0400Z and the four-hour desks last ok 2026-10-20T0308Z, cut every run since for the old pacing); the top-up desk streams\\' reposted origins were screened from their includes, and their further references were not read (no screening read left in the band); volume.desks: five series this run (rotation slot 0 of 4: politics, world, defense, justice, disaster); '"+s[b:]
R("Not read: culture/sports/online sensors, worldwide trends, story clusters, volume, context.top, media descriptions (budget). ","Not read: culture/sports/online sensors, worldwide trends, story clusters, context.top, media descriptions (budget). ")
# volume
R("sweeps.append(sweep('context.top','context',None,",
"""VOL_DESKS = ['politics','world','defense','justice','disaster']
volume = []
for _d in VOL_DESKS:
    _vj = load_raw(f'volume_{_d}.txt')
    _pts = [{'start': x['start'].replace('.000Z','Z'), 'count': int(x['tweet_count'])} for x in (_vj.get('data') or [])]
    _pts.sort(key=lambda x: x['start'])
    assert sum(x['count'] for x in _pts) == _vj['meta']['total_tweet_count'], _d
    volume.append({'key': 'desk.'+_d, 'desk': _d, 'query': DESK_Q[_d].replace(' is:retweet -is:reply',''), 'granularity': 'hour', 'points': _pts})
sweeps.append(sweep('volume.desks','volume',None,'get_posts_counts_recent granularity hour, query "<standing query> lang:en", start_time 2026-10-21T05:00:00Z, end_time 2026-10-28T04:00:00Z, one read per desk for 5 desks this run (rotation slot 0 of 4 in capture/CAPABILITIES.md: politics, world, defense, justice, disaster); each series is the 167 full hours 2026-10-21T05:00Z to 2026-10-28T03:00Z, and each read was checked against meta.total_tweet_count',None,'ok',None,[]))
sweeps.append(sweep('context.top','context',None,""")
R("    'answers': ANSWERS,\n}","    'answers': ANSWERS,\n    'volume': volume,\n}")
open(p,'w').write(s); print('ok')
