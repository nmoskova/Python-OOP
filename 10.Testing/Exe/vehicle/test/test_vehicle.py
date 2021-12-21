from unittest import TestCase, main

from testing_10.exe.vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        fuel = 50
        horse_power = 100
        self.vehicle = Vehicle(fuel, horse_power)

    def test_vehicle_initialization(self):
        fuel = 50
        horse_power = 100
        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_drive_when_not_enough_fuel_raises(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(exc.exception))

    def test_drive_should_decrease_fuel(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)
        expected = 0
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_over_capacity_raises_error(self):
        fuel_to_refill = (self.vehicle.capacity - self.vehicle.fuel) + 1
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(fuel_to_refill)

        self.assertEqual("Too much fuel", str(exc.exception))

    def test_refuel_should_increase_fuel(self):
        fuel_to_refill = (self.vehicle.capacity - self.vehicle.fuel)
        self.vehicle.refuel(fuel_to_refill)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)

    def test_str_should_return_correct_string(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = self.vehicle.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
