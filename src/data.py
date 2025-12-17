"""Veri üretimi ve ön işleme yardımcıları."""

from __future__ import annotations

from typing import Tuple

import numpy as np


def make_synthetic_linear(
    n: int,
    d: int,
    p: int,
    noise_std: float = 0.5,
    seed: int | None = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Kolinear özellikler içeren sentetik veri üret.

    Args:
        n: Örnek sayısı.
        d: Özellik sayısı (>=1).
        p: Kolinearlık şiddeti; x2 = x1 + 10^-p * gürültü.
        noise_std: Hedefe eklenen gürültü std.
        seed: RNG sabiti.
    Returns:
        X (n, d), y (n,), theta_true (d,)
    """
    rng = np.random.default_rng(seed)
    x1 = rng.normal(size=(n, 1))
    features = [x1]

    if d >= 2:
        x2 = x1 + (10.0 ** (-p)) * rng.normal(size=(n, 1))
        features.append(x2)

    if d > 2:
        rest = rng.normal(size=(n, d - 2))
        features.append(rest)

    X = np.hstack(features)
    theta_true = rng.normal(size=(d,))
    noise = noise_std * rng.normal(size=n)
    y = X @ theta_true + noise
    return X, y, theta_true


def train_val_split(
    X: np.ndarray,
    y: np.ndarray,
    val_ratio: float = 0.2,
    seed: int | None = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Basit karıştırmalı train/val bölmesi."""
    rng = np.random.default_rng(seed)
    n = X.shape[0]
    idx = rng.permutation(n)
    split = int(n * (1 - val_ratio))
    train_idx, val_idx = idx[:split], idx[split:]
    return X[train_idx], X[val_idx], y[train_idx], y[val_idx]


def standardize(
    X_train: np.ndarray, X_val: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Eğitim ortalama/std ile standardizasyon.

    Returns:
        X_train_std, X_val_std, mean, std
    """
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0) + 1e-12
    X_train_std = (X_train - mean) / std
    X_val_std = (X_val - mean) / std
    return X_train_std, X_val_std, mean, std
