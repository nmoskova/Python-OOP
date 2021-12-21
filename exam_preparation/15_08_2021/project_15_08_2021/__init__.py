from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery


bakery = Bakery("Bakery")
print(bakery.add_food("Bread", "bread", 1))
print(bakery.add_food("Cake", "cake", 2))
print(bakery.add_drink("Tea", "tea", 200, "earl_grey"))
print(bakery.add_drink("Water", "water", 100, "Bankya"))
print(bakery.add_table("InsideTable", 50, 10))
print(bakery.add_table("OutsideTable", 100, 9))
print(bakery.reserve_table(10))
print(bakery.order_food(50, "bread", "cake", "sweets"))
