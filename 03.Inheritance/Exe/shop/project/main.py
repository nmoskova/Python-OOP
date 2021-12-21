from inheritance.Exe.shop.project.drink import Drink
from inheritance.Exe.shop.project.food import Food
from inheritance.Exe.shop.project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
