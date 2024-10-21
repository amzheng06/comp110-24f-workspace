"""a lil testing file"""

__author__: str = "730776315"


# cl11 - global variables and scope


# def remove_chars(msg: str, char: str) -> str:
#    """return copy of msg w/o char"""
#    copy: str = ""
#    index: int = 0
#    while index < len(msg):
#        if msg[index] != char:
#            copy += msg[index]
#        index += 1
#    return copy


# word: str = "yoyo"
# print(remove_chars(word, "o"))


# cl13 - lists

# my_number: list[float] = []

# grocer_list: list[str] = []

# grocer_list.append("bananas")
# grocer_list.append("bananas")
# grocer_list.append("bananas")
# grocer_list[2] = "eggs"

# print(grocer_list)


# cl15 - for loops

# names: list[str] = ["Alyssa", "Janet", "Vrinda"]

# for idx in range(0, len(names)):  # index for loop method
#    print(f"{idx}: {names[idx]}")

# index: int = 0
# while index < len(names):
#    print(f"{index}: {names[index]}")
#    index += 1


# cl17 - dictionaries

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
