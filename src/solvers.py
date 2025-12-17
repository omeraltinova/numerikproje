"""Normal denklem çözücüleri ve gradient descent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

import numpy as np
from numpy.linalg import inv, solve
from scipy.linalg import lstsq


def normal_eq_inverse(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Kötü pratik: (X^T X)^-1 X^T y."""
    xtx = X.T @ X
    xty = X.T @ y
    return inv(xtx) @ xty


def normal_eq_solve(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Önerilen: (X^T X) theta = X^T y sistemini solve ile çöz."""
    xtx = X.T @ X
    xty = X.T @ y
    return solve(xtx, xty)


def least_squares_qr(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """QR/least squares çözümü (opsiyonel ama daha stabil)."""
    theta, *_ = lstsq(X, y)
    return theta


@dataclass
class GDRuntimeLog:
    losses: List[float]
    grad_norms: List[float]
    thetas: List[np.ndarray]


def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float = 1e-3,
    max_iter: int = 10_000,
    tol: float = 1e-6,
    log_every: int = 10,
    callback: Callable[[int, float, float], None] | None = None,
) -> Tuple[np.ndarray, Dict[str, List[float]]]:
    """
    Basit batch gradient descent. MSE türevini kullanır.

    Returns:
        theta, history dict (losses, grad_norms)
    """
    n, d = X.shape
    theta = np.zeros(d)
    losses: List[float] = []
    grad_norms: List[float] = []

    for k in range(1, max_iter + 1):
        residual = X @ theta - y
        loss = 0.5 / n * np.dot(residual, residual)
        grad = (X.T @ residual) / n
        grad_norm = np.linalg.norm(grad)

        theta -= alpha * grad

        if k % log_every == 0 or k == 1:
            losses.append(loss)
            grad_norms.append(grad_norm)
            if callback:
                callback(k, loss, grad_norm)
        if grad_norm < tol:
            break

    history = {"losses": losses, "grad_norms": grad_norms}
    return theta, history
