from dataframe import Series
import pytest

def test_series_sum():
    series1 = Series(data=[1, 2], name="A")
    assert series1.sum() == 3

def test_max():
    test_list_1 = Series(data = [-1,-2,-60,-420,-69], name = 'jeff')
    assert test_list_1.max() == -1

    test_list_2 = Series(data = [1_000_000, 420, 0, -1000], name = 'bob')
    assert test_list_2.max() == 1_000_000

    test_list_2 = Series(data = [1_000_000, 420, 0, -1000], name = 'bob')
    assert test_list_2.max() == 1_000_000


def test_replace():
    test_list = Series([1,2,1,3], name = 'bobby')
    assert test_list.replace(1,3) == [3,2,3,3]

    test_list = Series([1,2,1,3], name = 'billy')
    assert test_list.replace(4,3) == [1,2,1,1]


    


# TODO: ALL - Implement tests for all other Series methods
# Use the test_series_sum test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html
