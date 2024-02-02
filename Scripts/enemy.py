import pygame

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
        self.move_vect.y = self.is_moving_down - self.is_moving_up
        self.rect = self.rect.move(self.move_vect * self.speed)
        if self.rect.top <= 0: self.rect.top = 0 
        if self.rect.bottom >= self.game.main.height: self.rect.bottom = self.game.main.height

    def draw(self) -> None:
        pygame.draw.rect(self.game.main.window, (255, 255, 255), self.rect)