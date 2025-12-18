
def is_missing(value) -> bool:
    if value is None:
        return True
    text = str(value).strip().lower()
    return text in {"", "na", "n/a", "null", "none", "nan"}


def try_float(value):
    if is_missing(value):
        return None
    try:
        return float(value)
    except :
        return None


def infer_type(values: list[str]) -> str:
    The_number = False

    for v in values:
        if is_missing(v):
            continue
        if try_float(v) is None:
            return "text"
        The_number = True

    return "number" if The_number else "text"



def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {
            "rows": 0,
            "columns": [],
            "missing": {},
        }

    columns = list(rows[0].keys())
    missing = {col: 0 for col in columns}

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


def profile_rows(rows: list[dict[str, str]]) -> dict:
    """
    Wrapper function required by Task 5
    """
    return basic_profile(rows)