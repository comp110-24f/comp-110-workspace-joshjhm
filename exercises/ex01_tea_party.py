"""ex01_tea_party second exercise"""

__author__: str = "730668650"


def main_planner(guests: int) -> None:
    """entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # had trouble getting the first line of print code working "cozy tea part line",
    # changed guests to string
    # changed type of output for main_planner cost to str to add "$" to beginning
    # This caused it to look goofy but still runs the same
    # found out that I forgot to put "Tea Bags:, Treats:, Cost:""


def tea_bags(people: int) -> int:
    """total # of teabags needed based on # of people"""
    return int(people * 2)
    # forgot to add ":" to end of function definition
    # added int() function to make sure output was int


def treats(people: int) -> int:
    """total # of treats needed based on drinks drunk by guests"""
    return int((tea_bags(people=people)) * 1.5)
    # was returning value with a .0 at the end so added int() function to return line


def cost(tea_count: int, treat_count: int) -> float:
    """determines total cost of tea party"""
    return tea_count * 0.50 + treat_count * 0.75
    # was having trouble until I realized I wasn't supposed to use previous functions
    # in this function definition


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
