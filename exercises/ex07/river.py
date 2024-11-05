"""File to define River class."""

__author__ = "730739772"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines the river object and models a river population."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Create new lists to store the suriving animals."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []

        for fish in self.fish:  # loop through the list of fishes
            if fish.age <= 3:
                surviving_fish.append(fish)

        for bears in self.bears:  # loop through the list of fishes
            if bears.age <= 5:
                surviving_bears.append(bears)

        self.fish = surviving_fish  # gets rid of fish that are too old
        self.bears = surviving_bears  # gets rid of bears that are too old
        return None

    def bears_eating(self):
        """Bears will eat if there are at least 5 fish."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                bears.eat(3)  # increases bears hunger by 3
                self.remove_fish(3)  # removes 3 fish from the river
        return None

    def check_hunger(self):
        """Checks hunger level of bears and removes starving bears."""
        full_bears: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                full_bears.append(bears)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        """Models reproduction of fish."""
        couples = (len(self.fish) // 2) * 4  # how many multiples of 2 rounded down *4

        for babies in range(0, couples):
            self.fish.append(Fish())  # adds new fish object to the list
        return None

    def repopulate_bears(self):
        """Models reproduction of bears."""
        couples = len(self.bears) // 2  # how many multiples of 2 rounded down

        for babies in range(0, couples):
            self.bears.append(Bear())  # adds a new bear object to the list

        return None

    def remove_fish(self, amount: int):
        """Directly removes fish from the river."""
        for fish in range(0, amount):  # loops {amount} number of times
            if len(self.fish) > 0:
                self.fish.pop(0)  # removes the first fish in the river
        return None

    def view_river(self):
        """Allows you to view the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week/7 days in the river."""
        while self.day < 7:
            self.one_river_day()
