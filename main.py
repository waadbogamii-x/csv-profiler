from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import write_json, write_markdown


def main() -> None:
    # Read CSV
    rows = read_csv_rows("data/sample.csv")

    # Compute profile
    report = basic_profile(rows)

    # Write outputs
    write_json(report, "outputs/report.json")
    write_markdown(report, "outputs/report.md")

    print("Wrote outputs/report.json and outputs/report.md")


if __name__ == "__main__":
    main()
