from inheritance.Exe.players_and_monsters.project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)