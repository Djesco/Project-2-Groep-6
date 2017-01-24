import pygame
import random
import time

pygame.init()

size = 256
spots_size = size//10
midden = int(size/2)
links = boven = int(size/4)
rechts = onder = size-links
keer = 20
spots = (0,0,0)
dice = (255,255,255)
screen = pygame.display.set_mode((size, size))


for i in range(keer):
    cijfer = random.randint(1,6)
    screen.fill(dice)
    if cijfer % 2 == 1:
        pygame.draw.circle(screen,spots,(midden,midden),spots_size)
    if cijfer ==2 or cijfer ==3 or cijfer==4 or cijfer==5 or cijfer==6:
        pygame.draw.circle(screen,spots,(links,onder),spots_size)
        pygame.draw.circle(screen,spots,(rechts,boven),spots_size)
    if cijfer==4 or cijfer==5 or cijfer==6:
        pygame.draw.circle(screen,spots,(links,boven),spots_size)
        pygame.draw.circle(screen,spots,(rechts,onder),spots_size)
    if cijfer==6:
        pygame.draw.circle(screen,spots,(midden,onder),spots_size)
        pygame.draw.circle(screen,spots,(midden,boven),spots_size)

    pygame.display.flip()
    time.sleep(0.4)
pygame.quit()
quit()

