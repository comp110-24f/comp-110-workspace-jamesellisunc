from personal import odd_and_even, short_words


def test_odd_and_even() -> None:
    """Case test"""
    input_list: list[int] = [7, 8, 10, 10, 5, 12, 3, 2, 11, 8]
    test = odd_and_even(input_list)
    output_list: list[int] = [7, 5, 3, 11]

    assert test == output_list


def test_short_words() -> None:
    input: list[str] = ["sun", "cloud", "sky"]
    test = short_words(input)
    output: list[str] = ["sun", "sky"]

    assert test == output
