"""EX07 - Dictionary Functions."""

__author__ = "730581165"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary and reverses the keys and values."""
    ret_dict: dict[str, str] = {}
    for elem in inp_dict:
        if inp_dict[elem] in ret_dict:
            raise KeyError("duplicate keys")
        else:
            ret_dict[inp_dict[elem]] = elem
    return ret_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Given a dictionary of names and colors and returns the color that appears most frequently."""
    color_dict: dict[str, int] = {}
    favorite_color: str = ""
    frequency: int = 0
    for elem in inp_dict:
        if inp_dict[elem] in color_dict:
            color_dict[inp_dict[elem]] += 1
        else:
            color_dict[inp_dict[elem]] = 1
    for elem in color_dict:
        if color_dict[elem] > frequency:
            frequency = color_dict[elem]
            favorite_color = elem
    return favorite_color
    

def count(inp_list: list[str]) -> dict[str, int]:
    """Given a list of strings and returns a dictionary of how frequently each string appeared."""
    ret_dict: dict[str, int] = {}
    for elem in inp_list:
        if elem in ret_dict:
            ret_dict[elem] += 1
        else:
            ret_dict[elem] = 1
    return ret_dict