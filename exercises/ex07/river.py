"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730776315"


class River:
    """Simulates how the river changes when Bear and Fish act."""

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
        """Checks ages and removes bears and fish that are too old."""
        # initialize copy of Fish list
        live_fish: list[Fish] = []
        # removing Bears who are too old
        live_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                live_bears.append(bear)
        # removing Fish who are too old
        for fish in self.fish:
            if fish.age <= 3:
                live_fish.append(fish)

        self.fish = live_fish
        self.bears = live_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes specified number of fish."""
        for i in range(0, amount):
            self.fish.pop(i)

    def bears_eating(self):
        """Simulates change in Fish when Bear eats."""
        for item in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                item.eat(3)
        return None

    def check_hunger(self):
        """Checks which Bears have starved."""
        # creates a copy of self.bears to be modified
        live_bears: list[Bear] = []
        for i in range(0, len(self.bears)):
            item_b: Bear = self.bears[i]
            if item_b.hunger_score >= 0:
                live_bears.append(item_b)
        self.bears = live_bears
        return None

    def repopulate_fish(self):
        """Simulates repopulation of Fish."""
        # create a copy of self.fish to be modified
        live_fish: list[Fish] = []
        for fish in self.fish:
            live_fish.append(fish)
        # adds four new fish for every two bears
        for i in range(0, len(self.fish) // 2):
            live_fish.append(Fish())
            live_fish.append(Fish())
            live_fish.append(Fish())
            live_fish.append(Fish())
            i += 1
        self.fish = live_fish
        return None

    def repopulate_bears(self):
        """Simulates repopulation of Bears."""
        # create a copy of self.bears to be modified
        live_bears: list[Bear] = []
        for bear in self.bears:
            live_bears.append(bear)
        # adds one new bear for every two bears
        for i in range(0, len(self.bears) // 2):
            live_bears.append(Bear())
            i += 1
        self.bears = live_bears
        return None

    def view_river(self) -> None:
        """Prints current stats of the river."""
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

    def one_river_week(self) -> None:
        """Simulates the passing of one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
