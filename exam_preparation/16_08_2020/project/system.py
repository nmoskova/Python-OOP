from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []  # storing all the hardware components
    _software = []  # storing all the software components

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.search_for_object_by_name(System._hardware, hardware_name)

        if not hardware:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.search_for_object_by_name(System._hardware, hardware_name)

        if not hardware:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.search_for_object_by_name(System._hardware, hardware_name)
        software = System.search_for_object_by_name(System._software, software_name)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        hardware_components = len(System._hardware)
        software_components = sum([len(h.software_components) for h in System._hardware])

        result = "System Analysis\n"\
                    f"Hardware Components: {hardware_components}\n"\
                    f"Software Components: {software_components}\n"

        total_memory_software = 0
        total_memory_hardware = 0
        total_capacity_software = 0
        total_capacity_hardware = 0

        for hardware in System._hardware:
            total_memory_hardware += hardware.memory
            total_capacity_hardware += hardware.capacity

            for software in hardware.software_components:
                total_memory_software += software.memory_consumption
                total_capacity_software += software.capacity_consumption

        result += f"Total Operational Memory: {total_memory_software} / {total_memory_hardware}\n"
        result += f"Total Capacity Taken: {total_capacity_software} / {total_capacity_hardware}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {len([s for s in hardware.software_components if s.software_type == 'Express'])}\n"
            result += f"Light Software Components: {len([s for s in hardware.software_components if s.software_type == 'Light'])}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])} / {hardware.memory}\n"
            result += f"Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            software_components_str = ", ".join([s.name for s in hardware.software_components])
            result += f"Software Components: {'None' if len(hardware.software_components) == 0 else software_components_str}\n"

        return result.strip()

    @staticmethod
    def search_for_object_by_name(objects_repo, name):
        for object in objects_repo:
            if object.name == name:
                return object


