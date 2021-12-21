from abc import ABC, abstractmethod

from project.common.validator import Validator


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Fish name cannot be an empty string."
        Validator.raise_value_error_if_empty_string(value, error_message)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        error_message = "Fish species cannot be an empty string."
        Validator.raise_value_error_if_empty_string(value, error_message)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price cannot be equal to or below zero."
        Validator.raise_value_error_if_value_equal_or_below_zero(value, error_message)
        self.__price = value

    def eat(self):
        self.size += 5


