import pygame
import sys
from entity import Entity

class Scene():
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.sceneManager = None

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def update(self):
        print("update of " + self.name)

    def draw(self, surf):
        print("draw of " + self.name)

    def check_events(self):
        print("check_events of " + self.name)

class MainMenu(Scene):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.draw_entities = pygame.sprite.Group()
        self.new_game_button = Entity(self.draw_entities, (100, 200), (500, 500), (255, 255, 255))

    def update(self):
        return super().update()
    
    def draw(self, surf):
        super().draw(surf)
        self.draw_entities.draw(surf)
    
    def check_events(self):
        super().check_events()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.sceneManager.set_curr_scene("game")