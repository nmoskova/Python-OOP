class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        res = Equipment.id
        Equipment.id += 1
        return res

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


# eq1 = Equipment("jacket")
# eq2 = Equipment("f=dress")
# print(eq1)
# print(eq2)