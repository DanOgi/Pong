import pygame
from sceneManager import SceneManager
from windowManager import WindowManager
from scenes import *

class Main():
    def __init__(self) -> None:
        # self.win_width = 1280
        # self.win_height = 720
        # self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.win_manager = WindowManager(self)
        self.win = self.win_manager.get_win_surf()
        self.clk = pygame.time.Clock()
        self.fps = 60

        self.sceneManager = SceneManager(self)
        self.sceneManager.add(MainMenu("main_menu"))
        self.sceneManager.add(Game("game"))
        self.sceneManager.add(Options("options"))
        self.sceneManager.add(Credits("credits"))
        self.sceneManager.set_curr_scene("main_menu")

        self.curr_scene = self.sceneManager.get_curr_scene()
    
    def loop(self):
        while True:
            self.win = self.win_manager.get_win_surf()
            self.curr_scene = self.sceneManager.get_curr_scene()
            self.win.fill("black")
            
            self.curr_scene.check_events()
            self.curr_scene.update()
            self.curr_scene.draw()

            pygame.display.flip()
            self.clk.tick(self.fps)

m = Main()
m.loop()