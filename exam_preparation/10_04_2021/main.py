from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish

repo = DecorationRepository()
ornament = Ornament()
plant = Plant()
repo.add(ornament)
repo.find_by_type("Ornament")
freshwater = FreshwaterFish("freshy", "golden", 10)
print(freshwater.size)
fresh_aquarium = FreshwaterAquarium("Freshy")
salty_aquarium = SaltwaterAquarium("Salty")
print(fresh_aquarium.name)
fresh_aquarium.add_fish(freshwater)
print(fresh_aquarium.add_fish(freshwater))
fresh_aquarium.feed()
fresh_aquarium.add_decoration(ornament)
fresh_aquarium.add_decoration(plant)
print(fresh_aquarium)

print("-------------------------")

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "name"))
print(controller.add_aquarium("SaltwaterAquarium", "name_2"))
print(controller.aquariums)
print("-------------------------")
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Ornament"))
print("-------------------------")
print(controller.insert_decoration("name", "Ornament"))
print(controller.insert_decoration("name", "Ornament"))
print(controller.add_fish("name", "FreshwaterFish", "salsa", "species", 1000))
print(controller.add_fish("name", "FreshwaterFish", "sx", "species", 500))
print(controller.feed_fish("name"))
print("-------------------------")
print(controller.report())
print("-------------------------")
print(controller.calculate_value("name"))
print(controller.report())
print("-------------------------")
print(fresh_aquarium)





