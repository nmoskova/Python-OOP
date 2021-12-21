class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


nat = Person("Natalia", 31)
print(nat.get_name())
print(nat.get_age())
print(nat.__dict__)
