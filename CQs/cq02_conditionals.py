"""Challenge Question 02"""

__author__ = "730668650"


def guess_a_number() -> None:
    """begins game of guessing secret number"""
    secret: int = 7
    x = int(input("Guess a number:"))
    """records the guess"""
    print("Your guess was " + str(x))
    # had trouble getting input function to work
    # didn't quite know how to use it so just experimented
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    # couldn't get if/else statements to work until attached to guess_a_number()


if __name__ == "__main__":
    guess_a_number()

# autograder found issue with fuction when it was separated
# combined all functions into guess_a_number()

# autograder determined the output for specific guess to be incorrect
# reordered print of guess to be before confirmation of guess
