"""unit tests for utils function for ex05"""

__author__ = "730668650"

from exercises.ex05.utils import only_evens, sub, add_at_index

# imports all functions

import pytest


def test_return_evens() -> None:
    """tests if only_evens returns only even numbers for only_evens() function"""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_mutation_only_evens() -> None:
    """checks that list isn't mutated for only_evens() function"""
    list0: list[int] = [6, 7, 8, 9, 10]
    only_evens(list0)
    assert list0 == [6, 7, 8, 9, 10]


def test_ec_evens() -> None:
    """checks that returns correct values for edge case for only_evens()"""
    assert only_evens([10000, -20, -19, -1, -2, 0, -15]) == [10000, -20, -2, 0]


def test_return_sub() -> None:
    """tests return list for sub() function"""
    assert sub([15, 20, 25, 30, 35], 2, 4) == [25, 30]


def test_mutation_sub() -> None:
    """checks that list isn't mutated for sub() function"""
    list1: list[int] = [5, 6, 1, 2, 3, 4]
    sub(list1, 3, 5)
    assert list1 == [5, 6, 1, 2, 3, 4]


def test_ec_sub() -> None:
    """checks that correct values are returned for edge case for sub()"""
    assert sub([-1083, 1874, 0, -18, 7, 1], -17, 197) == [-1083, 1874, 0, -18, 7, 1]


def test_return_add_idx() -> None:
    """checks that add_at_index() function has no return value"""
    assert add_at_index([9, 8, 7, 6, 5], 15, 3) == None


def test_mutate_add_idx() -> None:
    """checks that add_at_index() function mutates list correctly"""
    list2: list[int] = [10, 20, 40, 50]
    add_at_index(list2, 30, 2)
    assert list2 == [10, 20, 30, 40, 50]


def test_ec_add_idx() -> None:
    """checks that correct values are returned for edge case for add_at_index()"""
    list3: list[int] = [900, -1203, 57, 89, 0, -12]
    assert add_at_index(list3, -193, 4) == None
    assert list3 == [900, -1203, 57, 89, -193, 0, -12]


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index([50, 20, 30], 3, 7)
        # an IndexError is raised for the case when the add_at_index is given an
        # <index_to_insert_num>
        # that is greater than the length of our <list_object>
