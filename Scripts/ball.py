import pygame
from game_state import GameState

class Ball():
    def __init__(self, game) -> None:
        self.game = game
        self.pos = [0, 0]
        self.radius = 10
        self.move_vect = pygame.math.Vector2(0, 0)
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False
        self.speed = 5
        self.rect = pygame.draw.circle(self.game.main.window, (255, 255, 255), self.pos, self.radius)

    def update(self) -> None:
        match self.game.game_state:
            case GameState.PLAYER_START:
                self.is_moving_up = False
                self.is_moving_down = False
                self.is_moving_left = False
                self.is_moving_right = False
                self.pos[0] = self.game.player.rect.right + self.radius
                self.pos[1] = self.game.player.rect.centery

            case GameState.PLAYER_GETS_POINT:
                self.is_moving_up = False
                self.is_moving_down = False
                self.is_moving_left = False
                self.is_moving_right = False
                self.speed = 5

            case GameState.ENEMY_START:
                self.is_moving_up = False
                self.is_moving_down = False
                self.is_moving_left = False
                self.is_moving_right = False
                self.pos[0] = self.game.enemy.rect.left - self.radius
                self.pos[1] = self.game.enemy.rect.centery

            case GameState.ENEMY_GETS_POINT:
                self.is_moving_up = False
                self.is_moving_down = False
                self.is_moving_left = False
                self.is_moving_right = False
                self.speed = 5

            case GameState.BALL_IN_GAME:
                if self.rect.colliderect(self.game.player) and self.is_moving_left:
                    self.is_moving_left = False
                    self.is_moving_right = True
                    self.is_moving_up = self.game.player.is_moving_up
                    self.is_moving_down = self.game.player.is_moving_down
                    if self.speed != 20: self.speed += 1

                if self.rect.colliderect(self.game.enemy) and self.is_moving_right:
                    self.is_moving_right = False
                    self.is_moving_left = True
                    self.is_moving_up = self.game.enemy.is_moving_up
                    self.is_moving_down = self.game.enemy.is_moving_down
                    if self.speed != 20: self.speed += 1
                
                if self.rect.top <= 0 and self.is_moving_up:
                    self.is_moving_up = False
                    self.is_moving_down = True

                if self.rect.bottom >= self.game.main.height and self.is_moving_down:
                    self.is_moving_down = False
                    self.is_moving_up = True

        self.move_vect.x = self.is_moving_right - self.is_moving_left
        self.move_vect.y = self.is_moving_down - self.is_moving_up
        self.pos += self.move_vect * self.speed

    
    def draw(self) -> None:
        self.rect = pygame.draw.circle(self.game.main.window, (255, 255, 255), self.pos, self.radius)