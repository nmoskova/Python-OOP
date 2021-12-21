from inheritance.Exe.shop.project.product import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name, 15)