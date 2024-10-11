"""Summing the elements of a list using different loops"""

__author__ = "730668650"


def w_sum(vals: list[float]) -> float:
    """returns sum of all elements"""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx = idx + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """returns sum of all elements"""
    sum: float = 0.0
    for element in vals:
        sum = sum + element
    return sum


def f_range_sum(vals: list[float]) -> float:
    """returns sum of all elements"""
    sum: float = 0.0
    idx: int = 0
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]
        idx = idx + 1
    # rewrote for statement to iterate over entire list
    return sum
