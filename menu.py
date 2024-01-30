import pygame
import sys
from button import Button

class Menu:
    def __init__(self) -> None:
        pygame.font.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 32)
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):

        game_button = Button(self.screen, 
                         (100, 100), 
                         (200, 100), 
                         "Nowa Gra",
                         text_size=32,
                         bg_color=(100, 100, 100))
        
        option_button = Button(self.screen, 
                         (100, 300), 
                         (200, 100), 
                         "Opcje",
                         text_size=32,
                         bg_color=(100, 100, 100))
        
        exit_button = Button(self.screen, 
                         (100, 500), 
                         (200, 100), 
                         "Wyjdź z gry",
                         text_size=32,
                         bg_color=(100, 100, 100))

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
            text = self.font.render("Menu", False, (255,255,255))
            self.screen.blit(text, (20, 20))
            
            game_button.draw()
            option_button.draw()
            exit_button.draw()

            self.clock.tick(60)
            pygame.display.flip()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False