"""Some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty string and then we can copy values over
    index: int = 0  # local variables: copy, index, msg, and char
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index] == char):  # if mes[index] != char
            # add it to copy
            copy += msg[index]  # copy = copy + msg[index]
        index += 1  # index = index + 1
    return copy


if __name__ == "__main__":
    # create a variable called word with the value "yoyo"
    word: str = "yoyo"  # GLOBAL variable
    # print the result of calling your function with arguments word and "y"
    print(remove_chars(msg=word, char="y"))  # with keyword arguments
    # pring the result of calling your function with arguments word and "o"
    print(remove_chars(word, "o"))  # with positional arguments
