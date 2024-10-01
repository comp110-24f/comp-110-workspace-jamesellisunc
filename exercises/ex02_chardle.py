"""My third exercise making a wordle-like game!"""

__author__ = "730739772"


def input_word() -> str:
    """Prompts user to enter a 5 letter word"""
    user_word: str = str(input("Enter a 5-character word: "))  # initial prompt proposed

    if len(user_word) != 5:  # error if length doesnt equal 5
        print("Error: Word must contain 5 characters.")
        exit()  # exits function early to not confuse user (before return function)
    return user_word


def input_letter() -> str:
    """Prompts user to enter a single character"""
    user_letter: str = str(input("Enter a single character: "))  # 2nd prompt proposed

    if len(user_letter) != 1:  # error if length isnt 1 character
        print("Error: Character must be a single character.")
        exit()  # exits function early to not confuse user (before return function)
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Checks if input character matches any characters in word"""
    count = 0  # number of repeats
    print(
        "Searching for " + letter + " in " + word
    )  # lets user know what they inputed prior
    check_index = 0
    while check_index < len(
        word
    ):  # while loop goes until every character of word is checked
        if word[check_index] == letter:
            print(str(letter) + " found at index " + str(check_index))
            count += 1  # increase count number
        check_index += 1  # increase index number

    # gives different message depending on the count number
    if count == 0:
        print(
            "No instances of " + str(letter) + " found in " + str(word)
        )  # count is 0, no instances
    elif count == 1:
        print("1 instance of " + str(letter) + " found in " + str(word))  # count is 1
    else:
        print(
            str(count) + " instances of " + str(letter) + " found in " + str(word)
        )  # count is greater than 1

    return None


def main() -> None:
    """Main function that runs the Chardle Game"""
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)  # calls both global variables


if __name__ == "__main__":
    main()
