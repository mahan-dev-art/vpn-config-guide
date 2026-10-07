import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]/'content'
class ContentStore:
 def __init__(self):
  self.configs=json.loads((BASE/'configs/configs.json').read_text(encoding='utf-8'))['configs']; self.apps=[]
  for p in (BASE/'apps').glob('*.json'): self.apps.append(json.loads(p.read_text(encoding='utf-8')))
 def get_config(self,i): return next((x for x in self.configs if x['id']==i),None)
 def get_app(self,s): return next((x for x in self.apps if x['slug']==s),None)
 def get_tutorial(self,a,p):
  f=BASE/'tutorials'/a/p/'tutorial.json'; return json.loads(f.read_text(encoding='utf-8')) if f.exists() else None
