import pandas as pd
import pytest

from data_analysis import get_coefficient_of_variation


def test_coefficient_of_variation():
    df = pd.DataFrame({"Sales": [0, 2, 4]})

    assert get_coefficient_of_variation(df, "Sales") == 100.0


def test_coefficient_of_variation_rejects_zero_mean():
    df = pd.DataFrame({"Sales": [-1, 1]})

    with pytest.raises(ValueError, match="mean is 0"):
        get_coefficient_of_variation(df, "Sales")


def test_coefficient_of_variation_needs_two_values():
    df = pd.DataFrame({"Sales": [5, None]})

    with pytest.raises(ValueError, match="at least two values"):
        get_coefficient_of_variation(df, "Sales")
