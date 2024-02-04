import pygame
from scene import Scene

class Credits(Scene):
    def __init__(self, main) -> None:
        super().__init__()
        self.main = main
        pygame.font.init()
        self.font = pygame.font.Font("Assets/upheavtt.ttf", 32)

    def display(self) -> None:
        creator_text_surf = self.font.render("Game created by: Daniel Ogorzalek", False, (255, 255, 255))
        creator_text_rect = creator_text_surf.get_rect()
        self.main.window.blit(creator_text_surf, (self.main.width/2 - creator_text_rect.centerx, self.main.height/2 - creator_text_rect.centery))

        font_text_surf = self.font.render("Font: Upheaval created by Ænigma", False, (255, 255, 255))
        font_text_rect = font_text_surf.get_rect()
        self.main.window.blit(font_text_surf, (self.main.width/2 - font_text_rect.centerx, self.main.height/2 - font_text_rect.centery + creator_text_rect.size[1]))

    def update(self) -> None:
        pass

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.curr_disp = self.main.main_menu