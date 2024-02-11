import pygame
from scenes import *
from windowManager import WindowManager
from sceneManager import SceneManager

class Main():
    def __init__(self) -> None:
        self.window_manager = WindowManager(self)
        self.scene_manager = SceneManager(self)

        self.win_surf = self.window_manager.get_win_surf()

        self.scene_manager.add(MainMenu("main_menu", self))
        self.scene_manager.add(OptionMenu("options_menu", self))
        self.scene_manager.add(CreditsMenu("credits_menu", self))
        self.scene_manager.add(Game("game", self))
        
        self.scene_manager.set_curr_scene("main_menu")
        self.curr_scene = self.scene_manager.get_curr_scene()

    def loop(self) -> None:
        while True:
            self.curr_scene = self.scene_manager.get_curr_scene()
            self.win_surf.fill("black")

            self.curr_scene.check_events()
            self.curr_scene.update()
            self.curr_scene.draw()

            pygame.display.flip()

m = Main()
m.loop()