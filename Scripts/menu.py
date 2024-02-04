import pygame
import sys
from scene import Scene
from button import Button

class Menu(Scene):
    def __init__(self, main) -> None:
        pygame.font.init()
        self.main = main
        self.font = pygame.font.Font("Assets/upheavtt.ttf", 256)
        self.game_button = Button(
            self.main.window,
            (self.main.width/2 - 150, 300),
            (300, 100),
            "Nowa Gra",
            48,
            font_family="Assets/upheavtt.ttf"
        )
        self.option_button = Button(
            self.main.window,
            (self.main.width/2 - 150, 400),
            (300, 100),
            "Opcje",
            48,
            font_family="Assets/upheavtt.ttf"
        )
        self.credit_button = Button(
            self.main.window,
            (self.main.width/2 - 150, 500),
            (300, 100),
            "Twórca",
            48,
            font_family="Assets/upheavtt.ttf"
        )
        super().__init__()

    def update(self):
        if not self.game_button.on_hover():
            self.game_button.text_color = (200, 200, 200)
        else:
            self.game_button.text_color = (255, 255, 255)
        if self.game_button.on_press():
            self.main.curr_disp = self.main.game

        if not self.option_button.on_hover():
            self.option_button.text_color = (200, 200, 200)
        else:
            self.option_button.text_color = (255, 255, 255)
        if self.option_button.on_press():
            self.main.curr_disp = self.main.options_menu

        if not self.credit_button.on_hover():
            self.credit_button.text_color = (200, 200, 200)
        else:
            self.credit_button.text_color = (255, 255, 255)
        if self.credit_button.on_press():
            self.main.curr_disp = self.main.credits_menu


    def display(self):
        text = self.font.render("Pong", False, (255, 255, 255))
        text_rect = text.get_rect()
        self.main.window.blit(text, (self.main.width/2 - text_rect.centerx, self.main.height/4 - text_rect.centery))
        self.game_button.draw()
        self.option_button.draw()
        self.credit_button.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()