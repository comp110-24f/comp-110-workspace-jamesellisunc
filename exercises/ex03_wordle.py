"""Making a wordle game by expanding off of ex02"""

__author__ = "730739772"


def input_guess(secret_word_len: int) -> str:
    """Prompts user to input a word with the length of the secret word"""
    guess = input(f"Enter a {secret_word_len} character word: ")
    # local variable for user guess

    while len(guess) != secret_word_len:
        # repeats until the guess is the same length as the secret word
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # using f string so the loop is viable for any length of secret
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if guessed letter is in secret word"""
    assert len(char_guess) == 1  # only allows the guessed letter to be 1 letter

    index = 0  # start with checking the 1st character
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1

    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Compares the guess to the secret word and emojifies the result"""
    assert len(guess) == len(secret)  # guess and secret word are the same length
    emoji_string = ""  # start an empty string for the emojis
    index = 0  # start with the first character

    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX  # if letters match and are in the same spot
        elif contains_char(secret, guess[index]):  # have to call contains_char here
            emoji_string += YELLOW_BOX  # if letters match but aren't in the same spot
        else:
            emoji_string += WHITE_BOX  # letters do not match

        index += 1  # check next index of both the guess and the secret word

    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1  # start on turn 1
    total_turns = 6  # only 6 turns per game

    while turn <= total_turns:
        print(
            f"=== Turn {turn}/{total_turns} ==="
        )  # f string allows us to change the total turn count

        guess = input_guess(len(secret))  # makes sure guess is the right length
        emoji_string = emojified(
            guess, secret
        )  # turns the guess into emoji form and prints
        print(emoji_string)

        if guess == secret:
            print(f"You won in {turn}/{total_turns} turns!")
            return None  # ends the game

        turn += 1  # if the guess != secret, move to next turn

    # if guess!=secret in 6 turns
    print(f"X/{total_turns} - Sorry, try again tomorrow!")
    # f string because total turns may change


if __name__ == "__main__":  # allows us to run the program
    main(secret="codes")
    # can change "codes" to whatever you want the secret word to me)
