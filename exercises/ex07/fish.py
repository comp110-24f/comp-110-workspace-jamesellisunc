"""File to define Fish class."""


class Fish:
    """Defines the Fish object."""

    age: int

    def __init__(self):
        """Initializes attributes of Fish."""
        self.age = 0
        return None

    def one_day(self):
        """Models the life of a fish after a single day."""
        self.age += 1
        return None
