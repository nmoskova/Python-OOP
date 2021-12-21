from project.pet_shop import PetShop


from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.name = "Name"
        self.pet_shop = PetShop(self.name)
        self.food_name = "food"
        self.quantity = 100
        self.pet_name = "pet_name"

    def test_pet_shop_initialisation(self):
        self.assertEqual(self.name, self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_invalid_quantity_raises_value_error(self):
        quantity = [0, -10]
        for q in quantity:
            with self.assertRaises(ValueError) as error:
                self.pet_shop.add_food(self.food_name, q)

            self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_with_valid_quantity(self):
        actual = self.pet_shop.add_food(self.food_name, self.quantity)
        self.assertEqual(self.quantity, self.pet_shop.food[self.food_name])
        self.assertEqual(f"Successfully added {self.quantity:.2f} grams of {self.food_name}.", actual)
        additional_quantity = 50.12
        actual_second_test = self.pet_shop.add_food(self.food_name, additional_quantity)
        self.assertEqual(self.quantity + additional_quantity, self.pet_shop.food[self.food_name])
        self.assertEqual(f"Successfully added {additional_quantity:.2f} grams of {self.food_name}.", actual_second_test)

    def test_add_pet_witch_does_not_exist_in_pets_list(self):
        actual = self.pet_shop.add_pet(self.pet_name)
        self.assertEqual([self.pet_name], self.pet_shop.pets)
        self.assertEqual(f"Successfully added {self.pet_name}.", actual)

    def test_add_pet_with_existing_pet_name_raises_exception(self):
        self.pet_shop.add_pet(self.pet_name)
        with self.assertRaises(Exception) as exc:
            self.pet_shop.add_pet(self.pet_name)

        self.assertEqual("Cannot add a pet with the same name", str(exc.exception))

    def test_feed_pet_raises_exception_if_pet_not_in_pets_list(self):
        with self.assertRaises(Exception) as exc:
            self.pet_shop.feed_pet(self.food_name, self.pet_name)

        self.assertEqual(f"Please insert a valid pet name", str(exc.exception))

    def test_feed_pet_with_not_available_food_returns_string(self):
        self.pet_shop.add_pet(self.pet_name)
        actual = self.pet_shop.feed_pet(self.food_name, self.pet_name)
        self.assertEqual(f'You do not have {self.food_name}', actual)

    def test_feed_pet_with_food_quantity_less_than_100(self):
        self.pet_shop.add_pet(self.pet_name)
        self.pet_shop.add_food(self.food_name, self.quantity-1)
        actual = self.pet_shop.feed_pet(self.food_name, self.pet_name)

        expected_quantity = (self.quantity - 1) + 1000.00
        self.assertEqual(expected_quantity, self.pet_shop.food[self.food_name])
        self.assertEqual("Adding food...", actual)

    def test_feed_pet_with_food_quantity_greater_or_equal_to_100(self):
        self.pet_shop.add_pet(self.pet_name)
        self.pet_shop.add_food(self.food_name, self.quantity)
        actual = self.pet_shop.feed_pet(self.food_name, self.pet_name)

        expected_quantity = self.quantity - 100
        self.assertEqual(expected_quantity, self.pet_shop.food[self.food_name])
        self.assertEqual(f"{self.pet_name} was successfully fed", actual)

    def test_repr_returns_correct_string(self):
        self.pet_shop.add_pet(self.pet_name)
        expected = f'Shop {self.name}:\n' \
               f'Pets: {", ".join(self.pet_shop.pets)}'
        actual = str(self.pet_shop)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    main()