"""Unit Tests for Dictionary Functions."""

__author__ = "730581165"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_1() -> None:
    """Tests that given an empty dictionary, returns an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_2() -> None:
    """Tests that given a dictionary with three indexes, returns a new dictionary with reversed keys and values."""
    test_dict: dict[str, str] = {"b": "a", "d" : "c", "f": "e"}
    assert invert(test_dict) == {"a": "b", "c" : "d", "e": "f"}


def test_invert_3() -> None:
    """Tests that given a dictionary with number as keys and items as values, returns a dictionary with items as keys and numbers as values."""
    test_dict: dict[str, str] = {"7": "apples", "12" : "eggs"}
    assert invert(test_dict) == {"apples": "7", "eggs" : "12"}


def test_favorite_color_1() -> None:
    """Tests that given an empty dictionary, returns a string of no value."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_2() -> None:
    """Tests that given a dictionary with a most frequent color, returns the most frequent color."""
    test_dict: dict[str, str] = {"Josh": "yellow", "Earl": "blue", "Jordan": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_3() -> None:
    """Tests that given a dictionar with no most frequent color, returns the first color."""
    test_dict: dict[str, str] = {"Ernest": "yellow", "Joe": "blue", "John": "red"}
    assert favorite_color(test_dict) == "yellow"


def test_count_1() -> None:
    """Tests that given an empty list, returns an empty dictionary."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_2() -> None:
    """Tests that given a list of the same item, returns a dictionary with one key and a value of how many times that item was in the list."""
    test_list: list[str] = ["apple", "apple", "apple", "apple", "apple"]
    assert count(test_list) == {"apple": 5}


def test_count_3() -> None:
    """Tests that given a list of several items, returns a dictionary with items as the keys and values of the frequency of that item in the list."""
    test_list: list[str] = ["ball", "piano", "table", "ball"]
    assert count(test_list) == {"ball": 2, "piano": 1, "table": 1}