"""Recreation of the game wordle"""

__author__ = "730668650"


WHITE_BOX: str = "\U00002B1C"

GREEN_BOX: str = "\U0001F7E9"

YELLOW_BOX: str = "\U0001F7E8"

# constants (I made them globals just to be safe)


# moved variables to be global


def input_guess(len_word: int) -> str:
    """input word for wordle"""

    word = input(f"Enter a {len_word} character word:")

    while len(word) != len_word:

        word = input(f"That wasn't {len_word} chars! Try again:")

    return word

    # added word = bc value of word was permanently set to 5

    # left exit() in (idk why it was here)


def contains_char(secret_word0: str, char_guess: str) -> bool:
    """checks for individual characters"""

    assert len(char_guess) == 1

    count0: int = 0

    contains: bool = False

    while count0 < len(secret_word0):

        if secret_word0[count0] == char_guess:

            contains = True

        count0 = count0 + 1

    return contains

    # I don't understand booleans

    # figured it out (set variable type to bool)

    # I was having an error due to changing parameter names


def emojified(user_guess: str, secret_word1: str) -> str:
    """returns comparison of secret word to user's guess as emojis"""

    assert len(user_guess) == len(secret_word1)

    count1: int = 0

    compare: str = ""

    while count1 < len(user_guess):

        if secret_word1[count1] == user_guess[count1]:

            compare = compare + GREEN_BOX

        elif (
            contains_char(secret_word0=secret_word1, char_guess=user_guess[count1])
            == True
        ):

            temp_count: int = 0

            char_count: int = 0

            total_char: int = 0

            while temp_count < len(user_guess):

                if secret_word1[count1] == user_guess[temp_count]:

                    total_char = total_char + 1

                    temp_count = temp_count + 1

                else:

                    temp_count = temp_count + 1

            temp_count = 0

            while temp_count <= count1:

                if secret_word1[count1] == user_guess[temp_count]:

                    char_count = char_count + 1

                    temp_count = temp_count + 1

                else:

                    temp_count = temp_count + 1

            if char_count <= total_char:

                compare = compare + YELLOW_BOX

            else:

                compare = compare + WHITE_BOX

            temp_count = 0

            char_count = 0

            total_char = 0

            # This part is to account for repeat letters

            # I assume there's probably a more efficient way to check for repeat letters

            # didn't work, trying to find issue

            # variables for secret_word1[count1] & user_guess[temp_count] were swapped

            # left count1 = count1 + 1 in at end of code line

        else:

            compare = compare + WHITE_BOX

        count1 = count1 + 1

    return compare

    # took about 40 minutes to realize I put char_guess = secret_word1[count1]

    # This resulted in it always resulting in an output of all yellow (if chars were

    # wrong)

    # if there are multiple of the same letter in the wrong place causes extra yellow

    # rearranged code, making it first check if the letter was at that index


def main(secret: str) -> None:
    """entrypoint of program and game loop"""

    count: int = 0

    secret_word_len: int = len(secret)

    game_end: bool = False

    while game_end == False:

        print(f"=== Turn {count+1}/6 ===")

        guess: str = input_guess(len_word=secret_word_len)

        while len(guess) != secret_word_len:

            guess = input(f"That wasn't {secret_word_len} chars! Try again:")

        if len(guess) == secret_word_len:

            print(emojified(user_guess=guess, secret_word1=secret))

            # added print() so it gives emojis

            count = count + 1

        if secret == guess:

            print(f"You won in {count}/6 turns!")
            game_end = True
        if count > 5:
            print("X/6 - Sorry, try again tomorrow!")
            game_end = True

    # Had to put input_guess() function into main()
    # changed while statement to bool so I could end game w/o forced exit


if __name__ == "__main__":

    main(secret="codes")
