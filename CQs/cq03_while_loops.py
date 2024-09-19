"""Practice using a while loop to iterate over a string"""

__author__ = "730739772"


def num_instances(phrase: str, search_char: str) -> int:
    """Will check each character of phrase and count how many
    characters match the character searched"""
    count: int = 0  # starting count at 0
    track_index: int = 0  # starting index at 0

    while track_index < len(phrase):  # keeps going until the index > length of phrase
        if (
            phrase[track_index] == search_char
        ):  # this checks the specific letter of the phrase
            count += 1
            # if it matches it will add 1 to the count
        track_index += 1
        # put on the same indent as if so that the variable increases always

    return count
