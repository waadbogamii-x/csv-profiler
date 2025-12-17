from pathlib import Path
import json
import typer
import time


from csv_profiler.io import read_csv_rows
from csv_profiler.profile import profile_rows
from csv_profiler.render import render_markdown

app = typer.Typer()



@app.command()
def profile(
    input_path: Path = typer.Argument(..., help="Path to input CSV"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Report name"),
    preview: bool = typer.Option(False, "--preview", help="Preview report"),
):
    start = time.perf_counter()

    rows = read_csv_rows(input_path)
    report = profile_rows(rows)

    end = time.perf_counter()
    report["timing_ms"] = int((end - start) * 1000)

    out_dir.mkdir(exist_ok=True)

    json_path = out_dir / f"{report_name}.json"
    json_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    markdown = render_markdown(report)
    md_path = out_dir / f"{report_name}.md"
    md_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    app()
