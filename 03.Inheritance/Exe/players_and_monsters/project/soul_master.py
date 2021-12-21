from inheritance.Exe.players_and_monsters.project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)