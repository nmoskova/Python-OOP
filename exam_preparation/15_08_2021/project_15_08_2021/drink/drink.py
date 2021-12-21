from abc import ABC, abstractmethod

from project.common.validator import Validator


class Drink(ABC):
    @abstractmethod
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name cannot be empty string or white space!"
        Validator.raise_if_string_is_empty_or_whitespace(value, error_message)

        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        error_message = "Portion cannot be less than or equal to zero!"
        Validator.raise_if_value_equal_or_less_than_zero(value, error_message)

        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        error_message = "Brand cannot be empty string or white space!"
        Validator.raise_if_string_is_empty_or_whitespace(value, error_message)

        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
