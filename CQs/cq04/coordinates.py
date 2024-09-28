"""Challenge Question 04 - Returns pair combinations for each character in 2 strings"""

__author__ = "730776315"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0  # tracks index of xs
    index2: int = 0  # tracks index of ys
    while index1 < len(xs):
        while index2 < len(ys):
            print(f"({xs[index1]},{ys[index2]})")
            index2 += 1
        index1 += 1
        index2 = 0  # resets the value so that the nested loop runs again
