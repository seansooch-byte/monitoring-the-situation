import json,re
def load_x(p):
  raw=open(p).read()
  if 'X reads left' in raw: raw=raw[:raw.rfind('X reads left')]
  raw=re.sub(r'</?cursor_untrusted[^>]*>','',raw)
  return json.loads(raw[raw.find('{'):raw.rfind('}')+1])
def left(p):
  m=re.findall(r'(\d+) of 1000 today',open(p).read()); return m[-1] if m else None
