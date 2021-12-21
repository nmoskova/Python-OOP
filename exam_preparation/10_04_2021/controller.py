from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.common.validator import Validator
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []  # will contain all aquariums (objects)

    def add_aquarium(self, aquarium_type, aquarium_name):
        aquarium = None
        if aquarium_type == FreshwaterAquarium.__name__:
            aquarium = FreshwaterAquarium(aquarium_name)
        if aquarium_type == SaltwaterAquarium.__name__:
            aquarium = SaltwaterAquarium(aquarium_name)

        if not aquarium:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        decoration = None
        if decoration_type == Ornament.__name__:
            decoration = Ornament()
        if decoration_type == Plant.__name__:
            decoration = Plant()

        if not decoration:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium = Validator.search_object_by_name(self.aquariums, aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        aquarium = Validator.search_object_by_name(self.aquariums, aquarium_name)
        if not aquarium:
            return None

        fish = None
        if fish_type == SaltwaterFish.__name__:
            fish = SaltwaterFish(fish_name, fish_species, price)
        if fish_type == FreshwaterFish.__name__:
            fish = FreshwaterFish(fish_name, fish_species, price)

        if not fish:
            return f"There isn't a fish of type {fish_type}."

        if (fish_type == "SaltwaterFish" and aquarium.__class__.__name__ == "FreshwaterAquarium") or\
                (fish_type == "FreshwaterFish" and aquarium.__class__.__name__ == "SaltwaterAquarium"):
            return "Water not suitable"

        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name):
        aquarium = Validator.search_object_by_name(self.aquariums, aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        # sum of all fish’s and decorations’ prices in the aquarium
        aquarium = Validator.search_object_by_name(self.aquariums, aquarium_name)
        total_price_fish = sum([f.price for f in aquarium.fish])
        total_price_decorations = sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {(total_price_fish + total_price_decorations):.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

