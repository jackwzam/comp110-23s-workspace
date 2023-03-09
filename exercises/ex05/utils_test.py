"""Unit Tests for Utils."""

__author__ = "730581165"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens_1() -> None:
    assert only_evens([]) == []

def test_only_evens_2() -> None:
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

def test_only_evens_3() -> None:
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]

def test_sub_1() -> None:
    assert sub([]) == []

def test_sub_2() -> None:
    test_list: list[int] = [1, 2, 3, 4]
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == [2, 3]

def test_sub_3() -> None:
    test_list: list[int] = [1, 2, 3, 4]
    start: int = -1
    end: int = 5
    assert sub(test_list, start, end) == [1, 2, 3, 4]

def test_concat_1() -> None:
    test_list_1: list[int] = []
    test_list_2: list[int] = []
    assert concat(test_list_1, test_list_2) == []

def test_concat_2() -> None:
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6]

def test_concat_3() -> None:
    test_list_1: list[int] = [2]
    test_list_2: list[int] = [-1, 7]
    assert concat(test_list_1, test_list_2) == [2, -1, 7]
