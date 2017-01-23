import pygame
import time
import random
import colors
from Game import Game
from main_menu import Main_menu 
pygame.init()

size = width, height = 1280, 720
columns = 32
rows = 20
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ontsnapperdam")
clock = pygame.time.Clock()
dt = clock.tick(60)
game = Game(columns, rows, width, height, 4)
def main():
    # pygame.mixer.music.load("menu music.mp3")
    # pygame.mixer.music.play(loops = 999, start = 0.0)
    # pygame.mixer.music.set_volume(0.2)
    m = Main_menu()
    while True:
        dt = clock.tick(60)/1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        # m = m.update(screen, width, height, events, dt)
        screen.fill(colors.black())
        game.update(screen, events, dt)

        pygame.display.flip()
main()

#6 afbeeldingen voor de dobbelsteen, randint bladert door de afbeeldingen enj returnd hoeveel je hebt gegooid