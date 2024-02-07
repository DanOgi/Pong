import pygame
import pygame.gfxdraw

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)

class Button(pygame.sprite.Sprite):
    def __init__(self, groups, pos, text = "Click", text_size = 20, text_font = None, text_color = (255, 255, 255)) -> None:
        super().__init__(groups)
        pygame.font.init()
        self.text_size = text_size
        self.text_font = text_font
        self.text_color = text_color
        self.font = pygame.font.Font(self.text_font, self.text_size)
        self.image = self.font.render(text, True, self.text_color)
        self.rect = self.image.get_rect(center = pos)
        self.clicked = False

    def update(self) -> None:
        super().update()
        if not pygame.mouse.get_pressed()[0] and self.clicked:
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
    
    def get_size(self):
        return self.image.get_size()
    
class Text(pygame.sprite.Sprite):
    def __init__(self, groups, pos, text = "Text", text_size = 20, text_font = None, text_color = (255, 255, 255)) -> None:
        super().__init__(groups)
        pygame.font.init()
        self.font = pygame.Font(text_font, text_size)
        self.image = self.font.render(text, True, text_color)
        self.rect = self.image.get_rect(center = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size) -> None:
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.moving_up = False
        self.moving_down = False
        self.speed = 5

        self.win_size = pygame.display.get_window_size()

    def update(self) -> None:
        super().update()
        self.rect = self.rect.move(0, (self.moving_down - self.moving_up) * self.speed)
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.win_size[1]: self.rect.bottom = self.win_size[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size) -> None:
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.moving_up = False
        self.moving_down = False
        self.speed = 5

        self.win_size = pygame.display.get_window_size()

    def update(self) -> None:
        super().update()        
        self.rect = self.rect.move(0, (self.moving_down - self.moving_up) * self.speed)
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.win_size[1]: self.rect.bottom = self.win_size[1]

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, pos, radius) -> None:
        super().__init__(groups)
            
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius = radius
        pygame.gfxdraw.aacircle(self.image, self.rect.centerx, self.rect.centery, radius-1, (255, 255, 255) )
        pygame.gfxdraw.filled_circle(self.image, self.rect.centerx, self.rect.centery, radius-1, (255, 255, 255))
        self.rect.center = pos


    def update(self) -> None:
        super().update()
