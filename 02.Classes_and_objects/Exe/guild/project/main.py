from classes_and_objects.exe.guild.project.guild import Guild
from classes_and_objects.exe.guild.project.player import Player

player = Player("George", 50, 100)
player_test = Player("Peter", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(player))
print(guild.assign_player(player_test))
print(guild.kick_player("Pe"))
print(guild.guild_info())
print(player_test.player_info())
