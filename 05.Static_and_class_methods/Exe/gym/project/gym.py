from static_and_class_methods_05.exe.gym.project.customer import Customer
from static_and_class_methods_05.exe.gym.project.equipment import Equipment
from static_and_class_methods_05.exe.gym.project.exercise_plan import ExercisePlan
from static_and_class_methods_05.exe.gym.project.subscription import Subscription
from static_and_class_methods_05.exe.gym.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return

        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return

        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return

        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return

        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return

        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        customer = self.__get_object_by_id(self.customers, subscription_id)
        trainer = self.__get_object_by_id(self.trainers, subscription_id)
        equipment = self.__get_object_by_id(self.equipment, subscription_id)
        plan = self.__get_object_by_id(self.plans, subscription_id)
        result = f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result

    @staticmethod
    def __get_object_by_id(objects, id):
        for object in objects:
            if object.id == id:
                return object
