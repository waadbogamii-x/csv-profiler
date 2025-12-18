









class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique


    @property
    def missing_pct(self) -> float:
        if self.total == 0:
            return 0
        return (self.missing / self.total) * 100


    def to_dict(self) -> dict:
      return {
            "name": self.name,
            "type": self.inferred_type,
            "total": self.total,
            "missing": self.missing,
            "unique": self.unique,
            "missing_pct": self.missing_pct,
        }
     


test = ColumnProfile("waad", "name", 10, 2, 3)
print(test.missing_pct)
print(test.to_dict())