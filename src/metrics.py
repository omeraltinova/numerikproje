"""Metrik yardımcıları."""

from __future__ import annotations

import numpy as np
from numpy.linalg import cond


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def cond_xtx(X: np.ndarray) -> float:
    return float(cond(X.T @ X))
