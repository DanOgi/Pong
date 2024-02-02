import pygame
import sys
from scene import Scene

class Menu(Scene):
    def __init__(self, main) -> None:
        self.main = main
        super().__init__()

    def update(self):
        pass

    def display(self):
        pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()