import pygame
from scenes import Scene

class SceneManager():
    def __init__(self, main, *scenes: None) -> None:
        self.main = main
        self.scene_list = list(*scenes)
        self.curr_scene = None
        self.win_manager = self.main.window_manager

    def add(self, scene: Scene):
        self.scene_list.append(scene)

    def remove(self, scene_name):
        for s in self.scene_list:
            if s.name == scene_name:
                self.scene_list.remove(s) 

    def set_curr_scene(self, scene_name) -> None:
        for s in self.scene_list:
            if s.name == scene_name:
                self.curr_scene = s
                return
                  
    def get_curr_scene(self) -> Scene:
        return self.curr_scene

    def print(self):
        print(self.scene_list)