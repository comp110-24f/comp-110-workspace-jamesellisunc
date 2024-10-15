"""Summing the elements of a list using different loops"""

__author__ = "730739772"


def w_sum(vals: list[float]) -> float:
    """Not very efficient compared to later functions but provides the most control"""
    index = 0  # start at first element
    end_value = 0.0  # returns 0.0 if list is empty
    while index < len(vals):
        end_value += vals[index]  # adds element in list to total
        index += 1

    return end_value


def f_sum(vals: list[float]) -> float:
    """Saves time compared to while loops, more efficient"""
    total = 0.0

    for numb in vals:  # for loop that allows me to use 1 less variable then before
        total += numb

    return total


def f_range_sum(vals: list[float]) -> float:
    """Makes use of the range function"""
    range_total = 0.0

    for numb in range(0, len(vals)):
        # range function that allows me to include only specific values
        range_total += vals[numb]
        # fix after autograder, mistake was I added indexes not elements

    return range_total
