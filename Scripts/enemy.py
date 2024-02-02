import pygame
from game_state import GameState

class Enemy():
    def __init__(self, game, size, pos) -> None:
        self.game = game
        self.size = size
        self.speed = 5
        self.pos = pygame.math.Vector2(*pos)
        self.move_vect = pygame.math.Vector2(0, 0)
        self.is_moving_up = False
        self.is_moving_down = False
        self.rect = pygame.Rect(*self.pos, *self.size)

    def update(self) -> None:
        match self.game.game_state:
            case GameState.PLAYER_START:
                self.is_moving_up = False
                self.is_moving_down = False
            case GameState.PLAYER_GETS_POINT:
                self.is_moving_up = False
                self.is_moving_down = False
            case GameState.ENEMY_START:
                self.is_moving_up = False
                self.is_moving_down = False
            case GameState.ENEMY_GETS_POINT:
                self.is_moving_up = False
                self.is_moving_down = False
            case GameState.BALL_IN_GAME:
                if self.game.ball.rect.centery - self.rect.centery > 15:
                    self.is_moving_down = True
                    self.is_moving_up = False
                elif self.game.ball.rect.centery - self.rect.centery < -15:
                    self.is_moving_down = False
                    self.is_moving_up = True
                else:
                    self.is_moving_down = False
                    self.is_moving_up = False
                    
        self.move_vect.y = self.is_moving_down - self.is_moving_up
        self.rect = self.rect.move(self.move_vect * self.speed)
        if self.rect.top <= 0: self.rect.top = 0 
        if self.rect.bottom >= self.game.main.height: self.rect.bottom = self.game.main.height

    def draw(self) -> None:
        pygame.draw.rect(self.game.main.window, (255, 255, 255), self.rect)