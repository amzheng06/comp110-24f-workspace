"""Challenge Question 02 - 9/13/2024"""

__author__ = "730776315"


def guess_a_number() -> None:
    secret: int = 7
    x = input("Guess a number:")
    print("Your guess was " + str(x))
    if secret == int(x):
        print("You got it!")
    elif secret < int(x):
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
