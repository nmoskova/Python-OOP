from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    """•	family_name: str – passed upon initialization
•	budget: float – passed upon initialization
•	members_count: int – passed upon initialization
•	children: list – an empty list that will contain all kids in that room (objects)
•	expenses – 0 by default. If it is set to a negative number, raise ValueError with the message "Expenses cannot be negative"
"""
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_el in args:
            for el in list_el:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                else:
                    total_expenses += el.cost * 30
        self.expenses = total_expenses


