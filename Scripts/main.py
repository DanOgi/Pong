from game import Game
from menu import Menu
import pygame

class Main():
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((1280, 720))
        self.time = pygame.time.Clock()
        self.game = Game(self)
        self.menu = Menu(self)
        self.curr_disp = self.menu

    def loop(self) -> None:
        while True:
            self.window.fill('black')
            
            self.curr_disp.check_events()
            self.curr_disp.update()
            self.curr_disp.display()
            
            pygame.display.flip()
            self.time.tick(60)

m = Main()
m.loop()
