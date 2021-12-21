from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", capacity, memory)

        self.capacity = int(0.25 * capacity)
        self.memory = int(0.75 * memory + memory)
