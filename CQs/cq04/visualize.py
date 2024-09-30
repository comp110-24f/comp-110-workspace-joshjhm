"""Visualize for cq04"""

__author__ = "730668650"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# could not get it to import unless I took cq04 out of the CQs folder
# after doing that and moving it back into the CQs folder it magically worked

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
