"""EX04 - List utils."""

__author__ = "730776315"


def all(inp_list: list[int], inp_int: int) -> bool:
    """Returns whether or not all ints in the list equal inp_int."""
    ind: int = 0
    while ind < len(inp_list):
        if inp_list[ind] != inp_int:
            return False  # exits
        ind += 1
    return True


def max(inp_list: list[int]) -> int:
    """Finds the maximum number in a list."""
    if len(inp_list) == 0:
        raise ValueError("max() arg  is an empty List")
    ind: int = 1  # because the value at ind=0 is already stor_max
    stor_max: int = inp_list[0]
    while ind < len(inp_list):
        if inp_list[ind] > stor_max:
            stor_max = inp_list[ind]
        ind += 1
    return stor_max


def is_equal(inp_list1: list[int], inp_list2: list[int]) -> bool:
    """Assesses whether elements at every index of two lists are equal."""
    if len(inp_list1) != len(inp_list2):  # accounts for if lists are not equally long
        return False
    ind: int = 0
    while ind < len(inp_list1) and ind < len(inp_list2):
        if inp_list1[ind] != inp_list2[ind]:
            return False  # exits
        ind += 1
    return True


def extend(inp_list1: list[int], inp_list2: list[int]) -> None:
    """Appends values of inp_list2 to inp_list1."""
    ind: int = 0
    while ind < len(inp_list2):
        inp_list1.append(inp_list2[ind])  # appends item at each index individually
        ind += 1
