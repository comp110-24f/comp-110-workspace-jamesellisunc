def get_first(input: list[str]) -> str:
    """Return first element."""
    if len(input) == 0:  # if empty input
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Remove and return first"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
