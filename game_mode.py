class GameMode:
    def __init__(self) -> None:
        self.mode = 0

    def set_game_mode(self, game_mode):
        self.mode = game_mode

    def get_game_mode(self):
        return self.mode