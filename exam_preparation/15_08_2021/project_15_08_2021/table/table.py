from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.common.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []   # every food order made from the table
        self.drink_orders = []  # every drink order made from the table
        self.number_of_people = 0  # count of people who sit at the table
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        error_message = "Capacity has to be greater than 0!"
        Validator.raise_if_value_equal_or_less_than_zero(value, error_message)

        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = sum([food.price for food in self.food_orders])
        drinks_bill = sum([drink.price for drink in self.drink_orders])
        return food_bill + drinks_bill

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"

        return None


