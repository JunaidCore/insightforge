import pandas as pd
import pytest

from data_analysis import get_difference_from_mean


def test_difference_from_mean():
    df = pd.DataFrame({"Sales": [1, 2, 3]})

    assert get_difference_from_mean(df, "Sales") == [-1.0, 0.0, 1.0]


def test_difference_from_mean_missing_value_is_none():
    df = pd.DataFrame({"Sales": [None, 4, 6]})

    assert get_difference_from_mean(df, "Sales") == [None, -1.0, 1.0]


def test_difference_from_mean_missing_column():
    df = pd.DataFrame({"Sales": [1]})

    with pytest.raises(KeyError, match="Column not found"):
        get_difference_from_mean(df, "Profit")
