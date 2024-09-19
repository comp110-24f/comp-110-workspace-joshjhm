"""Challenge Question 03"""

__author__ = "730668650"


def num_instances(phrase=str, search_char=str) -> int:
    """returns # of times a character occurs in a string"""
    count: int = 0
    index: int = 0
    while index < len(phrase):

        if search_char == phrase[index]:
            count = count + 1
            index = index + 1

        else:
            index = index + 1

    return print(count)


# trouble figuring out syntax for while statement
# added index = index + 1 to if statement to prevent infinite loop
