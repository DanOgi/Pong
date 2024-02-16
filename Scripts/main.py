import pygame
import time
from scenes import *
from windowManager import WindowManager
from sceneManager import SceneManager

# TODO Dodać do scenemanagera możliwość przesyłania zmiennych pomiędzy scenami 

class Main():
    def __init__(self) -> None:
        self.main_clock = pygame.time.Clock()
        self.frame_rate = 60

        self.last_time = time.time()
        self.dt = 0

        self.window_manager = WindowManager(self)
        self.scene_manager = SceneManager(self)

        self.win_surf = self.window_manager.get_win_surf()

        self.scene_manager.add(MainMenu("main_menu", self))
        self.scene_manager.add(OptionMenu("options_menu", self))
        self.scene_manager.add(CreditsMenu("credits_menu", self))
        self.scene_manager.add(Game("game", self))
        self.scene_manager.add(GameModeMenu("game_mode_menu", self))
        
        self.scene_manager.set_curr_scene("main_menu")
        self.curr_scene = self.scene_manager.get_curr_scene()

        self.game_mode = None

    def loop(self) -> None:
        while True:
            self.dt = time.time() - self.last_time
            self.dt *= 60
            self.last_time = time.time()

            self.curr_scene = self.scene_manager.get_curr_scene()
            self.win_surf.fill("black")

            self.curr_scene.check_events()
            self.curr_scene.update()
            self.curr_scene.draw()

            pygame.display.update()
            self.main_clock.tick(self.frame_rate)
            
            self.window_manager.update_delta_time(self.dt)

if __name__ == "__main__":
    m = Main()
    m.loop()