from inheritance.Exe.players_and_monsters.project.blade_knight import BladeKnight
from inheritance.Exe.players_and_monsters.project.elf import Elf
from inheritance.Exe.players_and_monsters.project.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
blade_kn = BladeKnight("BKnight", 100)
print(blade_kn.__class__.__bases__[0].__name__)
