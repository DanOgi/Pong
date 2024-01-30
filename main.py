import pygame
from game import Game
from menu import Menu

#TODO ulepszyć sztuczną inteligencję przeciwnika
#TODO W menu dodać funckjonalność klawiszy

game = Game()
menu = Menu()

game_mode = 0

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
        game_mode = 0
    elif keys[pygame.K_F2]:
        game_mode = 1
        
    match game_mode:
        case 0:
            menu.start()
            game.stop()
        case 1:
            menu.stop()
            game.start()
        case _:
            pass

    menu.run()
    game.run()