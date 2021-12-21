from inheritance.Exe.zoo.project.animal import Animal


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)