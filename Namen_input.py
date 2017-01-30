import pygame, sys
from pygame.locals import *
from Game import Game

import warnings

warnings.filterwarnings("ignore")

pygame.init()


class Namen():

    def __init__(self, playeramount):

        width = 1280
        height = 720
        size = (width, height)
        self.screen = pygame.display.set_mode(size)
        self.black = 0, 0, 0
        white = (255, 255, 255)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        self.screen.fill(white)
        pygame.display.set_caption("Name Input")

        self.naam = ""
        self.all_players = []
        self.playeramount = playeramount  # change to result chosen player amount
        self.charmax = 7

        self.letterrect = Rect(900, 50, 200, 600)
        self.letterrect.center = (629, 480)

        pygame.display.flip()
        self.key_to_alphabet = {pygame.K_a: "a", pygame.K_b: "b", pygame.K_c: "c", pygame.K_d: "d", pygame.K_e: "e",
                             pygame.K_f: "f", pygame.K_g: "g", pygame.K_h: "h", pygame.K_i: "i", pygame.K_j: "j",
                             pygame.K_k: "k", pygame.K_l: "l", pygame.K_m: "m", pygame.K_n: "n", pygame.K_o: "o",
                             pygame.K_p: "p", pygame.K_q: "q", pygame.K_r: "r", pygame.K_s: "s", pygame.K_t: "t",
                             pygame.K_u: "u", pygame.K_v: "v", pygame.K_w: "w", pygame.K_x: "x", pygame.K_y: "y",
                             pygame.K_z: "z", pygame.K_SPACE: " "}

        screen_center = (640, 360)
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textsurface = fontObj.render("Type je naam en druk op enter", True, self.black)
        rectsurface = textsurface.get_rect()
        rectsurface.center = (640, 50)
        border = rectsurface.inflate(25, 25)
        border = pygame.draw.rect(self.screen, self.black, border, 3)
        self.screen.blit(textsurface, rectsurface)

        gevangimg = pygame.image.load("images/gevangenis.png")
        self.gevangrect = gevangimg.get_rect()
        self.gevangrect.center = (1100,310)
        self.screen.blit(gevangimg,(self.gevangrect))

        self.next_knop = fontObj.render("ga naar spel", True, self.black)
        self.next_rect = self.next_knop.get_rect()
        self.next_rect.center = (1100,190)
        self.screen.blit(self.next_knop,self.next_rect)

    def check(self):
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

                elif event.type == KEYDOWN and len(self.all_players) <= self.playeramount - 1:

                    if event.key in self.key_to_alphabet and len(self.naam) <= self.charmax:
                        self.naam += (self.key_to_alphabet[event.key])

                    elif event.key == K_RETURN:
                        self.all_players.append(str(self.naam))
                        self.naam = ""
                        self.letterrect.y += 50

                    font = pygame.font.Font('freesansbold.ttf', 38)
                    perletter = font.render(self.naam, True, self.black)
                    self.screen.blit(perletter, self.letterrect)
                elif event.type == MOUSEBUTTONDOWN and len(self.all_players) == self.playeramount:
                    loc = event.pos
                    if self.gevangrect.collidepoint(loc) or self.next_rect.collidepoint(loc):

                        return self.all_players



            pygame.display.flip()







