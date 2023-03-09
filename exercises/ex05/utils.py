"""EX05 - 'list' Utility Functions."""

__author__ = "730581165"


def only_evens(list_of_ints: list[int]) -> list[int]:
    """Given a list of integers, a new list containing only the even elements is returned."""
    even_list: list[int] = []
    for elem in list_of_ints:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, returns a list of all the elements in the first list followed by all the elements in the second list."""
    total_list: list[int] = []
    for elem in list1:
        total_list.append(elem)
    for elem in list2:
        total_list.append(elem)
    return total_list


def sub(original_list: list[int], start: int, end: int) -> list[int]:
    """Given a list, start index, and end index, returns a sub list of the original list between the two indexes."""
    sub_list: list[int] = []
    if len(original_list) == 0 or start >= len(original_list) or end <= 0:
        return sub_list
    if start < 0:
        start = 0
    if end > len(original_list):
        end = len(original_list)
    while start < end:
        sub_list.append(original_list[start])
        start += 1
    return sub_list
    # for elem in range(start + 1, end + 1):
    #     sub_list.append(elem)
    # return sub_list