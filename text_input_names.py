# Laat speler tekst intypen op scherm
# Kijkt of een toets is ingedrukt, zoja dan word gekeken of toets in ascii_to_table staat, waar toets
# verbonden wordt met juiste letter. Deze leter word aan name toegevoegd.
# tekst wordt letter voor letter op scherm geblit
# namen worden in een list opgeslagen in de playerNames variabel

import pygame, sys
from pygame.locals import *
pygame.init()

width = 1280
height = 720
size = (width, height)
screen = pygame.display.set_mode(size)
black = 0,0,0
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
screen.fill(white)
pygame.display.set_caption("Name Input")

name = ""
playerNames = [] #hier staan de namen in nadat ze zijn ingevoerd
playeramount = 3
playersrect = Rect(900, 50, 200, 600)
playersrect.center = (629,480)
charmax = 7

#dictionary die juiste letter aan de ingedrukte toets verbind
ascii_to_alphabet = {pygame.K_a: "a", pygame.K_b:"b", pygame.K_c:"c", pygame.K_d: "d", pygame.K_e:"e",
                     pygame.K_f:"f",pygame.K_g: "g",pygame.K_h:"h", pygame.K_i:"i",pygame.K_j: "j",
                     pygame.K_k: "k", pygame.K_l: "l",pygame.K_m: "m", pygame.K_n:"n", pygame.K_o:"o",
                     pygame.K_p: "p", pygame.K_q:"q", pygame.K_r:"r",pygame.K_s: "s", pygame.K_t: "t",
                     pygame.K_u: "u",pygame.K_v: "v", pygame.K_w:"w", pygame.K_x:"x",pygame.K_y: "y",
                     pygame.K_z:"z", pygame.K_SPACE: " "}

#typ je naam kop tekst
screen_center = (640, 360)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textsurface = fontObj.render("Type je naam", True, black)
rectsurface = textsurface.get_rect()
rectsurface.center = (640, 50)
border = rectsurface.inflate(25, 25)
border = pygame.draw.rect(screen, black, border, 3)
screen.blit(textsurface, rectsurface)

#regelt weergeven elke leter naam
def tekst_input():
    fontObj = pygame.font.Font('freesansbold.ttf', 38)
    letter = fontObj.render(name, True, black)
    screen.blit(letter, (playersrect))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif event.type == KEYDOWN:
            if len(playerNames) <= playeramount - 1:
                if event.key in ascii_to_alphabet and len(name) <= charmax:
                    name += (ascii_to_alphabet[event.key])

                elif event.key == K_RETURN:
                    playerNames.append(str(name))
                    name = ""
                    playersrect.y += 50
            tekst_input()






    pygame.display.flip()
