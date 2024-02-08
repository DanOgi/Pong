import pygame
import pygame.gfxdraw
import random

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

    def update(self, **kwargs) -> None:
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

        self.pos = pos
        self.text = text
        self.text_size = text_size
        self.text_font = text_font
        self.text_color = text_color

        self.font = pygame.Font(self.text_font, self.text_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(center = pos)

    def update(self, **kwargs) -> None:
        super().update()
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect(center = self.pos)


    def set_text(self, text):
        self.text = text  

    def get_size(self):
        return self.image.get_size()
    
class Carousele():
    def __init__(self, pos, text_size) -> None:
        self.entities = pygame.sprite.Group()

        self.text = Text(self.entities, pos, "1280 x 720", text_size)
        self.right_button = Button(self.entities, [0, 0], ">", text_size)
        self.left_button = Button(self.entities, [0, 0], "<", text_size)
        
        self.right_button.rect.centery = self.text.rect.centery
        self.left_button.rect.centery = self.text.rect.centery
        
        self.right_button.rect.left = self.text.rect.right
        self.left_button.rect.right = self.text.rect.left
    def draw(self, win):
        self.entities.draw(win)

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

    def update(self, **kwargs) -> None:
        super().update()
        self.rect = self.rect.move(0, (self.moving_down - self.moving_up) * self.speed)
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.win_size[1]: self.rect.bottom = self.win_size[1]

    def shot(self, ball):
        ball.moving_right = True
        ball.moving_left = False
        ball.moving_up = self.moving_up
        ball.moving_down = self.moving_down

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size, game_state) -> None:
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.moving_up = False
        self.moving_down = False
        self.speed = 5

        self.win_size = pygame.display.get_window_size()

        self.game_state = game_state

    def update(self, **kwargs) -> None:
        super().update()        
        self.rect = self.rect.move(0, (self.moving_down - self.moving_up) * self.speed)
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= self.win_size[1]: self.rect.bottom = self.win_size[1]

        from scenes import GameState
        match self.game_state:
            case GameState.BALL_IN_GAME:
                pass
            case GameState.PLAYER_START:
                self.rect.centery = self.win_size[1]/2
            case GameState.PLAYER_GETS_POINT:
                self.moving_down = False
                self.moving_up = False
            case GameState.ENEMY_START:
                self.rect.centery = self.win_size[1]/2
            case GameState.ENEMY_GETS_POINT:
                self.moving_down = False
                self.moving_up = False
    
    def move(self, ball):
        if self.rect.centery - ball.rect.centery > 0:
            self.moving_up = True
            self.moving_down = False
        elif self.rect.centery - ball.rect.centery < 0:
            self.moving_up = False
            self.moving_down = True
        else:
            self.moving_up = False
            self.moving_down = False
    
    def set_game_state(self, game_state):
        self.game_state = game_state

    def shot(self, ball):
        rnd = random.randint(0, 2)
        match rnd:
            case 0:
                ball.moving_left = True
                ball.moving_up = False
                ball.moving_down = False
                ball.moving_right = False
            case 1:
                ball.moving_left = True
                ball.moving_up = False
                ball.moving_down = True
                ball.moving_right = False
            case 2:
                ball.moving_left = True
                ball.moving_up = True
                ball.moving_down = False
                ball.moving_right = False
        return True

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, pos, radius, player, enemy, game_state) -> None:
        super().__init__(groups)
        
        self.player = player
        self.enemy = enemy
        self.game_state = game_state

        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius = radius
        pygame.gfxdraw.aacircle(self.image, self.rect.centerx, self.rect.centery, radius-1, (255, 255, 255) )
        pygame.gfxdraw.filled_circle(self.image, self.rect.centerx, self.rect.centery, radius-1, (255, 255, 255))
        self.rect.center = pos

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_vect = pygame.math.Vector2(0, 0)

        self.speed = 5
        
        self.win_size = pygame.display.get_window_size()

    def update(self, **kwargs) -> None:
        super().update()
        from scenes import GameState
        
        match self.game_state:
            case GameState.BALL_IN_GAME:
                self.colision()
                self.moving_vect = pygame.math.Vector2((self.moving_right - self.moving_left), (self.moving_down - self.moving_up))
            case GameState.PLAYER_START:
                self.rect.left = self.player.rect.right
                self.rect.centery = self.player.rect.centery 
            case GameState.ENEMY_START:
                self.rect.right = self.enemy.rect.left
                self.rect.centery = self.enemy.rect.centery 
            case GameState.PLAYER_GETS_POINT:
                self.moving_vect = pygame.math.Vector2(0, 0)
                self.speed = 5
            case GameState.ENEMY_GETS_POINT:
                self.moving_vect = pygame.math.Vector2(0, 0)
                self.speed = 5

        if self.moving_vect.length() > 0: self.moving_vect = self.moving_vect.normalize()
        self.rect = self.rect.move(self.moving_vect*self.speed)

    def colision(self) -> None:
        if self.rect.colliderect(self.player.rect) and self.moving_left:
            self.moving_left = False
            self.moving_right = True
            self.speed += 1
        
        if self.rect.colliderect(self.enemy.rect) and self.moving_right:
            self.moving_left = True
            self.moving_right = False
            self.speed += 1

        if self.moving_down and self.rect.bottom >= self.win_size[1]:
            self.moving_down = False
            self.moving_up = True

        if self.moving_up and self.rect.top <= 0:
            self.moving_down = True
            self.moving_up = False

    def set_game_state(self, game_state):
        self.game_state = game_state