"""Smoke tests for evaluation utilities."""

from __future__ import annotations

import numpy as np
import pytest

from src.models.evaluator import evaluate_model, mean_absolute_percentage_error


class TestMAPE:
    """Tests for MAPE calculation."""

    def test_perfect_predictions(self) -> None:
        y = np.array([100.0, 200.0, 300.0])
        assert mean_absolute_percentage_error(y, y) == pytest.approx(0.0)

    def test_known_values(self) -> None:
        y_true = np.array([100.0, 200.0])
        y_pred = np.array([110.0, 180.0])
        expected = ((10 / 100) + (20 / 200)) / 2 * 100  # 10%
        assert mean_absolute_percentage_error(y_true, y_pred) == pytest.approx(expected)

    def test_ignores_zero_actuals(self) -> None:
        y_true = np.array([0.0, 100.0])
        y_pred = np.array([10.0, 110.0])
        expected = (10 / 100) * 100  # only the non-zero entry
        assert mean_absolute_percentage_error(y_true, y_pred) == pytest.approx(expected)


class TestEvaluateModel:
    """Tests for the full evaluation dict."""

    def test_returns_all_keys(self) -> None:
        y = np.array([1.0, 2.0, 3.0])
        result = evaluate_model(y, y)
        assert set(result.keys()) == {"mae", "rmse", "mape", "r2"}

    def test_perfect_r2(self) -> None:
        y = np.array([1.0, 2.0, 3.0])
        result = evaluate_model(y, y)
        assert result["r2"] == pytest.approx(1.0)
