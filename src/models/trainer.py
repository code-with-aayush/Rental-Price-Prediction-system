"""
trainer — Model training pipeline.

TODO (Sprint 3):
    - Train Linear Regression, Decision Tree, Random Forest, XGBoost, CatBoost.
    - Persist trained models to models/ via Joblib.
    - Support hyperparameter grids for GridSearchCV / RandomizedSearchCV.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

MODELS_DIR = Path(__file__).resolve().parents[3] / "models"


def train_model(
    name: str,
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> Any:
    """Train a regression model identified by *name*.

    Parameters
    ----------
    name : str
        Model identifier.  One of ``"linear_regression"``,
        ``"decision_tree"``, ``"random_forest"``, ``"xgboost"``, ``"catboost"``.
    X_train : pd.DataFrame
        Training features.
    y_train : pd.Series
        Training target.

    Returns
    -------
    Any
        The fitted model object.

    Raises
    ------
    NotImplementedError
        Model training is planned for Sprint 3.
    """
    raise NotImplementedError(
        f"Training for '{name}' is planned for Sprint 3."
    )
