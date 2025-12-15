from __future__ import annotations

import json
from pathlib import Path


def write_json(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []

    # Title
    lines.append("# CSV Profiling Report\n")

    # Summary
    lines.append(f"- Rows: **{report.get('rows', 0)}**")
    lines.append(f"- Columns: **{len(report.get('columns', []))}**\n")

    # Missing values table
    lines.append("## Missing Values per Column\n")
    lines.append("| Column | Missing |")
    lines.append("|--------|---------|")

    for col, count in report.get("missing", {}).items():
        lines.append(f"| {col} | {count} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
