
def render_markdown(report: dict) -> str:
    """
    Render report as a Markdown string
    """
    lines: list[str] = []


    lines.append("# CSV Profiling Report\n")



    lines.append("## Dataset Summary\n")
    lines.append(f"- Rows: **{report.get('rows', 0)}**")
    lines.append(f"- Columns: **{len(report.get('columns', []))}**\n")



    lines.append("## Columns\n")
    lines.append("| Column | Missing |")
    lines.append("|--------|---------|")

    for col in report.get("columns", []):
        missing = report.get("missing", {}).get(col, 0)
        lines.append(f"| {col} | {missing} |")

    return "\n".join(lines)
