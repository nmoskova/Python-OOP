class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        """
       - If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list,
        reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
       - If you have the capacity, but no budget, return "Not enough budget"
       - In any other case, you do not have space, and you should return "Not enough space for animal"
        """
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        """
           - If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet),
            add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
           -Otherwise, return "Not enough space for worker"
        """
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        """
            - If there is a worker with that name in the workers' list,
             remove him and return "{worker_name} fired successfully"
            - Otherwise, return "There is no {worker_name} in the zoo"
        """
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        """
            - If you have enough budget to pay the workers (sum their salaries) pay them
             and return "You payed your workers. They are happy. Budget left: {left_budget}"
            - Otherwise, return "You have no budget to pay your workers. They are unhappy"
        """
        salaries_sum = sum([w.salary for w in self.workers])
        if salaries_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        """
            - If you have enough budget to take care of the animals, reduce the budget
             and return "You tended all the animals. They are happy. Budget left: {left_budget}"
            - Otherwise, return "You have no budget to tend the animals. They are unhappy."
        """
        tend_animals_total = sum([a.MONEY_FOR_CARE for a in self.animals])
        if tend_animals_total > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= tend_animals_total
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        """
            - Increase the budget with the given amount of profit
        """
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__get_status_by_type("Lion", self.animals)
        result += self.__get_status_by_type("Tiger", self.animals)
        result += self.__get_status_by_type("Cheetah", self.animals)

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__get_status_by_type("Keeper", self.workers)
        result += self.__get_status_by_type("Caretaker", self.workers)
        result += self.__get_status_by_type("Vet", self.workers)

        return result.strip()

    def __get_status_by_type(self, object_type, objects_list):
        objects_type = [str(x) for x in objects_list if x.__class__.__name__ == object_type]
        result = f"----- {len(objects_type)} {object_type}s:\n"
        for animal in objects_type:
            result += animal
            result += "\n"

        return result
