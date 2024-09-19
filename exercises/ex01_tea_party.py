"""Planning a cozy tea party!"""

__author__: str = "730739772"


def main_planner(guests: int) -> None:
    """Pulling everything together to print"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People"
    )  # guests is an int so we have to convert to a string
    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # convert the call of  tea_bags to string from an int
    print(
        "Treats: " + str(treats(guests))
    )  # convert call of treats to string from an int
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # tea_bags and treats are inputted as parameters of cost
    # must convert cost to string from float


def tea_bags(people: int) -> int:
    """We assume everyone will drink two cups of tea"""
    return people * 2  # tea_bags is given the value 2 * total people


def treats(people: int) -> int:
    """We assume everyone will have 1.5 treats per tea"""
    return int(
        tea_bags(people=people) * 1.5
    )  # multiply the amount of tea_bags by 1.5 to find treats


def cost(tea_count: int, treat_count: int) -> float:
    """Adding up total cost of treats and tea bags"""
    return float(  # must be float bc costs end in decimals
        (tea_count * 0.50) + (treat_count * 0.75)
    )  # multiplies variables tea_count and treat_count by their respective costs


if __name__ == "__main__":
    """This allows us to run our function"""
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # guest must be an int
