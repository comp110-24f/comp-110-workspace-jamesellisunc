"""Practice with dictionary functions"""

__author__ = "730739772"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values in a dictionary"""
    inverted_dict: dict[str, str] = {}  # initialize an empty dict

    for key in input_dict:
        value = input_dict[key]  # assign the value of a dictionary to a variable
        if value in inverted_dict:
            raise KeyError("Duplicate key found!")  # check for duplicate values
        else:
            inverted_dict[value] = key  # inverts the keys and values
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Finds the most common value in a dictionary"""

    if len(fav_colors) == 0:
        # autograder, incase of empty dict input (shouldve known by unit test)
        return ""

    color_count: dict[str, int] = {}  # initialize an empty dict

    for key in fav_colors:
        color = fav_colors[key]  # local variable used for conditions
        if color in color_count:
            color_count[color] += 1  # increase count if alr exists
        else:
            color_count[color] = 1  # add dict entry if DNE

    frequent_color = None  # None works as placeholder
    count = 0

    for key in fav_colors:
        color = fav_colors[key]  # local variable used as index for conditions
        if color_count[color] > count:
            frequent_color = color  # keeps order of "first" highest freq.
            count = color_count[color]
    return str(frequent_color)


def count(input_dict: list[str]) -> dict[str, int]:
    """Produce a dictionary that counts elem appearances in lists"""
    count_dict: dict[str, int] = {}  # initialize empty dict

    for key in input_dict:
        if key in count_dict:  # in conditional is super quick!
            count_dict[key] += 1  # if key exists, increment by 1
        else:
            count_dict[key] = 1  # if key DNE, set to 1
    return count_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary that alphabetizes each element in a list"""
    alphabet_dict: dict[str, list[str]] = {}  # initialize empty dict

    for word in input_list:
        first_letter = word[0].lower()  # new method that returns lower case of string

        if first_letter not in alphabet_dict:  # reverse of in conditional
            alphabet_dict[first_letter] = []  # create an empty list

        alphabet_dict[first_letter].append(word)  # append the value into list created

    return alphabet_dict


def update_attendance(
    attend_log: dict[str, list[str]], day: str, student_name: str
) -> None:
    """Modify a dictionary to track attendance of a list of students"""
    if day not in attend_log:  # conditional to test if day isnt a key yet
        attend_log[day] = []  # initialize empty list

    if student_name not in attend_log[day]:
        # autograder, must make sure to not repeat names
        attend_log[day].append(student_name)  # append value from dict to list
