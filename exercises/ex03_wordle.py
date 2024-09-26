"""EX03 - Wordle"""

__author__: str = "730776315"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    win_cond: int = 0  # 0 is false, 1 is true
    while turn < 6 and win_cond == 0:
        print(
            f"=== Turn {turn+1}/6 ==="
        )  # turn+1 to display the actual turn it's on, not index
        emoji_output: str = emojified(
            input_guess(guess_word_len=len(secret)), secret
        )  # input_guess returns guess_word
        print(emoji_output)
        if emoji_output == ("\U0001F7E9" * len(secret)):  # if all letters are correct
            win_cond = 1
        turn += 1
    if win_cond == 1:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(guess_word_len: int) -> str:
    """Prompts user to guess a word continually until guess is correct length"""
    guess_word: str = input(f"Enter a {guess_word_len} character word: ")
    while len(guess_word) != guess_word_len:
        guess_word = input(f"That wasn't {guess_word_len} chars! Try again: ")
    return guess_word


def contains_char(def_word: str, char_guess: str) -> bool:
    """Check whether a specific character is present in a word"""
    assert len(char_guess) == 1
    index: int = 0
    outcome: bool = (
        False  # if no letters in secret_word match char_guess, outcome remains False
    )
    while index < len(def_word):
        if def_word[index] == char_guess:
            outcome = True
        index += 1
    return outcome


def emojified(user_guess: str, secret_word: str) -> str:
    """Compare two equally long strings and return an emoji string"""
    assert len(user_guess) == len(secret_word)  # overrides error if not True
    index: int = 0
    emoji_string: str = ""
    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            emoji_string += "\U0001F7E9"
        elif contains_char(def_word=secret_word, char_guess=user_guess[index]) is True:
            emoji_string += "\U0001F7E8"
        else:
            emoji_string += "\U00002B1C"
        index += 1
    return emoji_string


if __name__ == "__main__":
    main(secret="codes")
