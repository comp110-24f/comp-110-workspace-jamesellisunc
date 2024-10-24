"""Importing a function and practicing unit tests"""

__author__ = "730739772"

from CQs.cq07.find_max import find_and_remove_max  # import function


def test_find_and_remove_max_expected_value() -> None:
    """Should return the expected value"""
    trial_lst: list[int] = [11, 7, 4, 3, 11]
    largest_num = find_and_remove_max(trial_lst)
    # assign whatever the biggest value is to a variable
    assert largest_num == 11  # highest value in trial list


def test_find_and_remove_max_mutation() -> None:
    """Should mutate list by removing all instances of max val"""
    trial_lst: list[int] = [11, 11, 7, 4, 3]
    find_and_remove_max(trial_lst)
    # mutate the list by popping all instances largest value
    assert trial_lst == [7, 4, 3]  # expected outcome


def test_find_and_remove_max_edge_case() -> None:
    """Incase of unconventional input"""
    assert find_and_remove_max([]) == -1
