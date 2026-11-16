#!/usr/bin/env python3
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT_DIR = ROOT / "report"
INDEX_PATH = ROOT / "REPORT_INDEX.md"
SUMMARY_NAME = "weekly_summary.md"

ISO_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")
COMPACT_DATE = re.compile(r"(?<!\d)(\d{4})(\d{2})(\d{2})(?!\d)")


def format_size(size_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size_bytes)
    unit_index = 0

    while value >= 1024 and unit_index < len(units) - 1:
        value /= 1024
        unit_index += 1

    if unit_index == 0:
        return f"{int(value)} {units[unit_index]}"
    return f"{value:.1f} {units[unit_index]}"


def load_weekly_summaries() -> dict[str, str]:
    """Parse report/weekly_summary.md into {YYYY-MM-DD: summary text}."""
    summary_path = REPORT_DIR / SUMMARY_NAME
    if not summary_path.exists():
        return {}

    summaries: dict[str, str] = {}
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= 2 and ISO_DATE.fullmatch(cells[0]):
            summaries[cells[0]] = " \\| ".join(cells[1:])
    return summaries


def report_date(filename: str) -> str | None:
    """Extract the report date from a filename (YYYY-MM-DD or YYYYMMDD)."""
    match = ISO_DATE.search(filename)
    if match:
        return match.group(1)
    match = COMPACT_DATE.search(filename)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def build_markdown(report_files: list[Path]) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    weekly = load_weekly_summaries()
    lines = [
        "# Report Index",
        "",
        f"Last updated: {timestamp}",
        "",
        "This index is generated automatically from the files in [`report/`](report).",
        f"The **Weekly summary** column is pulled from [`report/{SUMMARY_NAME}`](report/{SUMMARY_NAME}).",
        "",
        f"Total files: {len(report_files)}",
        "",
        "| File | Weekly summary | Type | Size | Modified |",
        "| --- | --- | --- | ---: | --- |",
    ]

    if not report_files:
        lines.extend([
            "| No files found | — | — | — | — |",
            "",
            "The `report/` folder is currently empty.",
        ])
        return "\n".join(lines) + "\n"

    for report_file in report_files:
        rel_path = report_file.relative_to(ROOT).as_posix()
        suffix = report_file.suffix.lower().lstrip(".") or "file"
        modified = datetime.fromtimestamp(report_file.stat().st_mtime, tz=timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )
        if report_file.name == SUMMARY_NAME:
            summary = "Roll-up of all weeks — start here"
        else:
            summary = weekly.get(report_date(report_file.name) or "", "—")
        lines.append(
            f"| [{report_file.name}]({rel_path}) | {summary} | {suffix.upper()} | {format_size(report_file.stat().st_size)} | {modified} |"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    if not REPORT_DIR.exists():
        raise FileNotFoundError(f"Report directory not found: {REPORT_DIR}")

    report_files = sorted(
        [path for path in REPORT_DIR.iterdir() if path.is_file()],
        key=lambda path: path.name.lower(),
    )
    INDEX_PATH.write_text(build_markdown(report_files), encoding="utf-8")


if __name__ == "__main__":
    main()
