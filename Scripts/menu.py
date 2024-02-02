import pygame
import sys
from scene import Scene
from button import Button

class Menu(Scene):
    def __init__(self, main) -> None:
        pygame.font.init()
        self.main = main
        self.font = pygame.font.Font(None, 128)
        self.game_button = Button(
            self.main.window,
            (self.main.width/2 - 150, 300),
            (300, 100),
            "Nowa Gra",
            64
        )
        super().__init__()

    def update(self):
        if not self.game_button.on_hover():
            self.game_button.text_color = (200, 200, 200)
        else:
            self.game_button.text_color = (255, 255, 255)
        if self.game_button.on_press():
            self.main.curr_disp = self.main.game

    def display(self):
        text = self.font.render("Pong", False, (255, 255, 255))
        text_rect = text.get_rect()
        self.main.window.blit(text, (self.main.width/2 - text_rect.centerx, self.main.height/4 - text_rect.centery))
        self.game_button.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()