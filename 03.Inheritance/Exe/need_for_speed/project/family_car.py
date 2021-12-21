from inheritance.Exe.need_for_speed.project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
