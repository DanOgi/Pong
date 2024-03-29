from typing import Any
from enum import Enum
import pygame
import pygame.gfxdraw
import time

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, scene) -> None:
        super().__init__(groups)
        self.scene = scene
        self.scene_manager = self.scene.scene_manager
        self.window_manager = self.scene.window_manager
        
        self.image = pygame.Surface((0 ,0))
        self.rect = self.image.get_rect(topleft = (0, 0))

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)

    def change_pos_to(self, **kwargs):
        self.rect = self.rect.move_to(**kwargs)
        self.pos = list(self.rect.topleft)

    def change_pos_by(self, pos):
        self.pos[0] = self.pos[0] + pos[0]
        self.pos[1] = self.pos[1] + pos[1]
        self.rect = self.rect.move(*pos)

class Text(Entity):
    def __init__(self, groups, scene, text="Text", text_color = (255, 255, 255), pos = [0, 0], text_size = 20) -> None:
        super().__init__(groups, scene)
        pygame.font.init()
        
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        self.pos = pos

        self.font = pygame.Font(None, self.text_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(topleft = self.pos)
        
    def change_text(self, text):
        self.text = text

class ButtonState(Enum):
    WAITING_FOR_CURSOR = 0
    WAITING_FOR_CLICK = 1
    WAITING_FOR_RELEASE = 2
    CLICKED = 3

class Button(Entity):
    def __init__(self, groups, scene, text="Click", text_color = (255, 255, 255), pos = [0, 0], text_size = 20) -> None:
        super().__init__(groups, scene)
        pygame.font.init()

        self.button_state = ButtonState.WAITING_FOR_CURSOR

        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        self.pos = pos

        self.font = pygame.Font(None, self.text_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(topleft = self.pos)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        mx, my = pygame.mouse.get_pos()
        mclicked = pygame.mouse.get_pressed()

        match self.button_state:
            case ButtonState.WAITING_FOR_CURSOR:
                if self.rect.collidepoint(mx, my) and mclicked[0]:
                    self.button_state = ButtonState.WAITING_FOR_RELEASE
                elif self.rect.collidepoint(mx, my) and not mclicked[0]:
                    self.button_state = ButtonState.WAITING_FOR_CLICK
            case ButtonState.WAITING_FOR_CLICK:
                if mclicked[0]:
                    self.button_state = ButtonState.CLICKED
                elif not self.rect.collidepoint(mx, my):
                    self.button_state = ButtonState.WAITING_FOR_CURSOR
            case ButtonState.WAITING_FOR_RELEASE:
                if not mclicked[0]:
                    self.button_state = ButtonState.WAITING_FOR_CLICK
                elif not self.rect.collidepoint(mx, my):
                    self.button_state = ButtonState.WAITING_FOR_CURSOR
            case ButtonState.CLICKED:
                if not self.rect.collidepoint(mx, my):
                    self.button_state = ButtonState.WAITING_FOR_CURSOR
                else:
                    self.button_state = ButtonState.WAITING_FOR_RELEASE

    def is_cursore_over(self):
        if self.button_state != ButtonState.WAITING_FOR_CURSOR:
            return True
        return False 
    
    def is_clicked_once(self):
        if self.button_state == ButtonState.CLICKED:
            return True
        return False
    
class Carousele(Entity):
    def __init__(self, groups, scene, text_options : list = ["Text"], pos = [0, 0]) -> None:
        super().__init__(groups, scene)
        pygame.font.init()
        self.f = pygame.Font(None, 32)
    
        self.pos = pos
        self.text_options = text_options
        self.text_options_index = 0

        self.left_button = Button(groups, scene, "<", text_size=32)
        self.right_button = Button(groups, scene, ">", text_size=32)
        self.middle_text = Text(groups, scene, self.text_options[self.text_options_index] ,text_size=32)

        self.left_button.rect.topleft = self.pos
        self.middle_text.rect.topleft = self.left_button.rect.topright
        self.middle_text.pos = self.left_button.rect.topright
        self.right_button.rect.topleft = self.middle_text.rect.topright

        self.part_rect = self.left_button.rect.union(self.middle_text.rect)
        self.rect = self.part_rect.union(self.right_button.rect)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.left_button.rect.topleft = self.pos
        self.middle_text.rect.topleft = self.left_button.rect.topright
        self.middle_text.pos = self.left_button.rect.topright
        self.right_button.rect.topleft = self.middle_text.rect.topright

        self.part_rect = self.left_button.rect.union(self.middle_text.rect)
        self.rect = self.part_rect.union(self.right_button.rect)

        if self.right_button.is_clicked_once():
            if self.text_options_index < len(self.text_options) - 1:
                self.text_options_index += 1
            else:
                self.text_options_index = 0

        if self.left_button.is_clicked_once():
            if self.text_options_index > 0:
                self.text_options_index -= 1
            else:
                self.text_options_index = len(self.text_options) - 1

        self.middle_text.change_text(self.text_options[self.text_options_index])

    def get_text(self):
        return self.text_options[self.text_options_index]
    
class Rect(Entity):
    def __init__(self, groups, scene, rect_size: list, rect_color= (255, 255, 255)) -> None:
        super().__init__(groups, scene)

        self.rect_size = rect_size
        self.rect_color = rect_color

        self.image = pygame.Surface(self.rect_size)
        self.rect = self.image.get_rect()
        self.image.fill(self.rect_color)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)

    def change_size(self, size: list):
        self.rect_size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft = self.pos)
        self.image.fill(self.rect_color)

class Circle(Entity):
    def __init__(self, groups, scene, circle_radius, circle_color = (255, 255, 255)) -> None:
        super().__init__(groups, scene)

        self.circle_radius = circle_radius
        self.circle_color = circle_color

        self.image = pygame.Surface((2*self.circle_radius, 2*self.circle_radius),  pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.gfxdraw.aacircle(self.image, self.rect.centerx, self.rect.centery, self.circle_radius-1, self.circle_color )
        pygame.gfxdraw.filled_circle(self.image, self.rect.centerx, self.rect.centery, self.circle_radius-1, self.circle_color)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs) 

    def change_size(self, radius):
        self.circle_radius = radius
        self.image = pygame.Surface((2*self.circle_radius, 2*self.circle_radius),  pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.gfxdraw.aacircle(self.image, self.rect.centerx, self.rect.centery, self.circle_radius-1, self.circle_color )
        pygame.gfxdraw.filled_circle(self.image, self.rect.centerx, self.rect.centery, self.circle_radius-1, self.circle_color)
    