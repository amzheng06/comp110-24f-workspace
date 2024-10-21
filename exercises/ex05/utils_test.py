from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""EX05 - List Utility Testing - Defined Unit Tests."""

__author__ = "730776315"


def test_only_evens_use() -> None:
    a: list[int] = [1, 2, 3, 4, 5]
    """Test that only_evens works in a normal use case,
    and returns a list of the even items in the input."""
    assert only_evens(a) == [2, 4]


def test_only_evens_edge() -> None:
    b: list[int] = [-1, -3, -5, 101]
    """Test that only_evens returns an empty list when input has no even numbers."""
    assert only_evens(b) == []


def test_only_evens_mut() -> None:
    c: list[int] = [13, 14, 15, 16]
    only_evens(c)
    """Test that only_evens does not mutate the input list."""
    assert c == [13, 14, 15, 16]


def test_sub_use() -> None:
    d_inp_list: list[int] = [1, 2, 3, 4, 5]
    d_start: int = 1
    d_end: int = 3
    """Test that sub works in a normal use case,
    and returns a list with the elements from specified
    start to end of the input list."""
    assert sub(d_inp_list, d_start, d_end) == [2, 3]


def test_sub_edge() -> None:
    e_inp_list: list[int] = [1, 2, 3, 4, 5]
    e_start: int = 5
    e_end: int = 0
    """Test that sub returns an empty list when end is greater than start."""
    assert sub(e_inp_list, e_start, e_end) == []


def test_sub_mut() -> None:
    f_inp_list: list[int] = [1, 2, 3, 4, 5]
    f_start: int = 3
    f_end: int = 4
    """Test that sub does not mutate input list."""
    sub(f_inp_list, f_start, f_end)
    assert f_inp_list == [1, 2, 3, 4, 5]


def test_sub_start_range() -> None:
    g_inp_list: list[int] = [1, 2, 3, 4, 5]
    g_start: int = -3
    g_end: int = 10
    """Test that sub works when start input is less than 0."""
    assert sub(g_inp_list, g_start, g_end) == [1, 2, 3, 4, 5]


def test_sub_end_range() -> None:
    h_inp_list: list[int] = [1, 2, 3, 4, 5]
    h_start: int = 1
    h_end: int = 16
    """Test that sub works when end input is greater than length of list."""
    assert sub(h_inp_list, h_start, h_end) == [2, 3, 4, 5]


def test_add_at_index_use() -> None:
    i_list: list[int] = [1, 2, 4, 5]
    i_elem: int = 3
    i_ind: int = 2
    """Test that add_at_index works in a normal use case,
    and adds the specified element at the specified index."""
    add_at_index(i_list, i_elem, i_ind)
    assert i_list == [1, 2, 3, 4, 5]


def test_add_at_index_mut() -> None:
    j_list: list[int] = [1, 2, 3, 5]
    j_elem: int = 4
    j_ind: int = 3
    """Test that add_at_index modifies the input list."""
    add_at_index(j_list, j_elem, j_ind)
    assert j_list == [1, 2, 3, 4, 5]


def test_add_at_index_raise_indexerror() -> None:
    k_list: list[int] = [1, 2, 3, 4, 5]
    k_elem: int = 10
    k_ind: int = 10
    """Test that add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index(k_list, k_elem, k_ind)


def test_add_at_index_edge() -> None:
    l_list: list[int] = [0]
    l_elem: int = 1
    l_ind: int = 1
    """Test that add_at_index works for a list of 1 item."""
    add_at_index(l_list, l_elem, l_ind)
    assert l_list == [0, 1]
