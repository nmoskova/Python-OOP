from abc import ABC, abstractmethod

from project.common.validator import Validator
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # represents the number of fish an aquarium can have
        self.decorations = []  # will contain all the decorations (objects)
        self.fish = []  # will contain all the fish (objects)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Aquarium name cannot be an empty string."
        Validator.raise_value_error_if_empty_string(value, error_message)

        self.__name = value

    def calculate_comfort(self):
        comfort_sum = sum([decoration.comfort for decoration in self.decorations])
        return comfort_sum

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ == FreshwaterFish.__name__ or \
            fish.__class__.__name__ == SaltwaterFish.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        result += f"Fish: {'none' if not self.fish else ' '.join([fish.name for fish in self.fish])}"
        result += "\n"
        result += f"Decorations: {len(self.decorations)}\n" \
                  f"Comfort: {self.calculate_comfort()}"

        return result




