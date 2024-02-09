import pygame
import sys
from enum import Enum
from entities import *

class GameState(Enum):
    PLAYER_START = 0
    PLAYER_GETS_POINT = 1
    ENEMY_START = 2
    ENEMY_GETS_POINT = 3
    BALL_IN_GAME = 4

class Scene():
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.sceneManager = None
        self.main = None
        self.win_manager = None

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

        self.new_game_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "New Game", 64)
        self.options_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + self.new_game_button.get_size()[1]), "Options", 64)
        self.credits_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + 2*self.options_button.get_size()[1]), "Credits", 64)
        self.exit_button = Button(self.entities, (self.win_size[0]/2, self.win_size[1]/2 + 3*self.credits_button.get_size()[1]), "Exit", 64)

        self.menu_text = Text(self.entities, (self.win_size[0]/2, self.new_game_button.rect.top - self.win_size[1]/5), "PONG", 128)
    
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
        self.carousele = Carousele((self.win_size[0]/2, self.win_size[1]/2), 32)
        self.win_res_text = Text(self.entities, (0, 0), "Resolution: ", 32)
        self.accept_button = Button(self.entities, (self.win_size[0]*3/4, self.win_size[1]*3/4), "Accept", 32)

        self.win_res_text.rect.right = self.carousele.left_button.rect.left
        self.win_res_text.rect.centery = self.carousele.left_button.rect.centery
        
    def update(self):
        super().update()
        self.carousele.update()
        self.accept_button.update()
    
    def draw(self):
        super().draw()
        self.entities.draw(self.win)
        self.carousele.draw(self.win)
    
    def check_events(self):
        super().check_events()
        if self.carousele.left_button.is_clicked_once():
            self.carousele.index -= 1
            if self.carousele.index == -1:
                self.carousele.index = self.carousele.resolution_list_len - 1

        if self.carousele.right_button.is_clicked_once():
            if self.carousele.index == self.carousele.resolution_list_len -1:
                self.carousele.index = 0
            else:
                self.carousele.index += 1

        if self.accept_button.is_clicked_once():
            pygame.display.set_mode((self.carousele.resolution_values[self.carousele.index]))

        print(self.accept_button.is_clicked_once())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.sceneManager.set_curr_scene("main_menu")


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
        self.game_state = GameState.PLAYER_START
        #self.text = Text(self.entities, (self.win_size[0]/2, self.win_size[1]/2), "GAME", 64)

        self.player = Player(self.entities, (self.win_size[0]*0.02, self.win_size[1]/2), (self.win_size[0]*0.015, self.win_size[1]*0.15))
        self.enemy = Enemy(self.entities, (self.win_size[0] - self.win_size[0]*0.02, self.win_size[1]/2), (self.win_size[0]*0.015, self.win_size[1]*0.15), self.game_state)
        self.ball = Ball(self.entities, (self.win_size[0]/2, self.win_size[1]/2), 10, self.player, self.enemy, self.game_state)

        self.player_points = 0
        self.enemy_points = 0

        self.player_points_text = Text(self.entities, (self.win_size[0]/4, self.win_size[1]/4), str(self.player_points), 128, None, (150, 150, 150))
        self.enemy_points_text = Text(self.entities, (3*self.win_size[0]/4, self.win_size[1]/4), str(self.enemy_points), 128, None, (150, 150, 150))

    def update(self):
        super().update()
        
        self.entities.update()
        self.ball.set_game_state(self.game_state)
        self.enemy.set_game_state(self.game_state)
        self.player_points_text.set_text(str(self.player_points))
        self.enemy_points_text.set_text(str(self.enemy_points))

        match self.game_state:
            case GameState.BALL_IN_GAME:
                if self.ball.rect.left <= 0:
                    self.game_state = GameState.ENEMY_GETS_POINT
                if self.ball.rect.right >= self.win_size[0]:
                    self.game_state = GameState.PLAYER_GETS_POINT
                self.enemy.move(self.ball)
            case GameState.PLAYER_START:
                pass
            case GameState.PLAYER_GETS_POINT:
                self.player_points += 1
                self.game_state = GameState.ENEMY_START
            case GameState.ENEMY_START:
                if self.enemy.shot(self.ball):
                    self.game_state = GameState.BALL_IN_GAME
            case GameState.ENEMY_GETS_POINT:
                self.enemy_points += 1
                self.game_state = GameState.PLAYER_START
    
    def draw(self):
        super().draw()
        pygame.draw.aaline(self.win, (150, 150, 150), (self.win_size[0]/2, 0), (self.win_size[0]/2, self.win_size[1]))
        self.entities.draw(self.win)

    def check_events(self):
        super().check_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.player.moving_down = True
                if event.key == pygame.K_w:
                    self.player.moving_up = True
                if event.key == pygame.K_SPACE:
                    if self.game_state == GameState.PLAYER_START:
                        self.game_state = GameState.BALL_IN_GAME
                        self.player.shot(self.ball)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player.moving_down = False
                if event.key == pygame.K_w:
                    self.player.moving_up = False
