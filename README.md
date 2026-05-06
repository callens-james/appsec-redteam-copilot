# AppSec Red Team Copilot

Background security copilot for coding workflows.

## MVP v1
- Watch selected project folders for code/config/dependency changes
- Build change-set/diff summary
- Run triage (rules + LLM-ready hook)
- Retrieve security evidence (RAG stub)
- Output PR-style security report
- Human-approval only

## Run
```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --port 3480
```

## Watcher config
Edit `backend/watchers/watch_config.json`.


## Step 9: Pre-commit Gate + Demo

### Install hooks
```bash
cd /home/james/openclaw-workspace/appsec-redteam-copilot
bash scripts/install_hooks.sh
```

### Pre-commit scan (manual)
```bash
python3 scripts/precommit_scan.py
```

### 2-minute demo
```bash
bash scripts/demo_run.sh
```

Behavior:
- `allow` => exit 0
- `warn` => exit 0 with warning
- `block` => exit 1 (commit blocked)
