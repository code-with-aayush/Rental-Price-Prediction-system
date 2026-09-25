"""
shap_explainer — SHAP-based explanation utilities.

TODO (Sprint 4):
    - Generate SHAP values for the best model.
    - Produce summary plot, dependence plots, and waterfall plots.
    - Expose helper for per-prediction explanations in Streamlit.
"""

from __future__ import annotations

from typing import Any

import pandas as pd


def explain_prediction(
    model: Any,
    X_instance: pd.DataFrame,
) -> dict:
    """Generate a SHAP explanation for a single prediction.

    Parameters
    ----------
    model : Any
        Trained model object.
    X_instance : pd.DataFrame
        Single-row DataFrame with the input features.

    Returns
    -------
    dict
        SHAP values and base value.

    Raises
    ------
    NotImplementedError
        SHAP integration is planned for Sprint 4.
    """
    raise NotImplementedError(
        "SHAP explainer is planned for Sprint 4."
    )
