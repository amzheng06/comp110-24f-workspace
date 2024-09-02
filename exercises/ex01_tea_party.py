"""Calculates resources needed for a tea party of a certain number of people"""

__author__: str = "730776315"


def main_planner(guests: int) -> None:
    """Calls each function and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    # calls cost, where tea_count comes from the result of tea_bags as a
    # function of the value of guests, and treat_count comes from the result
    # of treats as a function of the value of guests
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes number of teabags needed based on number of guests"""
    return 2 * people


def treats(people: int) -> int:
    """Computes number of treats needed based on amount of tea needed"""
    # Calls tea_bags function with the input of people,
    # then multiplies the result of tea_bags with 1.5; returns as int type
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes cost of teabags and  treats combined"""
    return float(0.5 * tea_count + 0.75 * treat_count)


if __name__ == "__main__":
    # placed at end so that all variables are defined
    main_planner(guests=int(input("How many guests are attending your tea party?")))
