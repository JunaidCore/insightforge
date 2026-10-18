import pandas as pd
import pytest

from data_analysis import get_category_counts


def test_category_counts():
    df = pd.DataFrame({"Region": ["North"]})

    assert get_category_counts(df, "Region") == {"North": 1}


def test_category_counts_ignores_missing_values():
    df = pd.DataFrame({"Region": ["North", None]})

    assert get_category_counts(df, "Region") == {"North": 1}


def test_category_counts_missing_column():
    df = pd.DataFrame({"Region": ["North"]})

    with pytest.raises(KeyError, match="Column not found"):
        get_category_counts(df, "Product")
