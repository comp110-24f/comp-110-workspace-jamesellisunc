"""Mutating functions."""

__author__ = "730739772"


def manual_append(a: list[int], value: int) -> None:
    a.append(value)  # adding a value


def double(a: list[int]) -> None:
    """Doubles the value of each item in list"""
    index = 0  # go through each item in a list
    while index < len(a):  # must be < and not <=, will give index error
        a[index] *= 2  # made the mistake of using append, created infinite loop
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
