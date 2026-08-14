from __future__ import annotations

from typing import Iterable, Iterator, TypeVar

T = TypeVar("T")


def iter_nonempty(values: Iterable[T]) -> Iterator[T]:
    for value in values:
        if value is None:
            continue
        if str(value).strip():
            yield value


def unique_nonempty_strings(values: Iterable[str | None]) -> set[str]:
    return {str(value).strip() for value in iter_nonempty(values)}
