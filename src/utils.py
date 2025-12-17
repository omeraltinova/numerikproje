"""Yardımcı fonksiyonlar."""

from __future__ import annotations

import contextlib
import time
from typing import Iterator

import numpy as np


def set_seed(seed: int | None = None) -> np.random.Generator:
    """Tek noktadan RNG üret."""
    return np.random.default_rng(seed)


@contextlib.contextmanager
def elapsed_timer() -> Iterator[callable]:
    """
    Kullanım:
    ```
    with elapsed_timer() as t:
        ...
    print(t())
    ```
    """
    start = time.perf_counter()

    def _elapsed():
        return time.perf_counter() - start

    yield _elapsed
