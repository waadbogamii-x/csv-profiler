from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import render_json, render_md


def main():
    rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)

    render_json(report)
    render_md(report)


if __name__ == "__main__":
    main()
