import pygame
from main import *

class Player:
    def __init__(self, pos: list, size: tuple, speed) -> None:
        self.pos = pos
        self.size = size
        self.speed = speed
        self.color = (255, 255, 255)
        self.move_vector = pygame.math.Vector2(0, 0)
        self.points = 0

    #player movement control 
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_vector.y = -1
        elif keys[pygame.K_DOWN]:
            self.move_vector.y = 1
        else:
            self.move_vector.y = 0

        self.pos[1] += self.move_vector.y * self.speed

        if self.pos[1] <= 0: self.pos[1] = 0
        if self.pos[1] >= height-self.size[1]: self.pos[1] = height-self.size[1]

    #shot ball on game's start
    def shot(self, ball):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ball.move_vector.x = 1
            ball.move_vector.y = self.move_vector.y
    
    #update player's parameters 
    def update(self, ball, game_state):
        self.move()
        if game_state == 0:
            self.shot(ball=ball)

    #draw a player on screen
    def draw(self):
        self.rect = pygame.draw.rect(screen, self.color, (*self.pos, *self.size))