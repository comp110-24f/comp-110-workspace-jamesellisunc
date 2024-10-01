"""Returns the concatenation of two strings"""

__author__ = "730739772"


def concat(input1: str, input2: str) -> str:
    return input1 + input2


if __name__ == "__main__":  # prevents module from running when imported

    # Global variables
    word1 = "happy"
    word2 = "tuesday"
    print(concat(word1, word2))
