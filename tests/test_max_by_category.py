import pandas as pd
import pytest

from data_analysis import get_max_by_category


def test_max_by_category():
    df = pd.DataFrame({"Region": ["North", "South"], "Sales": [10, 20]})

    assert get_max_by_category(df, "Region", "Sales") == {"North": 10.0, "South": 20.0}


def test_max_by_category_skips_missing_category():
    df = pd.DataFrame({"Region": ["North", None], "Sales": [5, 7]})

    assert get_max_by_category(df, "Region", "Sales") == {"North": 5.0}


def test_max_by_category_missing_column():
    df = pd.DataFrame({"Sales": [10]})

    with pytest.raises(KeyError, match="Column not found"):
        get_max_by_category(df, "Region", "Sales")
