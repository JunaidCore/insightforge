import pandas as pd

from data_analysis import get_columns_with_missing


def test_columns_with_missing():
    df = pd.DataFrame({"Sales": [None], "Region": ["North"]})

    assert get_columns_with_missing(df) == ["Sales"]


def test_columns_with_missing_none_missing():
    df = pd.DataFrame({"Sales": [1], "Region": ["North"]})

    assert get_columns_with_missing(df) == []


def test_columns_with_missing_keeps_column_order():
    df = pd.DataFrame({"Region": [None], "Sales": [None]})

    assert get_columns_with_missing(df) == ["Region", "Sales"]
