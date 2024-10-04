"""Mutating functions."""

__author__ = "730776315"


def manual_append(inp_list: list[int], app: int) -> None:
    return inp_list.append(app)


def double(inp_list: list[int]) -> None:
    ind: int = 0
    while ind < len(inp_list):
        inp_list[ind] = inp_list[ind] * 2
        ind += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
