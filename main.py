import pygame
import sys
from BoardGame import Game
pygame.init()

size = width, height = 1366 , 768
grid = colloms, rows = 30, 20
clock = pygame.time.Clock()
black = 0, 0, 0
screen = pygame.display.set_mode(size)
game = Game(colloms,rows,width,height)

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    game.draw(screen)

    pygame.display.flip()

