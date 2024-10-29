"""cq07 find_and_return_max function"""

__author__ = "730668650"


def find_and_remove_max(list0: list[int]) -> int:
    """returns largest value and removes it from list"""

    if len(list0) == 0:
        max_val = -1
    # empty list returns -1 and exits without modulation
    else:
        max_val: int = list0[0]
        for element in list0:
            if element > max_val:
                max_val = element
            # finds max element
        idx: int = 0
        while idx < len(list0):
            if list0[idx] == max_val:
                list0.pop(idx)
            else:
                idx = idx + 1
        # removes all instances of max element from list
    return max_val
