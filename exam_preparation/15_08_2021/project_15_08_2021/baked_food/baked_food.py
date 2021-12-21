from abc import ABC, abstractmethod

from project.common.validator import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion  # represents the size of the baked food in grams
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name cannot be empty string or white space!"
        Validator.raise_if_string_is_empty_or_whitespace(value, error_message)

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price cannot be less than or equal to zero!"
        Validator.raise_if_value_equal_or_less_than_zero(value, error_message)

        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
