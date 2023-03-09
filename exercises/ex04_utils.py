"""EX04 - 'list' Utility Functions."""

__author__ = "730581165"


def all(list_of_ints: list[int], indicated_number: int) -> bool:
    """Given a list of ints and an int, function will return a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(list_of_ints) == 0:
        return False
    i: int = 0
    while i < len(list_of_ints):
        if list_of_ints[i] == indicated_number:  # number in list matches indicated integer
            i += 1
        else:  # number in list doesn't match indicated integer
            return False
    return True


def max(input: list[int]) -> int:
    """Function is given a list of integers and returns the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = 0
    while i < len(input):
        if i == 0:  # The first value in the list will automatically be the max value
            max = input[i]
        else:
            if input[i] > max:
                max = input[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of integer values that returns True if every element at every index is equal in both lists."""
    i: int = 0
    if len(list1) != len(list2):
        return False  # lists are not the same length
    while i < len(list1):
        if list1[i] == list2[i]:
            i += 1
        else:
            return False
    return True