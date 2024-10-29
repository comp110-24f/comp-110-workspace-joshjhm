"""contains utils function for ex05"""

__author__ = "730668650"


def only_evens(a: list[int]) -> list[int]:
    """returns only even vals from list"""
    a0: list[int] = []
    # return value
    idx: int = 0
    while idx < len(a):
        if a[idx] % 2 == 0:
            a0.append(a[idx])
        idx = idx + 1
        # adds even numbers to list
    return a0


def sub(b: list[int], s_idx, e_idx) -> list[int]:
    """generates list b/w start idx and end idx (not inclusive)"""
    b0: list[int] = []

    # return value
    idx: int = s_idx
    end: int = e_idx
    if len(b) == 0:
        return b0
    # accounts for if list is empty
    else:
        if s_idx < 0:
            idx = 0
        # accounts for negative numbers
        # consequently also causes empty list to return when e_idx < 0
        if e_idx > len(b):
            end = len(b)
        # accounts for e_idx greater than list

        while idx < end:
            b0.append(b[idx])
            idx = idx + 1
        # adds all values from s_idx to e_idx (not inclusive)
    return b0


def add_at_index(c: list[int], add: int, at_idx: int) -> None:
    """adds value to list at idx"""
    # recreates entire list
    c0: list[int] = []
    idx: int = 0
    added: bool = False

    if at_idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    if at_idx > len(c):
        raise IndexError("Index is out of bounds for the input list")
    # raises error if at_idx is out of range
    while len(c0) <= len(c):
        if idx == at_idx:
            if added == False:
                c0.append(add)
                added = True
            # appends new int at_idx
            else:
                c0.append(c[idx])
                idx = idx + 1
            # appends old int at idx after new int
        else:
            c0.append(c[idx])
            idx = idx + 1
        # appends list at idx

    while len(c) > 0:
        c.pop(0)
    # deletes original list to be recreated
    idx0: int = 0
    while len(c) < len(c0):
        c.append(c0[idx0])
        idx0 = idx0 + 1
    # recreates original list as temporary list
    # I couldn't figure out how to insert value so I deleted and remade original list
