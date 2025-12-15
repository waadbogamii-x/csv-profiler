def basic_profile(rows: list[dict[str, str]]) -> dict:
    """Compute row count, column names, and missing values per column."""

    # Handle empty CSV
    if not rows:
        return {
            "rows": 0,
            "columns": [],
            "missing": {},
            "notes": ["Empty dataset"],
        }

    # Column names from first row
    columns = list(rows[0].keys())

    # Initialize missing counters
    missing = {col: 0 for col in columns}

    # Count missing values
    for row in rows:
        for col in columns:
            value = (row.get(col) or "").strip()
            if value == "":
                missing[col] += 1

    return {
        "rows": len(rows),
        "columns": columns,
        "missing": missing,
    }
