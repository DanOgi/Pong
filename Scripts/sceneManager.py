import pygame
from scenes import Scene

class SceneManager():
    def __init__(self, main, *scenes: None) -> None:
        self.main = main
        self.scene_list = list(*scenes)
        self.curr_scene = None
        self.win_manager = self.main.window_manager
        self.transfer_list = dict()

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
                s.need_reload = True
                return
                  
    def get_curr_scene(self) -> Scene:
        return self.curr_scene

    def print(self):
        print(self.scene_list)

    def set_atribute(self, scene_name, **kwargs):
        for s in self.scene_list:
            if s.name == scene_name:
                self.transfer_list[scene_name] = kwargs
    