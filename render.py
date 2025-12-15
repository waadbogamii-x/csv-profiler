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

    
    lines.append("# CSV Profiling Report\n")

    
    lines.append(f"- Rows: **{report.get('rows', 0)}**")
    lines.append(f"- Columns: **{len(report.get('columns', []))}**\n")

   
    lines.append("## Missing Values per Column\n")
    lines.append("| Column | Missing |")
    lines.append("|--------|---------|")

    for col, count in report.get("missing", {}).items():
        lines.append(f"| {col} | {count} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


    
def render_json(report: dict, out_dir: str = "outputs") -> None:
    Path(out_dir).mkdir(exist_ok=True)

    out_path = Path(out_dir) / "report.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)



def render_md(report: dict, out_dir: str = "outputs") -> None:
    Path(out_dir).mkdir(exist_ok=True)

    lines = []
    summary = report["summary"]

    # العنوان
    lines.append("# CSV Profiling Report\n")

    # الملخص
    lines.append("## Summary\n")
    lines.append(f"- Rows: **{summary['rows']}**\n")
    lines.append(f"- Columns: **{summary['columns']}**\n")

    # تفاصيل الأعمدة
    lines.append("\n## Columns\n")

    for col, info in report["columns"].items():
        lines.append(f"### {col}\n")
        lines.append(f"- Type: **{info['type']}**\n")

        if info["type"] == "number":
            lines.append(f"- Count: {info['count']}\n")
            lines.append(f"- Missing: {info['missing']}\n")
            lines.append(f"- Unique: {info['unique']}\n")
            lines.append(f"- Min: {info['min']}\n")
            lines.append(f"- Max: {info['max']}\n")
            lines.append(f"- Mean: {info['mean']}\n")
        else:
            lines.append(f"- Count: {info['count']}\n")
            lines.append(f"- Missing: {info['missing']}\n")
            lines.append(f"- Unique: {info['unique']}\n")
            lines.append("\nTop values:\n")

            for val, cnt in info["top"]:
                lines.append(f"- {val}: {cnt}\n")

        lines.append("\n")

    out_path = Path(out_dir) / "report.md"
    with out_path.open("w", encoding="utf-8") as f:
        f.writelines(lines)
