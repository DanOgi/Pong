import pygame
import sys
from player import Player
from enemy import Enemy
from ball import Ball

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load('ping_pong.mp3')

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 128)

#TODO: Ulepszyć AI Przeciwnika
#TODO: Dodać menu
    
player = Player(pos=[10, height/2-50], size=(25, 100), speed=5)
ball   = Ball(pos=(player.pos[0]+player.size[0]+10, player.pos[1]+player.size[1]/2), radius=10, speed=1)
enemy  = Enemy(pos=[width-35, height/2-50], size=(25, 100), speed=5)

# game_state = 0 -> player starts
# game_state = 1 -> game
# game_state = 2 -> player gets point
# game_state = 3 -> enemy start 
# game_state = 4 -> enemy gets point 
game_state = 0 

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.font.quit()
            sys.exit()

    screen.fill("black")

    player.update(ball=ball, game_state=game_state)
    enemy.update(ball=ball, game_state=game_state)
    ball.update(game_state=game_state, player=player,enemy=enemy)

    #drawning a vertical line
    for i in range(11):
        if i % 2 == 1: continue
        pygame.draw.line(screen, (150, 150, 150), (width/2, i*(height/11)), (width/2, (i+1)*(height/11)), 10)
    #pygame.draw.line(screen, (200, 200, 200), (width/2, 0), (width/2, height), 10)
        
    #write score on screen
    player_text = font.render(str(player.points), False, (150, 150, 150))
    screen.blit(player_text, (width/4, height/6))

    enemy_text = font.render(str(enemy.points), False, (150, 150, 150))
    screen.blit(enemy_text, (width * 3/4, height/6))

    player.draw()
    enemy.draw()
    ball.draw()

    # write score on screen
    #text = font.render("Player points: " + str(player.points) + "\n" + "Enemy points: " + str(enemy.points),
    #            False, (255, 255, 255))
    #screen.blit(text, (20, 20))

    keys = pygame.key.get_pressed()
    
    #change game state
    match game_state:
        case 0:
            if keys[pygame.K_SPACE]:
                game_state = 1
        case 1:
            if ball.pos[0] < 0:
                game_state = 4
            elif ball.pos[0] > width + ball.radius:
                game_state = 2
        case 2:
            player.points += 1
            game_state = 3
        case 3:
            enemy.shot(ball=ball)
            game_state = 1
        case 4:
            enemy.points += 1
            game_state = 0

    #reset game
    if keys[pygame.K_r]:
        game_state = 0

    clock.tick(fps)
    pygame.display.flip()
    