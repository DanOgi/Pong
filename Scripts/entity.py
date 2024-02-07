import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, size, pos, color) -> None:
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)