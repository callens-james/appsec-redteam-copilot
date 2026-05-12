# Changelog

## Unreleased
- Added portfolio readiness notes to clarify the strongest demo path, precise claims, current promotion gaps, and next validation step.
- Added a portfolio promotion package template for future evidence bundling.
- Expanded `.gitignore` coverage for Python/runtime cache artifacts.

## v0.3.0 - 2026-05-07
- Added pre-change diff hunk analysis endpoint with verdict gating (`allow`/`warn`/`block`)
- Added advisory ingestion cache refresh endpoint
- Added eval harness endpoint and persisted eval reports
- Added markdown security report renderer
- Added dashboard with report list/detail, eval, advisories refresh, and analysis actions
- Added Docker compose two-service runtime (API + watcher)
- Added systemd service-mode runbook and ops cheat sheet
