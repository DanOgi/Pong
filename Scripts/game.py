from scene import Scene
import pygame
import sys

class Game(Scene):
    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        self.rect_pos = [0, 0]
        self.rect_size = [50, 50]
        self.rect_direction = pygame.math.Vector2(0,0)

    def update(self): #change the game parameters
        self.rect_pos[0] += self.rect_direction.x
        self.rect_pos[1] += self.rect_direction.y

    def display(self): #draw every item
        pygame.draw.rect(self.main.window, (255,255,255), (*self.rect_pos, *self.rect_size))

    def check_events(self): #check if the event occurred
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.rect_direction.y = 1
                if event.key == pygame.K_w:
                    self.rect_direction.y = -1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.rect_direction.y = 0