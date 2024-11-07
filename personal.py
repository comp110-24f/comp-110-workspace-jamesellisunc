def odd_and_even(input: list[int]) -> list[int]:
    """Returns elements of input that are odd and have an even index"""
    new_list: list[int] = []

    for idx in range(0, len(input)):
        if input[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(input[idx])

    return new_list


def short_words(input: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters"""
    new_list: list[str] = []

    for elem in input:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list


def value_exits(input_dict: dict[str, int], val: int) -> bool:
    """Evaluates if a given value exists in a dict"""
    for key in input_dict:
        if input_dict[key] == val:
            return True
    return False


def pls_or_minus_n(inp: dict[str, int], n: int) -> None:
    """Checks if each val in a dict is even or odd"""
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n
