class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        res = Customer.id
        Customer.id += 1
        return res

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# c1 = Customer("Pesho", "adres", "email")
# c2 = Customer("Pesho2", "adres1", "email1")
# print(c1.id)
# print(c2.id)
# print(c1)