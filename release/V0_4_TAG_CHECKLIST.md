# v0.4 Tag Checklist

Purpose: capture the evidence needed before treating the v0.4 safety milestone as release/portfolio-ready.

Do not mark an item complete unless the result was actually observed and recorded.

## Validation Checklist

- [x] `bash scripts/safety_regression_check.sh` passes
  - Evidence/date: 2026-05-12, pass=11 fail=0
  - Notes: Updated regression script to match current capability-token safety model.

- [x] `/safety/audit/verify` returns `ok=true`
  - Evidence/date: 2026-05-12
  - Notes: `ok=true`, checked 15 audit entries, errors empty.

- [x] `/safety/metrics` shows `brokerCoverageRate` + `coverageStatus`
  - Evidence/date: 2026-05-12
  - Notes: `brokerCoverageRate=1.0`, `coverageStatus=SAFE`.

- [x] Broker-only mode confirmed ON
  - Evidence/date: 2026-05-12
  - Notes: `/safety/mode` returned `brokerOnlyMode=true`.

- [x] Master Safe Mode confirmed ON
  - Evidence/date: 2026-05-12
  - Notes: `/safety/mode` returned `agentSafeMode=true` and `commandGuard=true`.

- [ ] Emergency override tested: enable / auto-expire / disable + audit events
  - Evidence/date:
  - Notes: Not exercised in this local validation pass.

- [x] Threat/guarantee docs reviewed
  - Evidence/date: 2026-05-12
  - Notes: Existing guarantee/limit docs retained; runtime artifact and validation evidence docs added.

- [x] Demo script walkthrough completed
  - Evidence/date: 2026-05-12
  - Notes: Dashboard health verified; pre-change report endpoint and PR-comment endpoint validated against current repo state.

## Evidence Bundle

Current evidence bundle:

- `release/proof-pack/validation-evidence-2026-05-12.md`
- `release/proof-pack/latest_eval.json`
- `release/proof-pack/latest_prechange_report.json`
- `release/proof-pack/latest_report.json`
- `release/proof-pack/SECURITY_REPORT.md`

## Runtime Artifact Reminder

Before tagging or promotion review, check runtime artifact hygiene:

- `backend/watchers/change_queue.jsonl`
- `backend/data/advisories_cache.json`
- `backend/data/eval_reports/`
- `backend/data/eval_tmp/`
- `__pycache__/`
- `*.pyc`

See: `docs/RUNTIME_ARTIFACTS.md`

## Current Status

Local validation is mostly complete for the v0.4 safety milestone.

Remaining item before a strict tag/release claim:

- emergency override lifecycle test
