from typing import Any
import pygame

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

class Button(Entity):
    def __init__(self, groups, scene, text="Click", text_color = (255, 255, 255), pos = [0, 0], text_size = 20) -> None:
        super().__init__(groups, scene)
        pygame.font.init()

        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        self.pos = pos

        self.font = pygame.Font(None, self.text_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(topleft = self.pos)
        self.clicked = False

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        if self.clicked and not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def is_cursore_over(self):
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my):
            return True
        return False 
    
    def is_clicked_once(self):
        if self.is_cursore_over():
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                return True
            return False
        return False

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
    
    