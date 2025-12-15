def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return list(rows[0].keys())


def basic_profile(rows: list[dict[str, str]]) -> dict:
    
    cols = get_columns(rows)

    report = {
        "summary": {
            "rows": len(rows),
            "columns": len(cols),
        },
        "columns": {},
    }

    for col in cols:
        values = column_values(rows, col)
        col_type = infer_type(values)

        if col_type == "number":
            stats = numeric_stats(values)
        else:
            stats = text_stats(values)

        report["columns"][col] = {
            "type": col_type,
            **stats
        }

    return report


# task 1

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




# task 2

def column_values(rows: list[dict[str, str]], col: str) -> list[str]:
    return [row.get(col, "") for row in rows]



# task 3 

def numeric_stats(values: list[str]) -> dict:
    """Compute stats for numeric column values (strings)."""

    
    #remove
    usable = [v for v in values if not is_missing(v)]

   # convert
    nums = [try_float(v) for v in usable]

  
    count = len(nums)
    missing = len(values) - count

    if count == 0:
        return {
            "count": 0,
            "missing": missing,
            "unique": 0,
            "min": None,
            "max": None,
            "mean": None,
        }  

    return {
        "count": count,
        "missing": missing,
        "unique": len(set(nums)),
        "min": min(nums),
        "max": max(nums),
        "mean": sum(nums) / count,
    }
 





# task 4

def text_stats(values: list[str], top_k: int = 5) -> dict:
    
    usable = [v for v in values if not is_missing(v)]

    count = len(usable)
    missing = len(values) - count
    unique = len(set(usable))

    
    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top = sorted(
        counts.items(),
        key=lambda kv: kv[1],
        reverse=True
    )[:top_k]

    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "top": top,
    }




# task 5

