"""Concatenation for cq04"""

__author__ = "730668650"


def main() -> None:
    """runs concat if concatenation is main file"""

    print(concat(word1, word2))


def concat(str1: str, str2: str) -> str:
    """returns concat of two strings"""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    main()
