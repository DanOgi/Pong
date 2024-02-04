import pygame
from scene import Scene
from button import Button

class Options(Scene):
    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        self.windows_size_button = Button(
            self.main.window,
            (10, 10),
            (300, 100),
            "TEST",
        )

    def display(self) -> None:
        self.windows_size_button.draw()

    def update(self) -> None:
        if self.windows_size_button.on_press():
            #Nie działa
            self.main.width = 320
            self.main.height = 240
            self.main.window = pygame.display.set_mode((self.main.width, self.main.height))

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.curr_disp = self.main.main_menu

