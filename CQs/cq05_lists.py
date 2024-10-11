"""Mutating functions."""

__author__ = "730668650"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], num: int) -> None:
    """manually appends list"""
    a.append(num)


# corrected function definition
# (I wrote it by repeating the function in the definition originally idk y)


def double(b: list[int]) -> None:
    """doubles all values of a list"""
    idx: int = 0
    while idx < len(b):
        b[idx] = b[idx] * 2
        idx = idx + 1
    # forgot to add idx = idx + 1


double(list_2)
print(list_1)
print(list_2)
