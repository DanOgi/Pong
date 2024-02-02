from scene import Scene
from player import Player
from enemy import Enemy
from ball import Ball
from game_state import GameState
import pygame
import sys

class Game(Scene):

    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        self.player = Player(self, (25, 100), [10, self.main.height/2 - 50])
        self.enemy = Enemy(self, (25, 100), [self.main.width-25-10, self.main.height/2-50])
        self.ball = Ball(self)
        self.game_state = GameState.PLAYER_START

    def update(self): #change the game parameters
        match self.game_state:
            case GameState.PLAYER_START:
                print("Player start")
            case GameState.PLAYER_GETS_POINT:
                print("Player gets a point")
            case GameState.ENEMY_START:
                print("Enemy start")
            case GameState.ENEMY_GETS_POINT:
                print("Enemy gets a point")
            case GameState.BALL_IN_GAME:
                if self.ball.rect.left == 0:
                    self.game_state = GameState.ENEMY_GETS_POINT
                if self.ball.rect.right == self.main.width:
                    self.game_state = GameState.PLAYER_GETS_POINT
                print("Ball in game")

        self.player.update()
        self.enemy.update()
        self.ball.update()

    def display(self): #draw every item
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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player.is_moving_down = False
                if event.key == pygame.K_w:
                    self.player.is_moving_up = False