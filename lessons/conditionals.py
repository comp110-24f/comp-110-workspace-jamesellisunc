"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


less_than_10(num=5)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:  # conditonal/boolean expression
        print("Eat some food")  # "then" block
    else:
        print("Do your Comp 110 homework instead")  # "else" block
    print("Im proud of you <3")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word."""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"
