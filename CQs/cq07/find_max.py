"""CQ07 Function to be imported"""

__author__ = "730739772"


def find_and_remove_max(input: list[int]) -> int:
    """Return the largest int and remove the rest"""
    index = 0
    largest_num = 0

    if len(input) == 0:  # for an empty list
        return -1

    for num in input:  # for/in loop that finds the largest number
        if num > largest_num:
            largest_num = num

    while index < len(input):
        if input[index] == largest_num:
            input.pop(index)  # removes all instances of largest number
        index += 1

    return largest_num
