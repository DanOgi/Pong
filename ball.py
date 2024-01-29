import pygame 

class Ball:
    def __init__(self, pos:list, radius:int, speed, game) -> None:
        self.pos = pos
        self.radius = radius
        self.color = (255, 255, 255)
        self.speed = speed
        self.move_vector = pygame.math.Vector2(0, 0)
        self.touch_by_player = 0
        self.touch_by_enemy = 0
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.game = game
    
    # draw a ball on screen
    def draw(self):
        self.rect = pygame.draw.circle(self.game.screen, self.color, self.pos, self.radius)

    # ball's movement
    def move(self, game_state, player, enemy):
        self.pos += self.move_vector
        match game_state:
            case 0:
                self.pos[0] = player.pos[0] + player.size[0] + self.radius
                self.pos[1] = player.pos[1] + player.size[1]/2
                self.speed = 1

            case 1:
                self.pos += self.move_vector * self.speed
                if self.pos[1] - self.radius >= self.game.height or self.pos[1] + self.radius <= 0:
                    self.move_vector[1] = -self.move_vector[1]
                
                # colision with enemy
                if self.rect.colliderect(enemy.rect):
                    # check if collision is on enemy's side
                    if abs(self.rect.right - enemy.rect.left) <= 10 :
                        self.move_vector[0] = -1
                        if self.move_vector[1]:
                            self.move_vector[1] = enemy.move_vector[1]
                        
                        if not self.touch_by_enemy and self.speed < 15:
                            self.play_music()
                            self.speed += 1

                        self.touch_by_enemy = 1
                        self.touch_by_player = 0
                    
                    # check if collision is on enemy's bottom
                    if abs(self.rect.top - enemy.rect.bottom) <= 10:
                        self.move_vector[1] = 1
                        self.move_vector[0] = -1

                        if not self.touch_by_enemy and self.speed < 15:
                            self.play_music()
                            self.speed += 1
                        
                        self.touch_by_player = 0
                        self.touch_by_enemy = 1

                    # check if collision is on enemy's top
                    if abs(self.rect.bottom - enemy.rect.top) <= 10:
                        self.move_vector[1] = -1
                        self.move_vector[0] = -1

                        if not self.touch_by_enemy and self.speed < 15:
                            self.play_music()
                            self.speed += 1

                        self.touch_by_player = 0
                        self.touch_by_enemy = 1
                    
                # colision with player
                if self.rect.colliderect(player.rect):

                    # check if collision is on player's side
                    if abs(self.rect.left - player.rect.right) <= 10:
                        self.move_vector[0] = 1
                        if self.move_vector[1] == 0:
                            self.move_vector[1] = player.move_vector[1]
                        
                        if not self.touch_by_player and self.speed < 15:
                            self.play_music()
                            self.speed += 1

                        self.touch_by_player = 1
                        self.touch_by_enemy = 0

                    # check if collision is on player's bottom
                    if abs(self.rect.top - player.rect.bottom) <= 10:
                        self.move_vector[1] = 1
                        self.move_vector[0] = 1

                        if not self.touch_by_player and self.speed < 15:
                            self.play_music()
                            self.speed += 1
                        
                        self.touch_by_player = 1
                        self.touch_by_enemy = 0
                    
                    # check if collision is on player's top
                    if abs(self.rect.bottom - player.rect.top) <= 10:
                        self.move_vector[1] = -1
                        self.move_vector[0] = 1

                        if not self.touch_by_player and self.speed < 15:
                            self.play_music()
                            self.speed += 1

                        self.touch_by_player = 1
                        self.touch_by_enemy = 0
            case 2:
                pass
            case 3:
                self.pos[0] = enemy.pos[0] - self.radius
                self.pos[1] = enemy.pos[1] + enemy.size[1]/2
                self.speed = 1
            case 4:
                pass
            case _:
                pass

    # update a ball's parametersf
    def update(self, game_state, player, enemy):
        self.move(game_state=game_state, player=player, enemy=enemy)

    def play_music(self):
        pygame.mixer.music.play(1)