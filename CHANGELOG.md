# Changelog

All notable changes to the published RRA report series and its
publishing pipeline are documented here, newest first. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2026-11-24]

### Changed — publishing

- **Reports are now published as styled, interactive HTML** served by
  GitHub Pages at
  <https://vialliw.github.io/Relative-Rotation-Analysis-Dashboard/report/report_index.html>.
  Each report page offers click-to-sort tables in every data section, a
  color-coded 2×2 quadrant census grid (green LEADING / red LAGGING),
  crossing/tilt rows colored by signal (green = bullish destination,
  red = bearish), and bolded signal keywords in the narrative.
- Markdown remains the internal authoring format upstream; the `.html`
  is rendered and committed at publish time. The roll-ups
  `weekly_summary.md` and `report_index.md` continue to publish as
  markdown and render via Jekyll.
- `REPORT_INDEX.md` and `report/report_index.md` now link to the
  rendered Pages URLs instead of repo-relative file paths.

### Removed

- Legacy `*_analysis_report.md` report files — superseded by their
  same-stem `.html` renderings (content unchanged).

### Added — infrastructure

- GitHub Pages enabled on `main` (root) — `.html` files serve verbatim,
  `.md` files render through Jekyll.
- Publish hardening upstream (`vialliw/stock-ingestion`): remote
  `.html`/`.md` parity protection keeps the last good published page
  alive when a local draft regresses below the enrichment gate;
  dated-report deletions now require an explicit `--prune` opt-in;
  deletions and holds are logged for audit.

## [2026-11-23]

### Changed — report format (v4)

- **Section 1 (Quadrant Census)** now opens with a traditional 2×2 RRG
  grid — titled quadrant cells, theme-grouped tickers (energy, metals,
  defensive, growth, …), heading-arrow suffixes per ticker.
- **Direction arrows everywhere** — `NE/SE/SW/NW` heading codes replaced
  by `↗/↘/↙/↖`, plus a new `FLAT` state for sub-threshold moves;
  `Hdg` column renamed to `Heading` and a `Persist` column added.
- **New standalone §5 Quadrant Crossings** — every boundary crossing
  classified `CONFIRMED` (≥ 1.0 pt past the crossed axis) or
  `PROVISIONAL_CROSSING` (⚠ whipsaw watch), with quadrant-persistence
  walk-back (`TEMPORARY`/`PENDING`/`CONFIRMED`) and probabilistic signal
  labels; sections renumbered 1–9.
- The `> Weekly read:` narrative now sits above the census grid, one
  sentence per line.

[Unreleased]: #
