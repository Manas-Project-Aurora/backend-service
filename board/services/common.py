from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class Pagination:
    total_count: int
    taken_count: int
    skipped_count: int
