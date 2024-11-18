"""Linked lists - CL23, CL24, EX08."""

from __future__ import annotations

__author__ = "730776315"


class Node:
    """Node is a class where each object has value and link to next Node."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes Node with a value and next Node or None."""
        self.value = val
        self.next = next


three: Node = Node(2, None)
two: Node = Node(3, three)
one: Node = Node(1, two)


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node stored at the given index."""
    # edge case
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        # base case
        if index != 0:
            return value_at(head.next, index - 1)
        # recursive case
        else:
            return head.value


def max(head: Node | None) -> int:
    """Return the maximum data value in the linked list."""
    # edge case
    if head is None:
        raise ValueError("Cannot call max with None")

    else:
        # base case
        if head.next is None:
            return head.value
        # recursive case
        else:
            if head.value > head.next.value:
                head.next.value = head.value
            return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of Nodes with the same values as input list."""
    # base case
    if len(items) == 0:
        return None
    # recursive case
    else:
        first: int = items[0]
        items.pop(0)
        rest: Node | None = linkify(items)
        return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a linked list of Nodes with each value multiplied by factor."""
    # edge case
    if head is None:
        return None
    else:
        # base case
        if head.next is None:
            new: Node = Node(head.value * factor, None)
            return new
        # recursive case
        else:
            new = Node(head.value * factor, scale(head.next, factor))
            return new
