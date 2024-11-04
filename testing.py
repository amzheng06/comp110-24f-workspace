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

total_orders: int = 0
for flavor in ice_cream:
    total_orders += ice_cream[flavor]

print(ice_cream)


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        return (
            ((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)
        ) ** 0.5

    def get_slope(self) -> float:
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)
