from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []  # contain all software's components installed on that hardware

    def install(self, software: Software):
        if software.capacity_consumption > self.capacity and software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        return

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def return_software_memory(self):
        software_memory_consumption = sum([s.memory_consumption for s in self.software_components])
        return software_memory_consumption

    def return_software_capacity(self):
        software_capacity_consumption = sum([s.capacity_consumption for s in self.software_components])
        return software_capacity_consumption

    def __repr__(self):
        result = f"name = {self.name}\n"\
             f"hardware_type = {self.hardware_type}\n"\
             f"capacity = {self.capacity}\n"\
             f"memory = {self.memory}\n"\
             f"software_components = {self.software_components}\n"

        return result.strip()
