import pygame
import sys

from ball import Ball
from enemy import Enemy
from player import Player

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.Font(None, 128)
        self.player = Player(pos=[10, self.height/2-50], size=(25, 100), speed=5, game=self)
        self.ball = Ball(pos=(self.player.pos[0]+self.player.size[0]+10, self.player.pos[1]+self.player.size[1]/2), radius=10, speed=1, game=self)
        self.enemy = Enemy(pos=[self.width-35, self.height/2-50], size=(25, 100), speed=5, game=self)
        self.game_state = 0
        pygame.mixer.music.load('ping_pong.mp3')

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.font.quit()
                    sys.exit()

            self.screen.fill("black")

            self.player.update(ball=self.ball, game_state=self.game_state)
            self.enemy.update(ball=self.ball, game_state=self.game_state)
            self.ball.update(game_state=self.game_state, player=self.player,enemy=self.enemy)

            #drawning a vertical line
            for i in range(11):
                if i % 2 == 1: continue
                pygame.draw.line(self.screen, (150, 150, 150), (self.width/2, i*(self.height/11)), (self.width/2, (i+1)*(self.height/11)), 10)
            #pygame.draw.line(screen, (200, 200, 200), (width/2, 0), (width/2, height), 10)
                
            #write score on screen
            player_text = self.font.render(str(self.player.points), False, (150, 150, 150))
            self.screen.blit(player_text, (self.width/4, self.height/6))

            enemy_text = self.font.render(str(self.enemy.points), False, (150, 150, 150))
            self.screen.blit(enemy_text, (self.width * 3/4, self.height/6))

            self.player.draw()
            self.enemy.draw()
            self.ball.draw()

            # write score on screen
            #text = font.render("Player points: " + str(player.points) + "\n" + "Enemy points: " + str(enemy.points),
            #            False, (255, 255, 255))
            #screen.blit(text, (20, 20))

            keys = pygame.key.get_pressed()
    
            #change game state
            match self.game_state:
                case 0:
                    if keys[pygame.K_SPACE]:
                        self.game_state = 1
                case 1:
                    if self.ball.pos[0] < 0:
                        self.game_state = 4
                    elif self.ball.pos[0] > self.width + self.ball.radius:
                        self.game_state = 2
                case 2:
                    self.player.points += 1
                    self.game_state = 3
                case 3:
                    self.enemy.shot(ball=self.ball)
                    self.game_state = 1
                case 4:
                    self.enemy.points += 1
                    self.game_state = 0

            #reset game
            if keys[pygame.K_r]:
                self.game.game_state = 0

            self.clock.tick(self.fps)
            pygame.display.flip()