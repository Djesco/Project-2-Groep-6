import pygame
import time
import random
from main_menu import Main_menu 
pygame.init()
 
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ontsnapperdam")
clock = pygame.time.Clock()

def main():
    pygame.mixer.music.load("menu music.mp3")
    pygame.mixer.music.play(loops = 999, start = 0.0)
    pygame.mixer.music.set_volume(0.2)
    m = Main_menu()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        m = m.update(screen, width, height)   
main()

#6 afbeeldingen voor de dobbelsteen, randint bladert door de afbeeldingen enj returnd hoeveel je hebt gegooid