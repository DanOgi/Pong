from game import Game
from menu import Menu
from credits import Credits
from options import Options
from window_resolution_state import WindowResolutionState
import pygame

#TODO Naprawić wymiary obiektów w grze

class Main():
    def __init__(self) -> None:
        self.width, self.height = WindowResolutionState.RESOLUTION_1280X720
        self.dwidth, self.dheight = WindowResolutionState.RESOLUTION_1280X720
        self.was_resolution_changed = False
        self.window = pygame.display.set_mode((self.width, self.height))
        self.time = pygame.time.Clock()
        self.game = Game(self)
        self.main_menu = Menu(self)
        self.credits_menu = Credits(self)
        self.options_menu = Options(self)
        self.curr_disp = self.main_menu
        #self.font_size = 32

    def loop(self) -> None:
        while True:    
            if self.width != self.dwidth or self.height != self.dheight:
                self.was_resolution_changed = True
                self.dwidth = self.width
                self.dheight = self.height

            self.window.fill('black')
        
            self.curr_disp.check_events()
            self.curr_disp.update()
            self.curr_disp.display()
            
            pygame.display.flip()
            self.dt = self.time.tick(60)

            if self.was_resolution_changed:
                self.was_resolution_changed = False
            
m = Main()
m.loop()