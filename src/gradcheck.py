"""Gradient checking yardımcıları."""

from __future__ import annotations

from typing import Callable, Iterable, Tuple

import numpy as np


def J_mse(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> float:
    """MSE maliyet fonksiyonu."""
    n = X.shape[0]
    residual = X @ theta - y
    return 0.5 / n * np.dot(residual, residual)


def grad_mse_analytic(theta: np.ndarray, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Analitik gradyan: (1/n) X^T (X theta - y)."""
    n = X.shape[0]
    return (X.T @ (X @ theta - y)) / n


def grad_numeric_central(
    J: Callable[[np.ndarray], float],
    theta: np.ndarray,
    eps: float = 1e-4,
) -> np.ndarray:
    """
    Merkezi fark ile sayısal gradyan.
    J yalnızca theta argümanını alan kısmi uygulama olmalı.
    """
    grad = np.zeros_like(theta)
    for i in range(theta.size):
        e = np.zeros_like(theta)
        e[i] = 1.0
        grad[i] = (J(theta + eps * e) - J(theta - eps * e)) / (2 * eps)
    return grad


def epsilon_sweep(
    theta: np.ndarray,
    X: np.ndarray,
    y: np.ndarray,
    eps_list: Iterable[float],
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Epsilon taraması için relerr hesapla.

    Returns:
        eps_array, relerr_array
    """
    analytic = grad_mse_analytic(theta, X, y)
    eps_array = np.array(list(eps_list))
    relerrs = []
    for eps in eps_array:
        numeric = grad_numeric_central(lambda t: J_mse(t, X, y), theta, eps)
        denom = np.maximum(np.abs(analytic), np.abs(numeric))
        relerr = np.linalg.norm((analytic - numeric) / np.maximum(denom, 1e-15))
        relerrs.append(relerr)
    return eps_array, np.array(relerrs)
