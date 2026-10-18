import pandas as pd
import pytest

from data_analysis import get_standard_deviation


def test_standard_deviation_constant_column():
    df = pd.DataFrame({"Sales": [5, 5, 5]})

    assert get_standard_deviation(df, "Sales") == 0.0


def test_standard_deviation_ignores_missing_values():
    df = pd.DataFrame({"Sales": [None, 3, 3]})

    assert get_standard_deviation(df, "Sales") == 0.0


def test_standard_deviation_needs_two_values():
    df = pd.DataFrame({"Sales": [5]})

    with pytest.raises(ValueError, match="at least two values"):
        get_standard_deviation(df, "Sales")
