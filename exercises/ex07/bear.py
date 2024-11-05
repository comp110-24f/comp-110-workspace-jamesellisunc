"""File to define Bear class."""


class Bear:
    """Defines the Bear object."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes attributes."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Models the life of each bear after 1 day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Models a bear's hunger as they eat fish."""
        self.hunger_score += num_fish  # hunger increases by total fish eaten
        return None
