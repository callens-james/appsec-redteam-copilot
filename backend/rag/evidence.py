import json
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / 'data' / 'cve_seed.json'

def _load():
    try:
        return json.loads(DB.read_text())
    except Exception:
        return []

def find_evidence(text:str, top_k:int=3):
    text_l=(text or '').lower()
    items=[]
    for row in _load():
        score=0
        for t in row.get('tags',[]):
            if t.lower() in text_l:
                score += 1
        if score>0:
            items.append((score,row))
    items.sort(key=lambda x:x[0], reverse=True)
    return [r for _,r in items[:top_k]]
