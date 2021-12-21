class Child:
    def __init__(self, food_cost, *toys_cost):
        # required money for a day
        self.cost = food_cost + sum(toys_cost)