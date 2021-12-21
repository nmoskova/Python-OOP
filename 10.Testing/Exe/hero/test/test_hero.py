from unittest import TestCase, main

from testing_10.exe.hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        username = "Username"
        level = 1
        health = 10
        damage = 5
        self.hero = Hero(username, level, health, damage)

    def test_hero_initialisation(self):
        username = "Username"
        level = 1
        health = 10
        damage = 5
        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_battle_if_enemy_username_equals_to_self_username_raises_error(self):
        enemy_hero = Hero("Username", 2, 5, 1)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_hero_health_equal_to_zero_or_lower_raises_error(self):
        for health in [0, -25]:
            hero = Hero("Username", 1, health, 2)
            enemy_hero = Hero("Enemy_Username", 2, 5, 1)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy_hero)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_health_equal_to_zero_or_lower_raises_error(self):
        for health in [0, -25]:
            hero = Hero("Username", 1, 10, 2)
            enemy_hero = Hero("Enemy_Username", 2, health, 1)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy_hero)

            self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_returns_draw_when_both_heroes_die(self):
        hero = Hero("Username", 10, 100, 75)
        enemy_hero = Hero("Enemy_Username", hero.level, hero.health, hero.damage)
        expected_health = hero.health - enemy_hero.level * enemy_hero.damage
        result = hero.battle(enemy_hero)
        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, hero.health)
        self.assertEqual(expected_health, enemy_hero.health)

    def test_battle_returns_you_win_when_enemy_hero_dies(self):
        enemy_level, enemy_health, enemy_damage = 10, 100, 75
        hero_level, hero_health, hero_damage = enemy_level, (enemy_level * enemy_damage) + 250, enemy_damage

        hero = Hero("Username", hero_level, hero_health, hero_damage)
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = hero.battle(enemy)
        expected_health = (hero_health - enemy_level * enemy_damage) + 5
        self.assertEqual("You win", result)
        self.assertEqual(hero_level + 1, hero.level)
        self.assertEqual(expected_health, hero.health)
        self.assertEqual(hero_damage + 5, hero.damage)

    def test_battle_returns_lose_when_hero_dies(self):
        hero_level, hero_health, hero_damage = 10, 100, 75
        enemy_level, enemy_health, enemy_damage = hero_level, (hero_level * hero_damage) + 250, hero_damage

        hero = Hero("Username", hero_level, hero_health, hero_damage)
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = hero.battle(enemy)
        expected_health = (enemy_health - hero_level * hero_damage) + 5
        self.assertEqual("You lose", result)
        self.assertEqual(enemy_level + 1, enemy.level)
        self.assertEqual(expected_health, enemy.health)
        self.assertEqual(enemy_damage + 5, enemy.damage)

    def test_str_returns_correct_string(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
        f"Health: {self.hero.health}\n" \
        f"Damage: {self.hero.damage}\n"
        actual = self.hero.__str__()
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    main()

