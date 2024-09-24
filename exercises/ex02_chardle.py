"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730668650"


def main() -> None:
    """entrypoint of program"""

    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """input word for chardle"""
    word: str = input("Enter a 5 character word")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word

    # reconfigured so asks if == 5 instead of > or <
    # exit statement was put after return so it didn't work


def input_letter() -> str:
    """input single letter for chardle"""
    letter: str = input("Enter a single character:")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter
    # reconfigured so it checked == instead of < or >
    # exit statement was put after return so it didn't work


def contains_char(word, letter) -> None:
    """checks if word contains letter"""
    char: int = 0
    char2: int = 0
    print("Searching for " + letter + " in " + word)
    if word[char] == letter:
        print(letter + " found at index 1")
        char = char + 1
    else:
        char = char + 1

    if word[char] == letter:
        print(letter + " found at index 2")
        char = char + 1
    else:
        char = char + 1

    if word[char] == letter:
        print(letter + " found at index 3")
        char = char + 1
    else:
        char = char + 1

    if word[char] == letter:
        print(letter + " found at index 4")
        char = char + 1
    else:
        char = char + 1

    if word[char] == letter:
        print(letter + " found at index 5")
        char = char + 1
    else:
        char = char + 1
    # forgot second = for word[char] == letter:

    count: int = 0
    if word[char2] == letter:
        count = count + 1
        char2 = char2 + 1
    else:
        char2 = char2 + 1

    if word[char2] == letter:
        count = count + 1
        char2 = char2 + 1
    else:
        char2 = char2 + 1

    if word[char2] == letter:
        count = count + 1
        char2 = char2 + 1
    else:
        char2 = char2 + 1

    if word[char2] == letter:
        count = count + 1
        char2 = char2 + 1
    else:
        char2 = char2 + 1

    if word[char2] == letter:
        count = count + 1
        char2 = char2 + 1
    else:
        char2 = char2 + 1
    print(str(count) + " instances of " + letter + " found in " + word)
    # accidentally put char 2 instead of count for print statment
    # print statement got angry at me, wouldn't work bc forgot a + in front of word
    # was accidentally looping function 2x due to definition having word = input_word()


if __name__ == "__main__":
    main()
