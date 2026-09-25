# src/preprocessing/cleaner.py
"""Data cleaning pipeline for rental listings."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

IMPORTANT_FEATURES: list[str] = [
    "id",
    "name",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms",
    "bathrooms_text",
    "bedrooms",
    "beds",
    "amenities",
    "price",
    "minimum_nights",
    "maximum_nights",
    "latitude",
    "longitude",
    "neighbourhood_cleansed",
    "number_of_reviews",
    "review_scores_rating",
    "availability_365",
]


def load_raw_data(filepath: str | Path) -> pd.DataFrame:
    """Load raw CSV or compressed CSV dataset."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Raw data file not found: {path.resolve()}")
    return pd.read_csv(path)


def convert_price_to_numeric(series: pd.Series) -> pd.Series:
    """Convert price strings containing currency symbols into numeric values."""
    if series.dtype in ("object", "string"):
        cleaned = (
            series.astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        return pd.to_numeric(cleaned, errors="coerce")
    return pd.to_numeric(series, errors="coerce")


def remove_duplicate_listings(
    df: pd.DataFrame, id_col: str = "id"
) -> pd.DataFrame:
    """Remove duplicate listings based on listing ID or full rows."""
    if id_col in df.columns:
        return df.drop_duplicates(subset=[id_col]).reset_index(drop=True)
    return df.drop_duplicates().reset_index(drop=True)


def filter_valid_prices(
    df: pd.DataFrame,
    price_col: str = "price",
    min_price: float = 1.0,
    max_price: float = 100000.0,
) -> pd.DataFrame:
    """Filter out missing, zero, negative, or unrealistic price values."""
    valid_mask = (
        df[price_col].notnull()
        & (df[price_col] >= min_price)
        & (df[price_col] <= max_price)
    )
    return df.loc[valid_mask].reset_index(drop=True)


def get_missing_value_summary(
    df: pd.DataFrame, columns: list[str] | None = None
) -> pd.DataFrame:
    """Generate missing-value count and percentage summary for specified columns."""
    target_cols = [c for c in (columns or df.columns) if c in df.columns]
    missing_counts = df[target_cols].isnull().sum()
    missing_pct = (missing_counts / len(df)) * 100
    summary = pd.DataFrame(
        {"missing_count": missing_counts, "missing_pct": missing_pct.round(2)}
    )
    return summary[summary["missing_count"] > 0].sort_values(
        by="missing_count", ascending=False
    )


def print_cleaning_report(
    raw_rows: int,
    cleaned_df: pd.DataFrame,
    missing_summary: pd.DataFrame,
    price_stats: pd.Series,
) -> None:
    """Print standard cleaning pipeline audit metrics."""
    rows_removed = raw_rows - len(cleaned_df)
    print("=" * 60)
    print("RENTAL DATA CLEANING AUDIT REPORT")
    print("=" * 60)
    print(f"Raw row count:          {raw_rows:,}")
    print(f"Rows removed:           {rows_removed:,}")
    print(f"Final row count:        {len(cleaned_df):,}")
    print(f"Final column count:     {cleaned_df.shape[1]:,}")
    print("\nMissing-value summary (important features):")
    if not missing_summary.empty:
        print(missing_summary.to_string())
    else:
        print("No missing values in monitored features.")
    print("\nBasic price statistics:")
    print(price_stats.to_string())
    print("=" * 60)


def clean_rental_data(
    raw_filepath: str | Path = "data/raw/new_york_listings.csv.gz",
    output_filepath: str | Path = "data/processed/cleaned_listings.csv",
    price_col: str = "price",
    id_col: str = "id",
) -> pd.DataFrame:
    """Execute complete initial data cleaning pipeline and save processed output."""
    raw_df = load_raw_data(raw_filepath)
    raw_rows = len(raw_df)

    deduped_df = remove_duplicate_listings(raw_df, id_col=id_col)

    df = deduped_df.copy()
    df[price_col] = convert_price_to_numeric(df[price_col])
    cleaned_df = filter_valid_prices(df, price_col=price_col)

    missing_summary = get_missing_value_summary(cleaned_df, IMPORTANT_FEATURES)
    price_stats = cleaned_df[price_col].describe()

    if output_filepath:
        out_path = Path(output_filepath)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        cleaned_df.to_csv(out_path, index=False)

    print_cleaning_report(raw_rows, cleaned_df, missing_summary, price_stats)
    return cleaned_df


if __name__ == "__main__":
    clean_rental_data()
