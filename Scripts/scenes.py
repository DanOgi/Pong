import pygame
import sys
from entities import *

class Scene():
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.sceneManager = None
        self.main = None

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def update(self):
        pass

    def draw(self):
        pass

    def check_events(self):
        pass

class MainMenu(Scene):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.entities = pygame.sprite.Group()
        
        self.win = pygame.display.get_surface()
        self.win_size = pygame.display.get_window_size()

        self.new_game_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "New Game")
        self.options_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + self.new_game_button.get_size()[1]), "Options")
        self.credits_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + 2*self.options_button.get_size()[1]), "Credits")
        self.exit_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + 3*self.credits_button.get_size()[1]), "Exit")

        self.menu_text = Text(self.entities, (self.win_size[0]/2, self.win_size[1]/2 - 50), "PONG", 64)
    
    def update(self):
        super().update()
        self.win_size = pygame.display.get_window_size()
        self.entities.update()
    
    def draw(self):
        super().draw()
        self.entities.draw(self.win)
    
    def check_events(self):
        super().check_events()
        
        if self.exit_button.is_clicked_once():
            pygame.quit()
            sys.exit()

        if self.new_game_button.is_clicked_once():
            self.sceneManager.set_curr_scene("game")

        if self.options_button.is_clicked_once():
            self.sceneManager.set_curr_scene("options")

        if self.credits_button.is_clicked_once():
            self.sceneManager.set_curr_scene("credits")    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

class Options(Scene):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.win = pygame.display.get_surface()
        self.win_size = pygame.display.get_window_size()

        self.entities = pygame.sprite.Group()
        
        self.text = Text(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "OPTIONS", 64)

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
        self.entities.draw(self.win)
    
    def check_events(self):
        super().check_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

class Credits(Scene):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.win = pygame.display.get_surface()
        self.win_size = pygame.display.get_window_size()

        self.entities = pygame.sprite.Group()

        self.text = Text(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "Game created by Daniel Ogorzałek", 64)

    def draw(self):
        super().draw()
        self.entities.draw(self.win)
    
    def update(self):
        super().update()
    
    def check_events(self):
        super().check_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
class Game(Scene):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.win = pygame.display.get_surface()
        self.win_size = pygame.display.get_window_size()

        self.entities = pygame.sprite.Group()

        self.text = Text(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "GAME", 64)

    def update(self):
        return super().update()
    
    def draw(self):
        super().draw()
        self.entities.draw(self.win)

    def check_events(self):
        super().check_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()