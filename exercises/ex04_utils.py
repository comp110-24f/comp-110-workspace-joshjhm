"""EX04 - list Utility Functions"""

__author__ = "730668650"


def all(list0: list[int], int0: int) -> bool:
    """indicates if all ints in list are same as given int"""
    condition0: bool = False
    count_all: int = 0

    for element in list0:
        if element == int0:
            count_all = count_all + 1
    if len(list0) == count_all:
        condition0 = True
    if len(list0) == 0:
        condition0 = False
    return condition0
    # originally wrote to evaluate if !=
    # changed to ==


def max(list1: list[int]) -> int:
    """returns largest value in list"""
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")
    # forgot to add this in
    max_val: int = list1[0]
    for element in list1:
        if element > max_val:
            max_val = element
    return max_val


def is_equal(list2: list[int], list3: list[int]) -> bool:
    """checks if lists are equal"""

    condition1: bool = False
    equal_count: int = 0
    idx = 0
    if len(list2) != len(list3):
        return condition1
    # had written as assertion error
    # if lists aren't equal it's false
    for element in list2:
        if element == list3[idx]:
            equal_count = equal_count + 1
            idx = idx + 1
        else:
            idx = idx + 1
    # added idx to pull value from list3
    if len(list2) == equal_count:
        condition1 = True
    # removed useless code checking if both lists were empty
    return condition1


def extend(a: list[int], b: list[int]) -> None:
    """adds b list to end of a list"""
    for element in b:
        a.append(element)
    # worked 1st try
