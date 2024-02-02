from enum import Enum

class GameState(Enum):
        PLAYER_START = 0
        PLAYER_GETS_POINT = 1
        ENEMY_START = 2
        ENEMY_GETS_POINT = 3
        BALL_IN_GAME = 4