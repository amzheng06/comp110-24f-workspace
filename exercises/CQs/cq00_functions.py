"""Challenge Question 00 - 8/28/2024"""

__author__ = "730776315"


def mimic(message: str) -> str:
    """Repeats the input back to user"""
    return message


def main() -> None:
    """pulls together functions into main function; implements high level logic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
