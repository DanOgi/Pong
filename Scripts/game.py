from scene import Scene
from player import Player
from enemy import Enemy
from ball import Ball
from game_state import GameState
import pygame
import sys
import random

class Game(Scene):

    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        self.player = Player(self, (25, 100), [10, self.main.height/2 - 50])
        self.enemy = Enemy(self, (25, 100), [self.main.width-25-10, self.main.height/2-50])
        self.ball = Ball(self)
        self.game_state = GameState.PLAYER_START
        self.player_points = 0
        self.enemy_points = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, 128)

    def update(self): #change the game parameters
        match self.game_state:
            case GameState.PLAYER_START:
                pass
            case GameState.PLAYER_GETS_POINT:
                self.player_points += 1
                self.game_state = GameState.ENEMY_START
            case GameState.ENEMY_START:
                v = random.randint(0, 1)
                if v: 
                    self.ball.is_moving_up = True
                else:
                    self.ball.is_moving_down = True
                self.ball.is_moving_left = True
                self.game_state = GameState.BALL_IN_GAME
            case GameState.ENEMY_GETS_POINT:
                self.enemy_points += 1
                self.game_state = GameState.PLAYER_START
            case GameState.BALL_IN_GAME:
                if self.ball.rect.left == 0:
                    self.game_state = GameState.ENEMY_GETS_POINT
                if self.ball.rect.right == self.main.width:
                    self.game_state = GameState.PLAYER_GETS_POINT

        self.player.update()
        self.enemy.update()
        self.ball.update()

    def display(self): #draw every item
        player_points_text = self.font.render(str(self.player_points), False, (150, 150, 150))
        player_points_rect = player_points_text.get_rect()
        self.main.window.blit(player_points_text, (self.main.width/4 - player_points_rect.centerx, self.main.height/4 - player_points_rect.centery))

        enemy_points_text = self.font.render(str(self.enemy_points), False, (150, 150, 150))
        enemy_points_rect = enemy_points_text.get_rect()
        self.main.window.blit(enemy_points_text, (3*self.main.width/4 - enemy_points_rect.centerx, self.main.height/4 - enemy_points_rect.centery))
    
        for i in range(11):
            if not i%2:
                pygame.draw.line(self.main.window, (150, 150, 150), (self.main.width/2, (self.main.height/11)*i), (self.main.width/2, (self.main.height/11)*(i+1)), 10)

        self.player.draw()
        self.enemy.draw()
        self.ball.draw()

    def check_events(self): #check if the event occurred
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.player.is_moving_down = True
                if event.key == pygame.K_w:
                    self.player.is_moving_up = True
                if event.key == pygame.K_SPACE and self.game_state == GameState.PLAYER_START:
                    self.ball.is_moving_right = True
                    self.ball.is_moving_down = self.player.is_moving_down
                    self.ball.is_moving_up = self.player.is_moving_up
                    self.game_state = GameState.BALL_IN_GAME
                if event.key == pygame.K_ESCAPE:
                    self.main.curr_disp = self.main.main_menu
                    self.reset()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player.is_moving_down = False
                if event.key == pygame.K_w:
                    self.player.is_moving_up = False

    def reset(self):
        self.player_points = 0
        self.enemy_points = 0
        self.player.rect.centery = self.main.height/2
        self.enemy.rect.centery = self.main.height/2
        self.game_state = GameState.PLAYER_START