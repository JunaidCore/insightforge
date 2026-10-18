import pandas as pd
import pytest

from data_analysis import get_rolling_sum


def test_rolling_sum():
    df = pd.DataFrame({"Sales": [4, 6]})

    assert get_rolling_sum(df, "Sales", window=1) == [4.0, 6.0]


def test_rolling_sum_incomplete_window_is_none():
    df = pd.DataFrame({"Sales": [1, 2]})

    assert get_rolling_sum(df, "Sales") == [None, None]


def test_rolling_sum_rejects_small_window():
    df = pd.DataFrame({"Sales": [1]})

    with pytest.raises(ValueError, match="at least 1"):
        get_rolling_sum(df, "Sales", window=0)
