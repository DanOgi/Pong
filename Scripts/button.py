import pygame
from pygame import Color
from pygame import Surface
from pygame import Font

class Button():
    def __init__(self,
                 screen: Surface, 
                 pos: tuple, 
                 size: tuple, 
                 text: str, 
                 text_size: int = 20, 
                 text_color: Color = (255, 255, 255),
                 bg_color: Color = (0, 0, 0, 0),
                 font_family: Font = None) -> None:

        pygame.font.init()
        self.screen = screen
        self.font = pygame.font.Font(font_family, text_size)
        self.rect = pygame.Rect(*pos, *size)
        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color
        self.was_clicked = False
    
    def draw(self):
        text_surface = self.font.render(self.text,
                                        False,
                                        self.text_color,
                                        self.bg_color)
        text_rect = text_surface.get_rect()
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        self.screen.blit(text_surface, (self.rect.centerx-text_rect.centerx, 
                                        self.rect.centery-text_rect.centery))
    
    def on_hover(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(*mouse_pos)
    
    def on_press(self) -> bool:
        if self.was_clicked and not pygame.mouse.get_pressed()[0]:
            self.was_clicked = False
        if self.on_hover() and not self.was_clicked and pygame.mouse.get_pressed()[0]:
            self.was_clicked = True
            return True
        return False