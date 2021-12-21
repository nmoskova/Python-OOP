from project.common.validator import Validator
from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        min_number_table = 51
        max_number_table = 100
        error_message = "Outside table's number must be between 51 and 100 inclusive!"
        Validator.raise_if_table_number_not_valid(value, min_number_table, max_number_table, error_message)

        self.__table_number = value
