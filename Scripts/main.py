from game import Game
from menu import Menu
from credits import Credits
from options import Options
import pygame

class Main():
    def __init__(self) -> None:
        self.width = 1280
        self.height = 720
        self.window = pygame.display.set_mode((self.width, self.height))
        self.time = pygame.time.Clock()
        self.game = Game(self)
        self.main_menu = Menu(self)
        self.credits_menu = Credits(self)
        self.options_menu = Options(self)
        self.curr_disp = self.main_menu

    def loop(self) -> None:
        while True:
            self.window.fill('black')
            
            self.curr_disp.check_events()
            self.curr_disp.update()
            self.curr_disp.display()
            
            pygame.display.flip()
            self.dt = self.time.tick(60)
            
m = Main()
m.loop()