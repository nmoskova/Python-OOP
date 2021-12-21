from abc import ABC, abstractmethod


class Animal(ABC):

    def get_species(self):
        return self.__class__.__name__

    @abstractmethod
    def animal_sound(self):
        pass


class Cat(Animal):
    def animal_sound(self):
        return "meow"


class Dog(Animal):
    def animal_sound(self):
        return "woof - woof"


class Chicken(Animal):
    def animal_sound(self):
        return "coo- coo"


cat = Cat()
print(cat.get_species())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
