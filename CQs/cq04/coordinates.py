"""Coordinates for cq04"""

__author__ = "730668650"


def get_coords(xs: str, ys: str) -> None:
    """prints formatted pairs"""
    a: int = 0
    b: int = 0
    while len(xs) > a:
        while len(ys) > b:
            print("(" + xs[a] + ", " + ys[b] + ")")
            b = b + 1
        a = a + 1
        b = 0
    # realized I originally only wrote it to work with len(xs) = 2
    # wrote while len(xs) < a instead of > a
    # I wrote it to work with an if/else statement but had to change it to while loop
    # bc the assignment wanted me to
    # (it's slightly more efficient with a nested while loop I believe)
    # 1 less line of code
