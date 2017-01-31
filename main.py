import pygame
import time
import random
import colors
from main_menu import Main_menu 
pygame.init()
fullscreen = pygame.FULLSCREEN
width = 1280
height = 720
screen = pygame.display.set_mode((width,height), (fullscreen))

pygame.display.set_caption("Ontsnapperdam")
clock = pygame.time.Clock()
dt = clock.tick(60)

def main():
    pygame.mixer.music.load("menu music.mp3")
    pygame.mixer.music.play(loops = 999, start = 0.0)
    pygame.mixer.music.set_volume(0.2)
    m = Main_menu()
    while True:
        dt = clock.tick(60)/1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        m = m.update(screen, width, height, events, dt)
        #screen.fill(colors.black())
        #game.update(screen, event, dt)

        pygame.display.flip()
main()

#6 afbeeldingen voor de dobbelsteen, randint bladert door de afbeeldingen enj returnd hoeveel je hebt gegooid
