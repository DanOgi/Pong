import pygame
import random
from main import *

class Enemy:
    def __init__(self, pos:list, size:tuple, speed) -> None:
        self.pos = pos
        self.size = size
        self.speed = speed
        self.color = (255, 255, 255)
        self.points = 0
        self.move_vector = pygame.math.Vector2(0, 0)
        self.rect = pygame.Rect(0, 0, 0, 0)
    #draw a enemy on screen
    def draw(self):
        self.rect = pygame.draw.rect(screen, self.color, (*self.pos, *self.size))

    #update enemy's parameters
    def update(self, ball, game_state):
        self.move(ball, game_state)
    
    def move(self, ball, game_state):
        toleration = 5
        self.pos += self.move_vector * self.speed
        
        match game_state:
            case 0:
                if ball.rect.centery-toleration > self.rect.centery:
                    self.move_vector.y = 1
                elif ball.rect.centery+toleration < self.rect.centery:
                    self.move_vector.y = -1
                else:
                    self.move_vector.y = 0
            case 1:
                if ball.rect.centery-toleration > self.rect.centery:
                    self.move_vector.y = 1
                elif ball.rect.centery+toleration < self.rect.centery:
                    self.move_vector.y = -1
                else:
                    self.move_vector.y = 0
            case 2:
                pass
            case 3:
                self.move_vector = pygame.math.Vector2(0, 0)
            case 4:
                pass
            case _:
                pass

        if self.pos[1] <= 0: self.pos[1] = 0
        if self.pos[1] >= height-self.size[1]: self.pos[1] = height-self.size[1]
                
    def shot(self, ball):
        rand = random.randint(0, 2) - 1
        ball.move_vector.x = -1
        ball.move_vector.y = rand