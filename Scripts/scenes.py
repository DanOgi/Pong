import pygame
import sys
import random
from enum import Enum
from entities import *

class Scene():
    def __init__(self, name, main) -> None:
        self.name = name
        self.main = main
        self.scene_manager = self.main.scene_manager
        self.window_manager = self.main.window_manager
        self.win = self.window_manager.get_win_surf()
        self.win_size = self.window_manager.get_win_size()
        self.dt = self.window_manager.get_delta_time()

        self.entities = pygame.sprite.Group()

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def update(self):
        self.win = self.window_manager.get_win_surf()
        self.win_size = self.window_manager.get_win_size()
        self.dt = self.window_manager.get_delta_time()
        self.entities.update()

    def draw(self):
        self.entities.draw(self.win)

    def check_events(self):
        pass

class MainMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.title_text = Text(self.entities, self, "PONG", text_size=128)
        self.new_game_button = Button(self.entities, self, "New Game", text_size=32)
        self.options_button = Button(self.entities, self, "Options", text_size=32)
        self.credits_button = Button(self.entities, self, "Credits", text_size=32)
        self.exit_button = Button(self.entities, self, "Exit", text_size=32)

        self.new_game_button.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))
        self.options_button.change_pos_to(midtop = self.new_game_button.rect.midbottom)
        self.credits_button.change_pos_to(midtop = self.options_button.rect.midbottom)
        self.exit_button.change_pos_to(midtop = self.credits_button.rect.midbottom)
        self.title_text.change_pos_to(midbottom = self.new_game_button.rect.midtop)
        self.title_text.change_pos_by((0, -self.win_size[1]/10))

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
    
    def check_events(self):
        super().check_events()

        if self.exit_button.is_clicked_once():
            pygame.quit()
            sys.exit()

        if self.options_button.is_clicked_once():
            self.scene_manager.set_curr_scene("options_menu")

        if self.credits_button.is_clicked_once():
            self.scene_manager.set_curr_scene("credits_menu")

        if self.new_game_button.is_clicked_once():
            self.scene_manager.set_curr_scene("game")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
class OptionMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.title_text = Text(self.entities, self, "OPTIONS", text_size=64)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))

    def update(self):
        super().update()
    
    def draw(self):
        super().draw()
    
    def check_events(self):
        super().check_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

class CreditsMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.title_text = Text(self.entities, self, "CREDITS", text_size=64)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))

    def update(self):
        super().update()

    def draw(self):
        super().draw()
    
    def check_events(self):
        super().check_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

class Game(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)
        
        self.title_text = Text(self.entities, self, "GAME", text_size = 64)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))

        self.first_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.secont_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.ball = Circle(self.entities, self, 10)

        self.first_player.change_pos_to(left = 0, centery = self.win_size[1]/2)
        self.secont_player.change_pos_to(right = self.win_size[0], centery = self.win_size[1]/2)
        self.ball.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

        self.first_player_movement = [False, False, False, False] #Up Down Left Right
        self.first_player_movement_vect = pygame.math.Vector2(0, 0)
        self.first_player_movement_speed = 10

    def update(self):
        super().update()
        self.move_first_player()

    def draw(self):
        super().draw()

    def check_events(self):
        super().check_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.first_player_movement[0] = True
                if event.key == pygame.K_s:
                    self.first_player_movement[1] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.first_player_movement[0] = False
                if event.key == pygame.K_s:
                    self.first_player_movement[1] = False

    def move_first_player(self):
        self.first_player_movement_vect = pygame.math.Vector2(0, (self.first_player_movement[1] - self.first_player_movement[0])) * self.first_player_movement_speed
        self.first_player.change_pos_by(self.first_player_movement_vect)



                
            