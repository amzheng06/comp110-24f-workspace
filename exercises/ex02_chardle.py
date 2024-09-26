"""EX02 - Chardle - A cute step toward Wordle"""

__author__: str = "730776315"


def main() -> None:
    contains_char(input_word(), input_letter())


def input_word() -> str:
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exits program when user input is not 5 letters long
    return user_word


def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exits program when user input is not a single character
    return user_letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0  # counts how many occurences of letter there are in word
    # to identify if letter equals the letter at each index of word:
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:  # when letter is not found in word
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
