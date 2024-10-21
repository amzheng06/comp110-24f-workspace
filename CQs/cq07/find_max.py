"""Challenge Question 07 - 10/16/2024"""

__author__ = "730776315"


def find_and_remove_max(inp_list: list[int]) -> int:
    if len(inp_list) == 0:
        return int(-1)
    ind: int = 0
    max: int = inp_list[0]
    while ind < len(inp_list):
        if inp_list[ind] > max:
            max = inp_list[ind]
        ind += 1
    ind = 0
    while ind != len(inp_list):
        if inp_list[ind] == max:
            inp_list.pop(ind)
        else:
            ind += 1
    return max
