"""a lil testing file"""

# import math

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

# ice_cream: dict[str, int] = {
#    "chocolate": 12,
#    "vanilla": 8,
#    "strawberry": 4,
# }

# total_orders: int = 0
# for flavor in ice_cream:
#    total_orders += ice_cream[flavor]


# class Circle:
#    radius: float

#    def __init__(self, r: float):
#        self.radius = r

#    def area(self):
#        return math.pi * self.radius**2


# class Rectangle:
#    width: float
#    height: float

#    def __init__(self, w: float, h: float):
#        self.width = w
#        self.height = h

#    def area(self):
#        return self.width * self.height


class Course:
    """Models the idea of a UNC Course."""

    name: str
    level: int
    prereqs: list[str]

    def __init__(self):
        self.name = ""
        self.level = 0

    def is_valid_course(self, inp: str) -> bool:
        if self.level < 400:
            return False
        else:
            for c in self.prereqs:
                if c == inp:
                    return True
            return False


def find_courses(inp: list[Course], prereq: str) -> list[str]:
    """Finds 400+ level courses w/ the given prereq."""
    results: list[str] = []

    for c in inp:
        if c.level >= 400:
            for p in c.prereqs:
                if p == prereq:
                    results.append(c.name)
    return results


class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str):
        self.make = make
        self.model = ""
        self.year = 0
        self.color = ""
        self.mileage = 0.0

    def update_mileage(self, miles: float):
        self.mileage = miles

    def display_info(self) -> None:
        info: str = ""
        print(info)


def calculate_depreciation(inp: Car, depreciation_rate: float) -> float:
    return depreciation_rate * inp.mileage
