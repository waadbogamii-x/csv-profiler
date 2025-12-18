def render_markdown(report: dict) -> str:
    lines = []
    lines.append("# CSV Profile Report\n")

    lines.append("## Columns\n")
    lines.append("| Column |")
    lines.append("|--------|")

    for col in report["columns"]:
        lines.append(f"| {col} |")

    return "\n".join(lines)
