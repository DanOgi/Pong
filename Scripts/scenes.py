import pygame
import sys
import random
from math import sqrt
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
        
        self.need_reload = False

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def update(self):
        self.win = self.window_manager.get_win_surf()
        self.win_size = self.window_manager.get_win_size()
        self.dt = self.window_manager.get_delta_time()
        self.entities.update()

        if self.need_reload:
            self.reload()
            self.need_reload = False

    def draw(self):
        self.entities.draw(self.win)

    def check_events(self):
        pass

    def reload(self):
        print(f"Reload: {self.name}")

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
            self.scene_manager.set_curr_scene("game_mode_menu")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def reload(self):
        super().reload()
        self.new_game_button.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))
        self.options_button.change_pos_to(midtop = self.new_game_button.rect.midbottom)
        self.credits_button.change_pos_to(midtop = self.options_button.rect.midbottom)
        self.exit_button.change_pos_to(midtop = self.credits_button.rect.midbottom)
        self.title_text.change_pos_to(midbottom = self.new_game_button.rect.midtop)
        self.title_text.change_pos_by((0, -self.win_size[1]/10))
    
class OptionMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.title_text = Text(self.entities, self, "OPTIONS", text_size=64)
        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        
        self.carousele_text_options = ["640x480 (4:3)", "800x600 (4:3)", "1024x768 (4:3)", "1280x720 (16:9)", "1280x800 (16:10)", "1366x768 (16:9)",
                                       "1440x900 (16:10)", "1680x1050 (16:10)", "1920x1080 (16:9)", "1920x1200 (16:10)", "2560x1440 (16:9)"]
        self.carousele = Carousele(self.entities, self, self.carousele_text_options)
        self.carousele.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

        self.accept_button = Button(self.entities, self, "Accept", text_size=32)
        self.accept_button.change_pos_to(center=(self.win_size[0]*3/4, self.win_size[1]*3/4))

    def update(self):
        super().update()

        if self.accept_button.is_clicked_once():
            self.need_reload = True
            match self.carousele.get_text():
                case "640x480 (4:3)":
                    self.window_manager.change_win_size(640, 480)
                case "800x600 (4:3)":
                    self.window_manager.change_win_size(800, 600)
                case "1024x768 (4:3)":
                    self.window_manager.change_win_size(1024, 768)
                case "1280x720 (16:9)":
                    self.window_manager.change_win_size(1280, 720)
                case "1280x800 (16:10)":
                    self.window_manager.change_win_size(1280, 800)
                case "1366x768 (16:9)":
                    self.window_manager.change_win_size(1366, 768)
                case "1440x900 (16:10)":
                    self.window_manager.change_win_size(1440, 900)
                case "1680x1050 (16:10)":
                    self.window_manager.change_win_size(1680, 1050)
                case "1920x1080 (16:9)":
                    self.window_manager.change_win_size(1920, 1080)
                case "1920x1200 (16:10)":
                    self.window_manager.change_win_size(1920, 1200)
                case "2560x1440 (16:9)":
                    self.window_manager.change_win_size(2560, 1440)

    def draw(self):
        super().draw()
    
    def check_events(self):
        super().check_events()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene_manager.set_curr_scene("main_menu")

    def reload(self):
        super().reload()
        self.carousele.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))
        self.accept_button.change_pos_to(center=(self.win_size[0]*3/4, self.win_size[1]*3/4))
        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))

class CreditsMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.title_text = Text(self.entities, self, "CREDITS", text_size=64)
        self.creator_text = Text(self.entities, self, "Game made by Daniel Ogorzałek", text_size=64)
        
        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.creator_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

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
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene_manager.set_curr_scene("main_menu")

    def reload(self):
        super().reload()
        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.creator_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

class GameState(Enum):
    BALL_IN_GAME = 0
    FIRST_PLAYER_START = 1
    FIRST_PLAYER_GETS_POINT = 2
    SECOND_PLAYER_START = 3
    SECOND_PLAYER_GETS_POINT = 4

class GameMode(Enum):
    SINGLE_PLAYER = 0
    HOT_SEAT = 1

class Game(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.game_state = GameState.FIRST_PLAYER_START
        self.game_mode = GameMode.SINGLE_PLAYER
        self.first_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.second_player = Rect(self.entities, self, [self.win_size[0]*0.015, self.win_size[1]*0.15])
        #2 496
        sqr_win_size = self.win_size[0] * self.win_size[1]
        sqr_ball_rect = int(sqr_win_size/2496)
        ball_radius = int(sqrt(sqr_ball_rect)/2)
        
        self.ball = Circle(self.entities, self, ball_radius)
        self.title_text = Text(self.entities, self, "GAME", text_size = 64)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.first_player.change_pos_to(left = 0, centery = self.win_size[1]/2)
        self.second_player.change_pos_to(right = self.win_size[0], centery = self.win_size[1]/2)
        self.ball.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

        self.first_player_movement = [False, False, False, False] #Up Down Left Right
        self.first_player_movement_vect = pygame.math.Vector2(0, 0)
        self.first_player_movement_speed = 10
        self.first_player_score = 0
        self.first_player_score_text = Text(self.entities, self, str(self.first_player_score), text_size=64)
        self.first_player_score_text.change_pos_to(center = (self.win_size[0]/4, self.win_size[1]/4))

        self.second_player_movement = [False, False, False, False] #Up Down Left Right
        self.second_player_movement_vect = pygame.math.Vector2(0, 0)
        self.second_player_movement_speed = 10
        self.second_player_ai_epsilon = 10 # a min number of pixel that are between ball rect centery and second player rect centery needed to make second player move
        self.second_player_score = 0
        self.second_player_score_text = Text(self.entities, self, str(self.second_player_score), text_size=64)
        self.second_player_score_text.change_pos_to(center = (self.win_size[0]*3/4, self.win_size[1]/4))

        self.ball_movement = [False, False, False, False] #Up Down Left Right
        self.ball_movement_vect = pygame.math.Vector2(0, 0)
        self.ball_movement_speed = 5
        self.ball_movement_speed_add_value = int(5*0.2)

    def update(self):
        super().update()
        self.move_first_player()

        if self.game_mode == GameMode.SINGLE_PLAYER:
            self.second_player_ai()
        self.move_second_player()

        match self.game_state:
            case GameState.BALL_IN_GAME:
                self.detect_ball_collision()
                self.move_ball()
                if self.ball.rect.left <= 0:
                    self.game_state = GameState.SECOND_PLAYER_GETS_POINT
                if self.ball.rect.right >= self.win_size[0]:
                    self.game_state = GameState.FIRST_PLAYER_GETS_POINT

            case GameState.FIRST_PLAYER_START:
                self.ball.change_pos_to(centery = self.first_player.rect.centery, left = self.first_player.rect.right)

            case GameState.FIRST_PLAYER_GETS_POINT:
                self.ball_movement = [False, False, False, False]
                self.ball_movement_speed = 5
                self.first_player_score += 1
                self.first_player_score_text.change_text(str(self.first_player_score))
                self.game_state = GameState.SECOND_PLAYER_START

            case GameState.SECOND_PLAYER_START:
                self.ball.change_pos_to(centery = self.second_player.rect.centery, right = self.second_player.rect.left)
                if self.game_mode == GameMode.SINGLE_PLAYER:
                    self.second_player_ai_shot()

            case GameState.SECOND_PLAYER_GETS_POINT:
                self.ball_movement = [False, False, False, False]
                self.ball_movement_speed = 5
                self.second_player_score += 1
                self.second_player_score_text.change_text(str(self.second_player_score))
                self.game_state = GameState.FIRST_PLAYER_START

         
    def draw(self):
        super().draw()

    def check_events(self):
        super().check_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #first player keys

                if event.key == pygame.K_ESCAPE:
                    self.scene_manager.set_curr_scene("main_menu")

                if event.key == pygame.K_w:
                    self.first_player_movement[0] = True
                if event.key == pygame.K_s:
                    self.first_player_movement[1] = True
                if event.key == pygame.K_SPACE and self.game_state == GameState.FIRST_PLAYER_START:
                    self.ball_movement[3] = True
                    self.ball_movement[0] = self.first_player_movement[0]
                    self.ball_movement[1] = self.first_player_movement[1]
                    self.game_state = GameState.BALL_IN_GAME

                #second player keys
                if self.game_mode == GameMode.HOT_SEAT:
                    if event.key == pygame.K_UP:
                        self.second_player_movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.second_player_movement[1] = True
                    if event.key == pygame.K_KP_ENTER and self.game_state == GameState.SECOND_PLAYER_START:
                        self.ball_movement[2] = True
                        self.ball_movement[0] = self.second_player_movement[0]
                        self.ball_movement[1] = self.second_player_movement[1]
                        self.game_state = GameState.BALL_IN_GAME

            if event.type == pygame.KEYUP:
                #first player keys
                if event.key == pygame.K_w:
                    self.first_player_movement[0] = False
                if event.key == pygame.K_s:
                    self.first_player_movement[1] = False
                
                #second player keys
                if self.game_mode == GameMode.HOT_SEAT:
                    if event.key == pygame.K_UP:
                        self.second_player_movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.second_player_movement[1] = False
                    

    def reload(self):
        super().reload()
        atributes_dict = self.scene_manager.transfer_list["game"]
        self.game_mode = atributes_dict["game_mode"]

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.first_player_score_text.change_pos_to(center = (self.win_size[0]/4, self.win_size[1]/4))
        self.second_player_score_text.change_pos_to(center = (self.win_size[0]*3/4, self.win_size[1]/4))

        self.first_player.change_size([self.win_size[0]*0.015, self.win_size[1]*0.15])
        self.second_player.change_size([self.win_size[0]*0.015, self.win_size[1]*0.15])

        sqr_win_size = self.win_size[0] * self.win_size[1]
        sqr_ball_rect = int(sqr_win_size/2496)
        ball_radius = int(sqrt(sqr_ball_rect)/2)
        self.ball.change_size(ball_radius)

        self.title_text.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/8))
        self.first_player.change_pos_to(left = 0, centery = self.win_size[1]/2)
        self.second_player.change_pos_to(right = self.win_size[0], centery = self.win_size[1]/2)
        self.ball.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))

        self.ball_movement_speed = int(self.win_size[0]/256)
        self.ball_movement_speed_add_value = int(self.ball_movement_speed*0.2)
        if self.ball_movement_speed_add_value < 1:
            self.ball_movement_speed_add_value = 1

        self.game_state = GameState.FIRST_PLAYER_START
        
        self.first_player_score = 0
        self.second_player_score = 0

        self.first_player_score_text.change_text(str(self.first_player_score))
        self.second_player_score_text.change_text(str(self.second_player_score))

    
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
        #self.ball_movement = [False, False, False, False] #Up Down Left Right
        if self.ball_movement[0] and self.ball.rect.top <= 0:
            self.ball_movement[0] = False
            self.ball_movement[1] = True
        
        if self.ball_movement[1] and self.ball.rect.top >= self.win_size[1]:
            self.ball_movement[0] = True
            self.ball_movement[1] = False

        if self.ball_movement[2] and self.ball.rect.colliderect(self.first_player.rect):
            if not (self.ball_movement[0] or self.ball_movement[1]):
                self.ball_movement[0] = self.first_player_movement[0]
                self.ball_movement[1] = self.first_player_movement[1]
            self.ball_movement[2] = False
            self.ball_movement[3] = True        
            self.ball_movement_speed += self.ball_movement_speed_add_value

        if self.ball_movement[3] and self.ball.rect.colliderect(self.second_player.rect):
            if not (self.ball_movement[0] or self.ball_movement[1]):
                self.ball_movement[0] = self.second_player_movement[0]
                self.ball_movement[1] = self.second_player_movement[1]
            self.ball_movement[2] = True
            self.ball_movement[3] = False
            self.ball_movement_speed += self.ball_movement_speed_add_value

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

    def second_player_ai_shot(self):
        if self.game_state == GameState.SECOND_PLAYER_START:
            rnd = random.randint(0, 2)
            match rnd:
                case 0:
                    self.ball_movement[0] = False
                    self.ball_movement[1] = False
                    self.ball_movement[2] = True
                case 1:
                    self.ball_movement[0] = True
                    self.ball_movement[1] = False
                    self.ball_movement[2] = True
                case 2:
                    self.ball_movement[0] = False
                    self.ball_movement[1] = True
                    self.ball_movement[2] = True
            self.game_state = GameState.BALL_IN_GAME

class GameModeMenu(Scene):
    def __init__(self, name, main) -> None:
        super().__init__(name, main)

        self.single_player_button = Button(self.entities, self, "Singleplayer", text_size=64)
        self.hot_seat_button = Button(self.entities, self, "Hot seat", text_size=64)

        self.single_player_button.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))
        self.hot_seat_button.change_pos_to(centerx = self.single_player_button.rect.centerx, top = self.single_player_button.rect.bottom)

    def update(self):
        return super().update()
    
    def draw(self):
        return super().draw()
    
    def check_events(self):
        super().check_events()
        if self.single_player_button.is_clicked_once():
            self.scene_manager.set_atribute("game", game_mode = GameMode.SINGLE_PLAYER)
            self.scene_manager.set_curr_scene("game")

        if self.hot_seat_button.is_clicked_once():
            self.scene_manager.set_atribute("game", game_mode = GameMode.HOT_SEAT)
            self.scene_manager.set_curr_scene("game")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene_manager.set_curr_scene("main_menu")
    
    def reload(self):
        super().reload()
        self.single_player_button.change_pos_to(center = (self.win_size[0]/2, self.win_size[1]/2))
        self.hot_seat_button.change_pos_to(centerx = self.single_player_button.rect.centerx, top = self.single_player_button.rect.bottom)