"""
evaluator — Model evaluation utilities.

TODO (Sprint 3):
    - Compute MAE, RMSE, MAPE, R² for each model.
    - Generate comparison table and bar chart.
    - Select best model automatically.
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def mean_absolute_percentage_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Compute MAPE, excluding zero actuals to avoid division errors.

    Parameters
    ----------
    y_true : np.ndarray
        Ground-truth values.
    y_pred : np.ndarray
        Predicted values.

    Returns
    -------
    float
        MAPE as a percentage (0–100+).
    """
    mask = y_true != 0
    return float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)


def evaluate_model(
    y_true: np.ndarray,
    y_pred: np.ndarray,
) -> dict[str, float]:
    """Return a dict of evaluation metrics.

    Parameters
    ----------
    y_true : np.ndarray
        Ground-truth values.
    y_pred : np.ndarray
        Predicted values.

    Returns
    -------
    dict[str, float]
        Keys: ``mae``, ``rmse``, ``mape``, ``r2``.
    """
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "mape": mean_absolute_percentage_error(np.asarray(y_true), np.asarray(y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
    }
