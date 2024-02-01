import pygame
import sys
from scene import Scene

class Menu(Scene):
    def __init__(self, main) -> None:
        self.main = main
        self.rect_color = [50, 100, 0]
        self.color_vect = pygame.math.Vector3(1, 1, 1)
        super().__init__()

    def update(self):
        self.rect_color[0] += self.color_vect.x
        self.rect_color[1] += self.color_vect.y
        self.rect_color[2] += self.color_vect.z

        if self.rect_color[0] == 255:
            self.color_vect.x = -1
        elif self.rect_color[0] == 0:
            self.color_vect.x = 1

        if self.rect_color[1] == 255:
            self.color_vect.y = -1
        elif self.rect_color[1] == 0:
            self.color_vect.y = 1

        if self.rect_color[2] == 255:
            self.color_vect.z = -1
        elif self.rect_color[2] == 0:
            self.color_vect.z = 1

    def display(self):
        pygame.draw.rect(self.main.window, self.rect_color,(100, 100, 100, 100))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.main.curr_disp = self.main.game