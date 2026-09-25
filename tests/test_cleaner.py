# tests/test_cleaner.py
"""Unit tests for the data cleaning pipeline."""

from __future__ import annotations

import pandas as pd
import pytest

from src.preprocessing.cleaner import (
    convert_price_to_numeric,
    filter_valid_prices,
    get_missing_value_summary,
    remove_duplicate_listings,
)


class TestPriceConversion:
    """Tests for price string parsing and numeric conversion."""

    def test_strip_currency_symbols(self) -> None:
        raw_prices = pd.Series(["$120.00", "$1,450.50", "300", "$80.43"])
        converted = convert_price_to_numeric(raw_prices)
        assert converted.tolist() == pytest.approx([120.0, 1450.5, 300.0, 80.43])

    def test_handles_non_numeric_and_nulls(self) -> None:
        raw_prices = pd.Series(["$50.00", "N/A", None, "Contact for Price"])
        converted = convert_price_to_numeric(raw_prices)
        assert converted.iloc[0] == pytest.approx(50.0)
        assert pd.isna(converted.iloc[1])
        assert pd.isna(converted.iloc[2])
        assert pd.isna(converted.iloc[3])


class TestDeduplication:
    """Tests for listing deduplication."""

    def test_dedup_by_id(self) -> None:
        df = pd.DataFrame(
            {"id": [101, 102, 101, 103], "price": [100.0, 150.0, 100.0, 200.0]}
        )
        deduped = remove_duplicate_listings(df, id_col="id")
        assert len(deduped) == 3
        assert deduped["id"].tolist() == [101, 102, 103]

    def test_dedup_fallback_no_id(self) -> None:
        df = pd.DataFrame({"room_type": ["Entire", "Private", "Entire"]})
        deduped = remove_duplicate_listings(df, id_col="id")
        assert len(deduped) == 2


class TestPriceFiltering:
    """Tests for filtering invalid price rows."""

    def test_removes_zero_negative_and_nan(self) -> None:
        df = pd.DataFrame({"price": [150.0, 0.0, -25.0, None, 250.0, 120000.0]})
        cleaned = filter_valid_prices(df, min_price=1.0, max_price=100000.0)
        assert cleaned["price"].tolist() == pytest.approx([150.0, 250.0])


class TestMissingSummary:
    """Tests for missing value summary generation."""

    def test_missing_summary_calculation(self) -> None:
        df = pd.DataFrame({"bedrooms": [1.0, None, 2.0, None], "bathrooms": [1.0, 1.0, 1.0, 1.0]})
        summary = get_missing_value_summary(df, columns=["bedrooms", "bathrooms"])
        assert "bedrooms" in summary.index
        assert summary.loc["bedrooms", "missing_count"] == 2
        assert summary.loc["bedrooms", "missing_pct"] == pytest.approx(50.0)
        assert "bathrooms" not in summary.index
