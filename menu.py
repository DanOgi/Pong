import pygame
import sys
from button import Button

class Menu:
    def __init__(self) -> None:
        pygame.font.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font("upheavtt.ttf", 256)
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):

        game_button = Button(self.screen, 
                         (self.width/2-100, 275), 
                         (225, 75), 
                         "Nowa Gra",
                         text_size=32,
                         bg_color=(100, 100, 100),
                         font_family="upheavtt.ttf")
        
        option_button = Button(self.screen, 
                         (self.width/2-100, 375), 
                         (225, 75), 
                         "Opcje",
                         text_size=32,
                         bg_color=(100, 100, 100),
                         font_family="upheavtt.ttf")
        
        exit_button = Button(self.screen, 
                         (self.width/2-100, 475), 
                         (225, 75), 
                         "Wyjdz z gry",
                         text_size=32,
                         bg_color=(100, 100, 100),
                         font_family="upheavtt.ttf")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.font.quit()
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_F2]:
                self.stop()
                
            self.screen.fill("black")
            text = self.font.render("Pong", False, (255,255,255))
            text_rect = text.get_rect()
            self.screen.blit(text, (self.width/2-text_rect.width/2, 20))
            
            game_button.draw()
            option_button.draw()
            exit_button.draw()

            self.clock.tick(60)
            pygame.display.flip()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False