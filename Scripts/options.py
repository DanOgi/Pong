import pygame
import sys
from scene import Scene
from button import Button

class Options(Scene):
    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        pygame.font.init()
        self.font = pygame.font.Font("Assets/upheavtt.ttf", 32)
        self.window_size_text = self.font.render("Window size : ", False, (255, 255, 255))
        self.window_size_rect = self.window_size_text.get_rect()
        self.windows_size_button_left = Button(
            self.main.window,
            (self.main.width/4 + self.window_size_rect.right, self.main.height/2  - self.window_size_rect.centery),
            (32, 32),
            "<",
            text_size=32,
            font_family="Assets/upheavtt.ttf"
        )
        self.windows_size_button_righ = Button(
            self.main.window,
            (3*self.main.width/4, self.main.height/2  - self.window_size_rect.centery),
            (32, 32),
            ">",
            text_size=32,
            font_family="Assets/upheavtt.ttf"
        )
        self.window_size_index = 0
        self.window_size_options = ["320 x 240", 
                                    "480 × 320", 
                                    "640 × 480", 
                                    "800 × 480", 
                                    "800 × 600",
                                    "1024 × 600",
                                    "1024 × 768",
                                    "1280 × 720", 
                                    "1280 × 800",
                                    "1280 × 1024",
                                    "1366 × 768",
                                    "1400 × 1050",  
                                    "1440 × 900",  
                                    "1600 × 1024", 
                                    "1600 × 1200",
                                    "1600 × 900",
                                    "1680 × 1050",
                                    "1920 × 1080"]
        self.window_size_options_len = len(self.window_size_options)
    def display(self) -> None:
        self.main.window.blit(self.window_size_text, (self.main.width/4, self.main.height/2 - self.window_size_rect.centery))
        self.windows_size_button_left.draw()
        carousel_rect = self.carousel()
        self.windows_size_button_righ.rect.left = carousel_rect.right
        self.windows_size_button_righ.draw()

    def update(self) -> None:
        if self.windows_size_button_left.on_press():
            self.window_size_index -= 1
            if self.window_size_index == -1:
                self.window_size_index = self.window_size_options_len - 1
        
        if self.windows_size_button_righ.on_press():
            self.window_size_index += 1
            if self.window_size_index == self.window_size_options_len - 1:
                self.window_size_index = 0

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.curr_disp = self.main.main_menu

    def carousel(self):
        text = self.font.render(self.window_size_options[self.window_size_index], False, (255, 255, 255))
        text_rect = self.main.window.blit(text, (self.windows_size_button_left.rect.right, self.windows_size_button_left.rect.top))
        return text_rect