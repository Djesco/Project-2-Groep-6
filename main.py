import pygame
import sys
from time import sleep
from BoardGame import Game
pygame.init()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

size = width, height = (1280, 720)
grid = colloms, rows = 32, 20
clock = pygame.time.Clock()
basicfont = pygame.font.Font('freesansbold.ttf', 18)
displaysurf = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode(size)
game = Game(colloms,rows,width,height)

events = pygame.event.get()
key = pygame.key.get_pressed()
menu = True

def printText(text, font, color):
    area = font.render(text, True, color)
    return area, area.get_rect()

while menu:
    for event in events:
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            exit()
        elif key[pygame.K_KP_ENTER]:
            menu = False
            game_loop()
    screen.fill(white)
    title = pygame.font.Font('freesansbold.ttf', 50)
    sub = pygame.font.Font('freesansbold.ttf', 25)
    titleText, titleRect = printText("Ontsnapperdam", title, black)
    titleRect.center = ((width/2), (50))
    screen.blit(titleText, titleRect)
    startText, startRect = printText("Start game", sub, black)
    startRect.center = ((width/2), (height/3))
    screen.blit(startText, startRect)
    clock.tick(15)
    pygame.display.update()

def game_loop():
    while not menu:
        for event in events:
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                screen.fill(red)
                endText = basicfont.render('Game over!', True, white)
                endRect = endText.get_rect()
                endRect.topleft = (10, 10)
                displaysurf.blit(endText, endRect)
                pygame.display.flip()
                sleep(1)
                exit()

        screen.fill(black)

        game.draw(screen)

        pygame.display.flip()