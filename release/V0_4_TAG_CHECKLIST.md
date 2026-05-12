# v0.4 Tag Checklist

Purpose: capture the evidence needed before treating the v0.4 safety milestone as release/portfolio-ready.

Do not mark an item complete unless the result was actually observed and recorded.

## Validation Checklist

- [ ] `bash scripts/safety_regression_check.sh` passes
  - Evidence/date:
  - Notes:

- [ ] `/safety/audit/verify` returns `ok=true`
  - Evidence/date:
  - Notes:

- [ ] `/safety/metrics` shows `brokerCoverageRate` + `coverageStatus`
  - Evidence/date:
  - Notes:

- [ ] Broker-only mode confirmed ON
  - Evidence/date:
  - Notes:

- [ ] Master Safe Mode confirmed ON
  - Evidence/date:
  - Notes:

- [ ] Emergency override tested: enable / auto-expire / disable + audit events
  - Evidence/date:
  - Notes:

- [ ] Threat/guarantee docs reviewed
  - Evidence/date:
  - Notes:

- [ ] Demo script walkthrough completed
  - Evidence/date:
  - Notes:

## Evidence Bundle

When complete, update or create a final proof bundle with:

- latest eval result summary
- latest pre-change report summary
- audit verification result
- safety metrics result
- screenshots or dashboard proof, if refreshed
- known limits / non-claims

Recommended destination:

`release/proof-pack/`

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

Not yet marked release-ready. This checklist is prepared for a focused validation pass.
