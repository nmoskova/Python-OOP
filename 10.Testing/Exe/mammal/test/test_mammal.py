from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "mammal_type", "sound")

    def test_mammal_initialisation(self):
        name = "Name"
        mammal_type = "Type"
        sound = "Sound"
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_if_makes_the_correct_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_if_kingdom_getter_returns_animal(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_returns_the_right_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()