#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT_DIR = ROOT / "report"
INDEX_PATH = ROOT / "REPORT_INDEX.md"


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


def build_markdown(report_files: list[Path]) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Report Index",
        "",
        f"Last updated: {timestamp}",
        "",
        "This index is generated automatically from the files in [`report/`](report).",
        "",
        f"Total files: {len(report_files)}",
        "",
        "| File | Type | Size | Modified |",
        "| --- | --- | ---: | --- |",
    ]

    if not report_files:
        lines.extend([
            "| No files found | — | — | — |",
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
        lines.append(
            f"| [{report_file.name}]({rel_path}) | {suffix.upper()} | {format_size(report_file.stat().st_size)} | {modified} |"
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
