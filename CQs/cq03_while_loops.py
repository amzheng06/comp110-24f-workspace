"""Challenge Question 03 - 9/18/2024"""

__author__: str = "730776315"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns number of occurences of search_char in phrase"""
    count: int = 0
    index: int = 0
    # index represents the index of the current letter of the phrase that is being
    # compared
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count
