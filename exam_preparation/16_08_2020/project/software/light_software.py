from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
        self.capacity_consumption = int(capacity_consumption + 0.5 * capacity_consumption)
        self.memory_consumption = int(memory_consumption - 0.5 * memory_consumption)

