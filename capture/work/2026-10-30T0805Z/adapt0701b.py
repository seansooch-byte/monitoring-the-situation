s=open('build_capture.py').read()
a=s.index("DESK_OVERRIDE_RUN.update({'2115878416423784939':'medicine'"); b=s.index("\n",a)
add = """
DESK_OVERRIDE_RUN.update({'2115988739260395803':'sports','2115194826371272979':'sports','2115180887335633049':'sports'})  # 0701Z desk fixes: MySportsUpdate Christian Watson cleared post and scrapytweets Odegaard post are sports; xghana_ 'Sad story' video is the origin quoted by its own Nevada soccer-academy post (sports)
skip_nsfw |= {'2115731138249412793','2115902565376241837'}  # 0701Z: graphic: RyanAFournier footage of a Trump supporter stabbed outside the Ohio rally (the Chillicothe stabbing video left out since 1707Z); Localman254_ video of a mob beating a phone snatcher to death in Mombasa"""
s=s[:b]+add+s[b:]
open('build_capture.py','w').write(s); print('ok')
