"""File to define Fish class."""

__author__ = "730776315"


class Fish:
    """Class for Fish, where each object has an age."""

    age: int

    def __init__(self):
        """New Fish with age of 0."""
        self.age = 0

    def one_day(self) -> None:
        """Simulate one day of life for the fish."""
        self.age += 1
        return None
