"""3 Unit Tests for each function in utils file"""

__author__ = "730739772"

from exercises.ex05.utils import only_evens, sub, add_at_index

"""only_evens unit tests"""


def test_only_evens_return_val() -> None:
    """Test a list with both even and odd numbers"""
    list_a: list[int] = [1, 2, 3, 4, 5, 6]
    assert (only_evens(list_a)) == [2, 4, 6]


def test_only_evens_just_odds() -> None:
    """Test a list with only odd numbers"""
    list_a: list[int] = [1, 3, 5, 7, 9, 11]  # only odd numbers
    assert (only_evens(list_a)) == []


def test_only_evens_edge_case() -> None:
    """ "An empty list should provide a new empty list in return"""
    list_a: list[int] = []  # nothing to be appended to a new list
    assert (only_evens(list_a)) == []


"""sub unit tests"""


def test_sub_return_val() -> None:
    """Should return a subset of a list from a range of two indexes"""
    list_a: list[int] = [1, 2, 3, 4, 5, 6]
    assert (sub(list_a, 1, 4)) == [2, 3, 4]  # should return indexes 1-3


def test_sub_large_end_range() -> None:
    """Should return from start index to the end of the list if end is > len(list)"""
    list_a: list[int] = [1, 2, 3, 4, 5, 6]
    assert (sub(list_a, 1, 9)) == [2, 3, 4, 5, 6]
    # e_idx should change from 9 to len(list_a)


def test_sub_edge_case() -> None:
    """sub called on an empty list should return an empty list"""
    list_a: list[int] = []
    assert (sub(list_a, 1, 3)) == []
    # should return a new empty list because list_a is empty


"""add_at_index unit tests"""


def test_add_at_index_return_val() -> None:
    """Test appending a value to a list"""
    list_a: list[int] = [1, 2, 3, 4]
    add_at_index(list_a, 10, 1)
    assert list_a == [1, 10, 2, 3, 4]


def test_add_at_index_first_of_list() -> None:
    """Test to see if value can be appended to the first of list"""
    list_a: list[int] = [1, 2, 3, 4]
    add_at_index(list_a, 10, 0)
    assert list_a == [10, 1, 2, 3, 4]


def test_add_at_index_end_of_list() -> None:
    """Test to see if value can be appended to the end of list"""
    list_a: list[int] = [1, 2, 3, 4]
    add_at_index(list_a, 10, 4)
    assert list_a == [1, 2, 3, 4, 10]


def test_add_at_index_edge_case() -> None:
    """Test that an empty list can still be appended"""
    list_a: list[int] = []
    add_at_index(list_a, 5, 0)
    assert list_a == [5]
