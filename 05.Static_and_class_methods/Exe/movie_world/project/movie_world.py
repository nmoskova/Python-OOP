from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    @staticmethod
    def __get_obj_by_id(objects, id):
        for object in objects:
            if object.id == id:
                return object

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd.is_rented:
            return "DVD is already rented"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers_string = "\n".join([str(x) for x in self.customers])
        dvds_string = "\n".join([str(x) for x in self.dvds])
        result = customers_string + "\n" + dvds_string
        return result


