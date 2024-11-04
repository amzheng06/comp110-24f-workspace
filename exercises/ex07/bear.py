"""File to define Bear class."""

__author__ = "730776315"


class Bear:
    """Class for Bear, where each object has an age and a hunger score."""

    age: int
    hunger_score: int

    def __init__(self):
        """New Bear with age of 0 and hunger score of 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulate one day of life for the bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Simulates the bear eating one fish."""
        self.hunger_score += num_fish
        return None
