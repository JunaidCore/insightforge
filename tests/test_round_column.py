import pandas as pd
import pytest

from data_analysis import round_column


def test_round_column():
    df = pd.DataFrame({"Price": [1.234, 5.678]})

    assert round_column(df, "Price") == [1.23, 5.68]


def test_round_column_missing_value_is_none():
    df = pd.DataFrame({"Price": [None, 2.5]})

    assert round_column(df, "Price") == [None, 2.5]


def test_round_column_rejects_negative_decimals():
    df = pd.DataFrame({"Price": [1.5]})

    with pytest.raises(ValueError, match="must not be negative"):
        round_column(df, "Price", decimals=-1)
