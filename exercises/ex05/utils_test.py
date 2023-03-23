"""Unit Tests for Utils."""

__author__ = "730581165"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_1() -> None:
    """Tests what a empty list should return."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_2() -> None:
    """Tests that only even numbers are returned."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_only_evens_3() -> None:
    """Tests that a list full of even numbers is completely returned."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_sub_1() -> None:
    """Tests that an empty list returns an empty list."""
    test_list: list[int] = []
    start: int = 1
    end: int = 2
    assert sub(test_list, start, end) == []


def test_sub_2() -> None:
    """Tests that the starting index is inclusive and the end index is exclusive for the modified list."""
    test_list: list[int] = [1, 2, 3, 4]
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == [2, 3]


def test_sub_3() -> None:
    """Tests that the start and end indexes can be less than and greater than the length of the list and the whole list is returned."""
    test_list: list[int] = [1, 2, 3, 4]
    start: int = -1
    end: int = 5
    assert sub(test_list, start, end) == [1, 2, 3, 4]


def test_concat_1() -> None:
    """Tests that two empty lists return an empty list."""
    test_list_1: list[int] = []
    test_list_2: list[int] = []
    assert concat(test_list_1, test_list_2) == []


def test_concat_2() -> None:
    """Tests that the two lists are combined in order of first list then second list."""
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_3() -> None:
    """Tests that two lists of different lengths are combined in order of first list then second list."""
    test_list_1: list[int] = [2]
    test_list_2: list[int] = [-1, 7]
    assert concat(test_list_1, test_list_2) == [2, -1, 7]
