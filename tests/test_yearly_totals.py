import pandas as pd
import pytest

from data_analysis import get_yearly_totals


def test_yearly_totals():
    df = pd.DataFrame({
        "Date": ["2023-01-05", "2024-03-01"],
        "Sales": [100, 50],
    })

    assert get_yearly_totals(df, "Date", "Sales") == {2023: 100.0, 2024: 50.0}


def test_yearly_totals_ignores_invalid_dates():
    df = pd.DataFrame({
        "Date": ["2024-01-01", "not a date"],
        "Sales": [20, 10],
    })

    assert get_yearly_totals(df, "Date", "Sales") == {2024: 20.0}


def test_yearly_totals_missing_date_column():
    df = pd.DataFrame({"Sales": [10]})

    with pytest.raises(KeyError, match="Column not found"):
        get_yearly_totals(df, "Date", "Sales")
