"""Challenge Question 00 mimic function"""

__author__ = "730668650"


def mimic(message: str) -> str:
    """Returns input as output"""
    return message


def main() -> None:
    """prints result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
