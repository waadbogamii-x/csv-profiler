from __future__ import annotations

from csv import DictReader
from pathlib import Path

import csv

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    
    if not path.exists():
        raise FileNotFoundError("CSV file not found")
   # فتحت الملف وقرأت الصفوف واتحقق فيه صفوف فعلية او لا

    with path.open("r", encoding="utf-8") as file:
        #يقرأ
        r = csv.DictReader(file)
        #يحطها بليست
        rows = list(r)

    if len(rows) == 0:
        raise ValueError("CSV has no rows")

    return rows
