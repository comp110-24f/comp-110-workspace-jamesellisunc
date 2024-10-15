"""Showing the utility of the list function"""

__author__ = "730739772"


def all(a: list[int], value: int) -> bool:
    """Checks to see if all the items in the list are equal to value"""
    if len(a) == 0:
        return False  # fix after autograder, if list is empty, false immediately

    index = 0
    while index < len(a):
        if a[index] != value:  # check if item in list != value
            return False
        index += 1  # check next item in list
    return True


def max(input: list[int]) -> int:
    """Checks to see what the max value in the list is"""
    if len(input) == 0:  # checks if list has no item, therefore no max value
        raise ValueError("max() arg is an empty List")

    largest_num = input[0]  # set largest number in list to the first item
    index = 1  # set index to the 2nd item in the list before while loop

    while index < len(input):
        if input[index] > largest_num:
            largest_num = input[
                index
            ]  # sets new largest number if it is > than previous
        index += 1

    return largest_num


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Checks if both lists are deeply equal"""
    if len(list_a) != len(list_b):  # first checks if the lengths of each equal
        return False

    index = 0

    while index < len(list_a):
        if list_a[index] != list_b[index]:  # checks value of list at each index
            return False  # item at index of both lists does not match
        index += 1
    return True  # lists are deeply equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appends list 2 to the end of list 1"""
    index = 0

    while index < len(list_2):  # loop to append for each item in list 2
        list_1.append(list_2[index])  # appends to the end of list 1
        index += 1
