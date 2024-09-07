"""Planning a cozy tea party!"""

__author__: str = "730739772"


def main_planner(guests: int) -> None:
    """Pulling everything together to print"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """We assume everyone will drink two cups of tea"""
    return people * 2


def treats(people: int) -> int:
    """We assume everyone will have 1.5 treats per tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Adding up total cost of treats and tea bags"""
    return float((tea_count * 0.50) + (treat_count * 0.75))


if __name__ == "__main__":
    """This allows us to run our function"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
