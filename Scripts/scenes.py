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

class GameState(Enum):
    BALL_IN_GAME = 0
    FIRST_PLAYER_START = 1
    FIRST_PLAYER_GETS_POINT = 2
    SECOND_PLAYER_START = 3
    SECOND_PLAYER_GETS_POINT = 4

class Game(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.game_state = GameState.SECOND_PLAYER_START

        self.first_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.second_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.ball = Circle(self.entities, self, 10)
        self.title_text = Text(self.entities, self, "GAME", text_size = 64)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.first_player.change_pos_to(left = 0, centery = self.win_size[1]/2)
        self.second_player.change_pos_to(right = self.win_size[0], centery = self.win_size[1]/2)
        self.ball.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

        self.first_player_movement = [False, False, False, False] #Up Down Left Right
        self.first_player_movement_vect = pygame.math.Vector2(0, 0)
        self.first_player_movement_speed = 10

        self.second_player_movement = [False, False, False, False] #Up Down Left Right
        self.second_player_movement_vect = pygame.math.Vector2(0, 0)
        self.second_player_movement_speed = 10
        self.second_player_ai_epsilon = 10 # a min number of pixel that are between ball rect centery and second player rect centery needed to make second player move

        self.ball_movement = [False, False, False, False] #Up Down Left Right
        self.ball_movement_vect = pygame.math.Vector2(0, 0)
        self.ball_movement_speed = 5

    def update(self):
        super().update()
        self.move_first_player()

        self.second_player_ai()
        self.move_second_player()

        match self.game_state:
            case GameState.BALL_IN_GAME:
                self.detect_ball_collision()
                self.move_ball()

            case GameState.FIRST_PLAYER_START:
                self.ball.change_pos_to(centery = self.first_player.rect.centery, left = self.first_player.rect.right)

            case GameState.FIRST_PLAYER_GETS_POINT:
                pass

            case GameState.SECOND_PLAYER_START:
                self.ball.change_pos_to(centery = self.second_player.rect.centery, right = self.second_player.rect.left)

            case GameState.SECOND_PLAYER_GETS_POINT:
                pass

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

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         self.second_player_movement[0] = True
            #     if event.key == pygame.K_DOWN:
            #         self.second_player_movement[1] = True

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_UP:
            #         self.second_player_movement[0] = False
            #     if event.key == pygame.K_DOWN:
            #         self.second_player_movement[1] = False

    def move_first_player(self):
        self.first_player_movement_vect = pygame.math.Vector2(0, (self.first_player_movement[1] - self.first_player_movement[0])) * self.first_player_movement_speed
        self.first_player.change_pos_by(self.first_player_movement_vect)

        if self.first_player.rect.top <= 0:
            self.first_player.rect.top = 0

        if self.first_player.rect.bottom >= self.win_size[1]:
            self.first_player.rect.bottom = self.win_size[1]

    def move_second_player(self):
        self.second_player_movement_vect = pygame.math.Vector2(0, (self.second_player_movement[1] - self.second_player_movement[0])) * self.second_player_movement_speed
        self.second_player.change_pos_by(self.second_player_movement_vect)

        if self.second_player.rect.top <= 0:
            self.second_player.rect.top = 0

        if self.second_player.rect.bottom >= self.win_size[1]:
            self.second_player.rect.bottom = self.win_size[1]

    def move_ball(self):
        self.ball_movement_vect = pygame.math.Vector2(self.ball_movement[3] - self.ball_movement[2], self.ball_movement[1] - self.ball_movement[0]) * self.ball_movement_speed
        self.ball.change_pos_by(self.ball_movement_vect)

    def detect_ball_collision(self):
        if self.ball_movement[0] and self.ball.rect.top == 0:
            self.ball_movement[0] = False
            self.ball_movement[1] = True
        
        if self.ball_movement[1] and self.ball.rect.top == self.win_size[1]:
            self.ball_movement[0] = True
            self.ball_movement[1] = False

        if self.ball_movement[2] and self.ball.rect.colliderect(self.first_player.rect):
            self.ball_movement[2] = False
            self.ball_movement[3] = True

        if self.ball_movement[3] and self.ball.rect.colliderect(self.second_player.rect):
            self.ball_movement[2] = True
            self.ball_movement[3] = False

    def second_player_ai(self):
        if self.ball.rect.centery - self.second_player.rect.centery > self.second_player_ai_epsilon: #a ball is higher that second player
            self.second_player_movement[0] = False
            self.second_player_movement[1] = True

        elif self.ball.rect.centery - self.second_player.rect.centery < -self.second_player_ai_epsilon: #a ball is lower that second player
            self.second_player_movement[0] = True
            self.second_player_movement[1] = False

        else:
            self.second_player_movement[0] = False
            self.second_player_movement[1] = False
