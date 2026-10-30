s=open('build_capture.py').read()
def rep(a,b):
    global s
    c=s.count(a)
    if c<1:
        raise SystemExit('missing: '+repr(a[:140]))
    s=s.replace(a,b)

rep('"""Build capture/2026/10/17/2201Z.json','"""Build capture/2026/10/17/2308Z.json')
rep("capture/work/2026-10-17T2201Z'","capture/work/2026-10-17T2308Z'")
rep("RUN_ID = '2026-10-17T2201Z'","RUN_ID = '2026-10-17T2308Z'")
rep("STARTED = '2026-10-17T22:01:00Z'","STARTED = '2026-10-17T23:08:00Z'")
rep("OBS_AT = '2026-10-17T22:02:00Z'","OBS_AT = '2026-10-17T23:09:00Z'")
rep("READS_BEFORE = 400\nREADS_AFTER = 368","READS_BEFORE = 368\nREADS_AFTER = 340")
rep("datetime(2026,10,17,22,6,tzinfo","datetime(2026,10,17,23,12,tzinfo")

old_files = """    'watch0': 'watch0.txt', 'watch1': 'watch1.txt',
    'quote_and': 'quote_and.txt', 'quote_my': 'quote_my.txt', 'quote_it': 'quote_it.txt',
    'repost_that': 'repost_that.txt',
    'trend_auburn': 'trend_auburn.txt', 'trend_underwood': 'trend_underwood.txt', 'trend_rhyne': 'trend_rhyne.txt', 'trend_carr': 'trend_carr.txt',
    'sensor_news': 'sensor_news.txt', 'sensor_money': 'sensor_money.txt', 'sensor_science': 'sensor_science.txt',"""
new_files = """    'watch0': 'watch0.txt', 'watch1': 'watch1.txt',
    'quote_just': 'quote_just.txt', 'quote_what': 'quote_what.txt', 'quote_the': 'quote_the.txt',
    'repost_this': 'repost_this.txt',
    'trend_georgia': 'trend_georgia.txt', 'trend_tennessee': 'trend_tennessee.txt', 'trend_rocco': 'trend_rocco.txt', 'trend_michigan': 'trend_michigan.txt', 'trend_gunner': 'trend_gunner.txt',
    'sensor_culture': 'sensor_culture.txt', 'sensor_sports': 'sensor_sports.txt', 'sensor_online': 'sensor_online.txt',"""
rep(old_files, new_files)

rep("DUE = ['politics','entertainment','sports','internet','world','justice','markets','ai','tech','medicine','defense','disaster','business']",
    "DUE = ['politics','entertainment','sports','internet','music','gaming','offbeat']")

old_src = """    ('quote_and','quote'),('quote_my','quote'),('quote_it','quote'),('repost_that','repost'),
    ('trend_auburn','trend.Auburn'),('trend_underwood','trend.Bryce Underwood'),('trend_rhyne','trend.Rhyne'),('trend_carr','trend.Tommy Carr'),
    ('sensor_news','sensors.news'),('sensor_money','sensors.money'),('sensor_science','sensors.science'),"""
new_src = """    ('quote_just','quote'),('quote_what','quote'),('quote_the','quote'),('repost_this','repost'),
    ('trend_georgia','trend.Georgia'),('trend_tennessee','trend.Tennessee'),('trend_rocco','trend.Rocco Becht'),('trend_michigan','trend.Michigan'),('trend_gunner','trend.Gunner'),
    ('sensor_culture','sensors.culture'),('sensor_sports','sensors.sports'),('sensor_online','sensors.online'),"""
rep(old_src, new_src)

rep("        if str(_x) in ('trend.Auburn','trend.Gunner','trend.Bryce Underwood','trend.Tommy Carr','trend.Michigan','trend.Rhyne','trend.#WNBAfinals','trend.Gabby Williams'): return 'sports'",
    "        if str(_x) in ('trend.Auburn','trend.Gunner','trend.Bryce Underwood','trend.Tommy Carr','trend.Michigan','trend.Rhyne','trend.#WNBAfinals','trend.Gabby Williams','trend.Georgia','trend.Tennessee','trend.Rocco Becht','trend.WAR DAMN EAGLE','trend.War Eagle'): return 'sports'")

rep("('Arch Manning','Arch'),('Nick Marsh','Marsh'),('Auburn','Gunner'),('Bryce Underwood','Tommy Carr'),('Tommy Carr','Bryce Underwood'),('Bryce Underwood','Michigan'),('Tommy Carr','Michigan'),('Rhyne','#WNBAfinals')]:",
    "('Arch Manning','Arch'),('Nick Marsh','Marsh'),('Auburn','Gunner'),('Auburn','Georgia'),('Georgia','Gunner'),('Georgia','WAR DAMN EAGLE'),('Georgia','War Eagle'),('Bryce Underwood','Tommy Carr'),('Tommy Carr','Bryce Underwood'),('Bryce Underwood','Michigan'),('Tommy Carr','Michigan'),('Rhyne','#WNBAfinals'),('Rocco Becht','Tennessee')]:")

rep("""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('news','money','science')}
SENSOR_READ = {'news','money','science'}""",
"""SENSOR_Q = {g: open(f'{W}/sensor_{g}_q.txt').read().strip() for g in ('culture','sports','online')}
SENSOR_READ = {'culture','sports','online'}""")

rep("(22Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 2 reads;",
    "(23Z is not a fourth hour, so no slow tier); {len(watch_ids)} unique ids, under the 400 cap, none left out, {len(watch_returned)} returned, {len(watch_unavailable)} unavailable, 2 reads;")

import re
m=re.search(r"trend names Auburn.*?Macron had posts attached in 2101Z\)", s)
if not m:
    raise SystemExit('trend names block not found')
TR=('trend names Georgia, Tennessee, "Rocco Becht", Michigan, Gunner (each "<name> lang:en is:retweet", newest first, 25 each, names quoted when they have a space; '
    'the top-ten US names with no posts attached in 2201Z that are new or newly prominent; Georgia and Gunner are one event with Auburn (Auburn v Georgia), both searched; '
    'Tennessee and Rocco Becht are one event (Iowa State football, Rocco Becht); Michigan is one event with Bryce Underwood and Tommy Carr (Michigan benching), searched as a fresh top-ten name; '
    'Auburn, Tommy Carr, Bryce Underwood and Rhyne had posts attached in 2201Z; Arch, Sark, Indiana, Ohio State and Macron were searched in earlier runs today, not searched again)')
s=s.replace(m.group(0), TR)

rep("quote/repost words and/my/it + that; sensors news/money/science; desks politics/entertainment/sports/internet/world/justice/markets/ai/tech/medicine/defense/disaster/business;",
    "quote/repost words just/what/the + this; sensors culture/sports/online; desks politics/entertainment/sports/internet/music/gaming/offbeat;")

rep("""'3 quote pages + 1 repost page, common words "and", "my", "it" and "that": ("and" lang:en is:quote -is:retweet), (my lang:en is:quote -is:retweet), (it lang:en is:quote -is:retweet), (that lang:en is:retweet), newest first, 25 each'""",
"""'3 quote pages + 1 repost page, common words "just", "what", "the" and "this": ("just" lang:en is:quote -is:retweet), ("what" lang:en is:quote -is:retweet), ("the" lang:en is:quote -is:retweet), ("this" lang:en is:retweet), newest first, 25 each'""")

rep("""        _last = '2026-10-17T2101Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: news/money/science this hour); last read in {_last}',6,'skipped','rotation: culture/sports/online read in 2101Z, next run',[]))""",
"""        _last = '2026-10-17T2201Z'
        sweeps.append(sweep(f'sensors.{g}','discovery',None,f'not read this run (rotation: culture/sports/online this hour); last read in {_last}',6,'skipped','rotation: news/money/science read in 2201Z, next run',[]))""")

rep("""        if d in ('music','gaming','offbeat'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2101Z, due 23:01Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""",
"""        if d in ('world','justice','markets','ai','tech','medicine'):
            reason = 'not due this run (two-hour desk, last ok 2026-10-17T2201Z, due 00:03Z)'
        elif d in ('defense','disaster','business'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2201Z, due 02:07Z)'
        elif d in ('science','ideas','life'):
            reason = 'not due this run (four-hour desk, last ok 2026-10-17T2101Z, due 01:01Z)'""")

rep("""f'Daytime run at 6:01 PM ET (22:01 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2101Z run ended at 400, so nothing else read in between). '""",
"""f'Daytime run at 7:08 PM ET (23:08 UTC Oct 17; 12:00-05:00 UTC band, up to 42 reads): {READS_USED} X reads ({READS_BEFORE} to {READS_AFTER} left today; the 2201Z run ended at 368, so nothing else read in between). '""")

rep("22Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 2 reads","23Z is not a fourth hour, so no slow tier; under the 400 cap, none left out; 2 reads")
rep("(4 reads); quote/repost words and/my/it + that (3+1); '","(5 reads); quote/repost words just/what/the + this (3+1); '")

m2=re.search(r"f'sensors news/money/science; 13 desk reads:.*?", s)
# find the full f-string - ends at next newline that closes the string awkwardly; look for specific
idx=s.find("f'sensors news/money/science; 13 desk reads:")
if idx<0:
    raise SystemExit('desk sensors reason not found')
# find end of this string literal (ends with '; ')
end=s.find("';", idx+2)
old=s[idx:end+1]
new=("f'sensors culture/sports/online; 7 desk reads: the hourly desks politics, entertainment, sports, internet "
     "and the two-hour desks music, gaming, offbeat (last ok 2101Z, due 23:01Z); world, justice, markets, ai, tech, medicine "
     "next due 00:03Z, defense, disaster, business 02:07Z, science, ideas, life 01:01Z; '")
s=s.replace(old, new)
print('replaced desk reason', old[:80], '...')

rep("culture/sports/online sensors next rotation","news/money/science sensors next rotation")
rep("out_path = f'{REPO}/capture/2026/10/17/2201Z.json'","out_path = f'{REPO}/capture/2026/10/17/2308Z.json'")

open('build_capture.py','w').write(s)
print('ok', len(s))
