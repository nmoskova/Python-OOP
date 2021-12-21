class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, liquid_ml):
        if self.content + liquid_ml > Glass.capacity:
            return f"Cannot add {liquid_ml} ml"

        self.content += liquid_ml
        return f"Glass filled with {liquid_ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = self.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
