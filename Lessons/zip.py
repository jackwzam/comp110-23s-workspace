"""Challenge Question 04 - Dict Function Writing."""

__author__ = "730581165"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Given a list of strings and a list of integers and returns a dictionary of string keys and integer values."""
    output: dict[str, int] = {}
    if len(list1) != len(list2):
        return output
    else:
        i: int = 0
        while i < len(list1):
            output[list1[i]] = list2[i]
            i += 1
        return output
