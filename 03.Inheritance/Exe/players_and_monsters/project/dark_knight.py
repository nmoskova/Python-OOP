from inheritance.Exe.players_and_monsters.project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)