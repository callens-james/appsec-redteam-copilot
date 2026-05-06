from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path
import json

from watchers.change_queue import list_items
from agents.triage_rules import triage_file
from evaluators.report_store import save_report, list_reports
from rag.git_diff import find_repo_root, changed_files

app = FastAPI(title="AppSec Red Team Copilot", version="0.1.1")
CFG = Path(__file__).resolve().parents[1] / 'watchers' / 'watch_config.json'

class AnalyzeRequest(BaseModel):
    project: str
    files: list[str] = []

@app.get('/health')
def health():
    return {"ok": True, "service": "appsec-redteam-copilot", "time": datetime.utcnow().isoformat()}

@app.get('/changes')
def changes(limit:int=Query(100, ge=1, le=1000)):
    return {"items": list_items(limit)}

@app.post('/analyze-diff')
def analyze_diff(req: AnalyzeRequest):
    reports=[triage_file(f) for f in req.files]
    overall='low'
    if any(r['risk']=='high' for r in reports):
        overall='high'
    elif any(r['risk']=='medium' for r in reports):
        overall='medium'
    return {
        "project": req.project,
        "summary": f"Analyzed {len(req.files)} files",
        "risk": overall,
        "findings": reports,
        "next": ["connect git diff extractor", "connect RAG evidence"]
    }
# test Wed May  6 02:46:54 PM UTC 2026
# test Wed May  6 02:50:04 PM UTC 2026


@app.post('/analyze-recent')
def analyze_recent(limit:int=Query(25, ge=1, le=500)):
    items = list_items(limit)
    files = []
    seen = set()
    for it in items:
        p = it.get('path')
        if p and p not in seen:
            seen.add(p)
            files.append(p)
    reports=[triage_file(f) for f in files]
    overall='low'
    if any(r['risk']=='high' for r in reports):
        overall='high'
    elif any(r['risk']=='medium' for r in reports):
        overall='medium'
    payload = {
        'project': 'workspace-recent',
        'summary': f'Analyzed {len(files)} recent changed files',
        'risk': overall,
        'findings': reports,
        'sourceCount': len(items)
    }
    saved = save_report(payload)
    return saved

@app.get('/reports')
def reports(limit:int=Query(50, ge=1, le=1000)):
    return {'items': list_reports(limit)}
# test Wed May  6 06:23:06 PM UTC 2026


@app.post('/analyze-repo-diff')
def analyze_repo_diff(path:str):
    root = find_repo_root(path)
    if not root:
        return {'error':'no git repo root found', 'path': path}
    files = changed_files(root)
    reports=[triage_file(f) for f in files]
    overall='low'
    if any(r.get('risk')=='high' for r in reports):
        overall='high'
    elif any(r.get('risk')=='medium' for r in reports):
        overall='medium'
    payload = {
      'project': str(root),
      'summary': f'Analyzed git diff files: {len(files)}',
      'risk': overall,
      'findings': reports,
      'source':'git-diff'
    }
    return save_report(payload)
