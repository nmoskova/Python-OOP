from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.common.validator import Validator
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name cannot be empty string or white space!"
        Validator.raise_if_string_is_empty_or_whitespace(value, error_message)

        self.__name = value

    def add_food(self, food_type, name, price):
        error_message = f"{food_type} {name} is already in the menu!"
        Validator.validate_if_exist_by_name(self.food_menu, name, error_message)

        if food_type == Bread.__name__:
            self.food_menu.append(Bread(name, price))

        if food_type == Cake.__name__:
            self.food_menu.append(Cake(name, price))

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        error_message = f"{drink_type} {name} is already in the menu!"
        Validator.validate_if_exist_by_name(self.drinks_menu, name, error_message)

        if drink_type == Tea.__name__:
            self.drinks_menu.append(Tea(name, portion, brand))

        if drink_type == Water.__name__:
            self.drinks_menu.append(Water(name, portion, brand))

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        error_message = f"Table {table_number} is already in the bakery!"
        Validator.validate_table_number(self.tables_repository, table_number, error_message)

        if table_type == InsideTable.__name__:
            self.tables_repository.append(InsideTable(table_number, capacity))
        if table_type == OutsideTable.__name__:
            self.tables_repository.append(OutsideTable(table_number, capacity))

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_name):
        table = Validator.search_for_table_by_table_number(self.tables_repository, table_number)
        if not table:
            return f"Could not find table {table_number}"

        food_not_in_menu = []
        ordered_food = []
        for name in food_name:
            food = Validator.search_for_object_by_name(self.food_menu, name)
            if not food:
                food_not_in_menu.append(name)
                continue

            table.order_food(food)
            ordered_food.append(str(food))

        result = f"Table {table_number} ordered:\n"
        result += "\n".join(ordered_food)
        result += f"\n{self.name} does not have in the menu:\n"
        result += "\n".join(food_not_in_menu)

        return result

    def order_drink(self, table_number, *drinks_name):
        table = Validator.search_for_table_by_table_number(self.tables_repository, table_number)
        if not table:
            return f"Could not find table {table_number}"

        drink_not_in_menu = []
        ordered_drinks = []
        for name in drinks_name:
            drink = Validator.search_for_object_by_name(self.drinks_menu, name)
            if not drink:
                drink_not_in_menu.append(name)
                continue

            table.order_drink(drink)
            ordered_drinks.append(str(drink))

        result = f"Table {table_number} ordered:\n"
        result += "\n".join(ordered_drinks)
        result += f"\n{self.name} does not have in the menu:\n"
        result += "\n".join(drink_not_in_menu)

        return result

    def leave_table(self, table_number):
        table = Validator.search_for_table_by_table_number(self.tables_repository, table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n"\
            f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info()
                result += "\n"

        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"