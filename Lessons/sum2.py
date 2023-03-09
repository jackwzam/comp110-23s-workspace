
def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    for elem in range(0, len(xs)):
        sum_total += xs[elem]
    return sum_total