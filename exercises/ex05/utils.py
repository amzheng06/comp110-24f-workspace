"""EX05 - List Utility Testing - Function Definitions."""

__author__ = "730776315"


def only_evens(inp_list: list[int]) -> list[int]:
    """Returns a list of the even items in input list."""
    out_list: list[int] = []
    for elem in inp_list:
        if elem % 2 == 0:
            out_list.append(elem)  # does not modify input
    return out_list


def sub(inp_list: list[int], start: int, end: int) -> list[int]:
    """Returns a list of the values in the input from start index
    to the value before the end index."""
    out_list: list[int] = []
    if start < 0:  # edge case - start range
        start = 0
    if end > len(inp_list):  # edge case - end range
        end = len(inp_list)
    index: int = start
    if len(inp_list) == 0 or start >= len(inp_list) or end < 0:
        return out_list  # edge cases - returns empty list
    while index < end:
        out_list.append(inp_list[index])
        index += 1  # when index == end, inp_list[end] will not be in the output
    return out_list


def add_at_index(inp_list: list[int], inp_elem: int, inp_ind: int) -> None:
    """Mutates input to add an element at a specified index."""
    index: int = (
        inp_ind  # initializes index as inp_ind when looping and adding items to output
    )
    copy_ind: int = 0  # keeps track of index in copy_list during while loop
    if index < 0 or index > len(inp_list):
        raise IndexError("Index is out of bounds for the input list")
    inp_list.append(int(0))  # increases length of inp_list to accommodate inp_elem
    copy_list: list[int] = []
    while copy_ind < len(inp_list):
        copy_list.append(inp_list[copy_ind])
        copy_ind += 1
    # purpose of copy_list is to have a static version of the original values
    # and indexes in input
    while index < len(inp_list) - 1:  # len(inp_list)-1 prevents range error
        inp_list[index + 1] = copy_list[index]
        index += 1
    inp_list[inp_ind] = inp_elem
