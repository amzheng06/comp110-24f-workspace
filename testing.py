"""a lil testing file"""

__author__: str = "730776315"


# cl11 - global variables and scope


def remove_chars(msg: str, char: str) -> str:
    """return copy of msg w/o char"""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(word, "o"))