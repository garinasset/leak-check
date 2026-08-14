from typing import Iterable, Optional

from lib.common import iter_nonempty


def clean_str_set(values: Iterable[Optional[str]]) -> list[str]:
    return list({
        str(v).strip()
        for v in iter_nonempty(values)
    })


def clean_int_set(values: Iterable) -> list[int]:
    result = set()
    for v in iter_nonempty(values):
        try:
            result.add(int(v))
        except (TypeError, ValueError):
            continue
    return list(result)


def clean_id_set(values: Iterable) -> list[str]:
    return list({
        str(v)
        for v in iter_nonempty(values)
    })