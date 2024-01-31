import pygame
from game import Game
from menu import Menu
from game_mode import GameMode

#TODO ulepszyć sztuczną inteligencję przeciwnika
#TODO W menu dodać funckjonalność klawiszy

game_mode = GameMode()
game = Game()
menu = Menu(game_mode)

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
        game_mode.set_game_mode(0)
    elif keys[pygame.K_F2]:
        game_mode.set_game_mode(1)
        
    match game_mode.get_game_mode():
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