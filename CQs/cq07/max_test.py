"""Challenge Question 07 - 10/16/2024"""

from CQs.cq07.find_max import find_and_remove_max

__author__ = "730776315"


def test_gen() -> None:
    a: list[int] = [1, 2, 3, 4, 5]

    assert find_and_remove_max(a) == 5


def test_mut() -> None:
    b: list[int] = [4, 4, 4, 3]
    find_and_remove_max(b)

    assert b == [3]


def test_edge() -> None:
    c: list[int] = [-1, -2, -3, -4]
    assert find_and_remove_max(c) == -1
