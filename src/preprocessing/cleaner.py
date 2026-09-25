"""
cleaner — Data cleaning utilities.

TODO (Sprint 2):
    - Handle missing values (impute or drop based on threshold).
    - Remove duplicate listings.
    - Standardise column names and data types.
    - Flag / remove outliers using IQR or z-score.
"""

from __future__ import annotations

import pandas as pd


def load_raw_data(filepath: str) -> pd.DataFrame:
    """Load a raw CSV file and return a DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the raw CSV file.

    Returns
    -------
    pd.DataFrame
        The loaded data.
    """
    return pd.read_csv(filepath)


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate rows.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    pd.DataFrame
        DataFrame with duplicates removed.
    """
    return df.drop_duplicates().reset_index(drop=True)


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Handle missing values using the specified strategy.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    strategy : str
        One of ``"drop"`` or ``"median"``.  Expand as needed.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame.

    Raises
    ------
    NotImplementedError
        Full cleaning logic is planned for Sprint 2.
    """
    raise NotImplementedError(
        "Full cleaning pipeline is planned for Sprint 2."
    )
