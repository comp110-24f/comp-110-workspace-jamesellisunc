"""3 functions to practice mutating lists as well as shifting elements in lists"""

__author__ = "730739772"


def only_evens(input_a: list[int]) -> list:
    """Creates a new list with the even elements of first list"""
    output_a = []  # create an empty list
    for elem in input_a:
        if elem % 2 == 0:  # even elements will be divisible by 2
            output_a.append(elem)

    return output_a


def sub(input_b: list[int], s_idx: int, e_idx: int) -> list:
    """Will generate a subset of the input list"""
    output_b = []  # create empty list

    if s_idx < 0:
        s_idx = 0  # minimum start index value must be 0

    if e_idx > len(input_b):
        e_idx = len(input_b)  # incase end index is > list length

    if len(input_b) == 0:  # returns empty list incase input list is empty
        return output_b
    elif s_idx >= len(input_b):  # start index cant be > list length
        return output_b
    elif e_idx <= 0:  # end index cant be <= 0
        return output_b
    elif s_idx > e_idx:  # if start is greater than end index
        return output_b

    for index in range(s_idx, e_idx):
        # e_idx isnt included in the range (e_idx-1 as asked in prompt)
        output_b.append(input_b[index])

    return output_b


def add_at_index(input_c: list[int], int_elem: int, idx: int) -> None:
    """int is added at a specific index"""

    if idx < 0 or idx > len(input_c):  # incase index is out of range
        raise IndexError("Index is out of bounds for the input list")

    input_c.append(0)  # add a placeholder value to the end of the list

    for elem in range(len(input_c) - 2, idx - 1, -1):
        # len(input_c) - 2 gives us the last value in the list before we appended
        # idx -1 is our stopping point (tried idx but it didnt work need -1)
        # -1 is the step, we need to go backwards
        input_c[elem + 1] = input_c[elem]  # shifts elements to the right by 1

    input_c[idx] = int_elem
