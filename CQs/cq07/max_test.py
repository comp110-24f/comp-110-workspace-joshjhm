"""cq07 unit tests for find_max function"""

__author__ = "730668650"

from CQs.cq07.find_max import find_and_remove_max


def test_exp_val() -> None:
    """checks if returns expected value (use case)"""
    exp_val: int = 3

    assert find_and_remove_max([3, 1, 2, 2, 1, 3]) == exp_val
    # checks that actual value of find_max function equals expected


def test_mutation() -> None:
    """checks if mutates correctly (use case)"""
    a: list[int] = [1, 2, 3]
    find_and_remove_max(a)
    assert a == [1, 2]


def test_return() -> None:
    """checks if returns expected value (edge case)"""
    exp_val: int = -62747166
    assert (
        find_and_remove_max([-17264718312, -62747166, -182756467187662535, -204393802])
        == exp_val
    )
