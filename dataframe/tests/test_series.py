from dataframe import Series
import pytest

def test_series_sum():
    series1 = Series(data=[1, 2], name="A")
    assert series1.sum() == 3


def test_series_min():
    series1 = Series(data=[1, 2, 3], name="A")
    assert series1.min() == 1

def test_series_mode():
    series1 = Series(data=[1, 2, 2, 3], name="A")
    assert series1.mode() == 2

def test_series_contains():
    series1 = Series(data=[1, 2, 3, 4], name="A")
    assert series1.contains(5) == False

def test_series_apply():
    series1 = Series(data=[1, 2, 3, 4], name="A")
    def square(x):
        return x**2
    new_series = series1.apply(square)
    match = Series(data=[1, 4, 9, 16], name="A")
    assert new_series == match

# TODO: ALL - Implement tests for all other Series methods
# Use the test_series_sum test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html