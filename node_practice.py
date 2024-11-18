"""Linked lists - CL23, CL24, EX08."""

from __future__ import annotations

__author__ = "730776315"


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)


def recursive_range(start: int, end: int) -> Node | None:
    # edge case:
    if start > end:
        raise ValueError("start is greater than end")
    else:
        # base case
        if start == end:
            return None
        # recursive case
        else:
            first: int = start
            rest: Node | None = recursive_range(start + 1, end)
            return Node(first, rest)


# base case: start==end parameter; exits the function
# recursive case: start < end; calls function again for the linked item
# call simulator:
#   r_range(110, 113) - recursive - outcome is Node(110, Node(111, Node(112, None)))
#   r_range(111, 113) - recursive - outcome is Node(111, Node(112, None)
#   r_range(112, 113) - recursive - outcome is Node(112,None)
#   r_range(113, 113) - base - outcome is None
# form the insidemost node first (the one with None as the next item)


def factorial(n: int) -> int:
    # edge case
    if n < 0:
        return -1
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)
