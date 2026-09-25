"""
engineer — Feature engineering utilities.

TODO (Sprint 2-3):
    - Create price_per_sqft feature.
    - Encode categorical columns (locality, furnishing status).
    - Bin continuous features (area, age of property).
    - Create amenity score from boolean amenity columns.
"""

from __future__ import annotations

import pandas as pd


def create_price_per_sqft(df: pd.DataFrame, price_col: str, area_col: str) -> pd.DataFrame:
    """Add a ``price_per_sqft`` column.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    price_col : str
        Column name for rental price.
    area_col : str
        Column name for area in square feet.

    Returns
    -------
    pd.DataFrame
        DataFrame with the new column appended.

    Raises
    ------
    NotImplementedError
        Full feature engineering is planned for Sprint 2–3.
    """
    raise NotImplementedError(
        "Feature engineering is planned for Sprint 2–3."
    )
