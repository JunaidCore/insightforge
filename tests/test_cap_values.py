import pandas as pd
import pytest

from data_analysis import cap_values


def test_cap_values():
    df = pd.DataFrame({"Sales": [1, 5]})

    assert cap_values(df, "Sales", 2, 10) == [2.0, 5.0]


def test_cap_values_missing_value_is_none():
    df = pd.DataFrame({"Sales": [None, 3]})

    assert cap_values(df, "Sales", 0, 10) == [None, 3.0]


def test_cap_values_rejects_inverted_range():
    df = pd.DataFrame({"Sales": [1]})

    with pytest.raises(ValueError, match="must not be greater"):
        cap_values(df, "Sales", 10, 2)
