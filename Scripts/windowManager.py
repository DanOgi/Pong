import pygame

class WindowManager():
    def __init__(self, main, widht = 1280, height = 780) -> None:
        self.main = main
        self.SCREEN_WIDHT = widht
        self.SCREEN_HEIGHT = height
        self.HALF_SCREEN_WIDHT = int(self.SCREEN_WIDHT/2)
        self.HALF_SCREEN_HEIGHT = int(self.SCREEN_HEIGHT/2)
        self.QUARTER_SCREEN_WIDHT = int(self.SCREEN_WIDHT/4)
        self.QUARTER_SCREEN_HEIGHT = int(self.SCREEN_HEIGHT/4)
        self.create_win()

    def create_win(self):
        self.win_surf = pygame.display.set_mode((self.SCREEN_WIDHT, self.SCREEN_HEIGHT))
        return self.win_surf

    def get_win_surf(self):
        return self.win_surf

    def change_win_size(self, widht, height):
        self.SCREEN_WIDHT = widht
        self.SCREEN_HEIGHT = height
        self.update()
        self.win_surf = pygame.display.set_mode((self.SCREEN_WIDHT, self.SCREEN_HEIGHT))

    def update(self):
        self.HALF_SCREEN_WIDHT = int(self.SCREEN_WIDHT/2)
        self.HALF_SCREEN_HEIGHT = int(self.SCREEN_HEIGHT/2)
        self.QUARTER_SCREEN_WIDHT = int(self.SCREEN_WIDHT/4)
        self.QUARTER_SCREEN_HEIGHT = int(self.SCREEN_HEIGHT/4)

    def get_win_size(self):
        return [self.SCREEN_WIDHT, self.SCREEN_HEIGHT]