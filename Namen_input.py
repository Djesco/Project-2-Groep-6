import pygame, sys
from pygame.locals import *
from Game import Game

import warnings

warnings.filterwarnings("ignore")

pygame.init()


class Namen():

    def __init__(self, playeramount, screen):
        self.screen = screen
        self.white = (255, 255, 255)
        self.screen.fill(self.white)
        self.black = (0, 0, 0)
        self.red = (255, 0,0)
        self.naam = ""
        self.all_players = []
        self.playeramount = playeramount  # change to result chosen player amount
        self.charmax = 11
        self.lightblue = (110, 160, 255)
        self.letterrect = Rect(900, 50, 200, 600)
        self.letterrect.center = (629, 480)


        pygame.display.flip()
        self.key_to_alphabet = {pygame.K_a: "a", pygame.K_b: "b", pygame.K_c: "c", pygame.K_d: "d", pygame.K_e: "e",
                             pygame.K_f: "f", pygame.K_g: "g", pygame.K_h: "h", pygame.K_i: "i", pygame.K_j: "j",
                             pygame.K_k: "k", pygame.K_l: "l", pygame.K_m: "m", pygame.K_n: "n", pygame.K_o: "o",
                             pygame.K_p: "p", pygame.K_q: "q", pygame.K_r: "r", pygame.K_s: "s", pygame.K_t: "t",
                             pygame.K_u: "u", pygame.K_v: "v", pygame.K_w: "w", pygame.K_x: "x", pygame.K_y: "y",
                             pygame.K_z: "z", pygame.K_SPACE: " ", K_BACKSPACE: " "}

        screen_center = (640, 360)
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textsurface = fontObj.render("Type je naam en klik op de gevangenis", True, self.black)
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
                        if event.key != K_BACKSPACE:
                            self.naam += (self.key_to_alphabet[event.key])

                            font = pygame.font.Font('freesansbold.ttf', 38)
                            perletter = font.render(self.naam, True, self.black)
                            self.screen.blit(perletter, self.letterrect)
                        elif event.key == K_BACKSPACE:
                            self.new = self.naam[0:-1]
                            perletter.fill(self.white)
                            self.naam = self.naam[0:-1]
                            self.screen.blit(perletter, self.letterrect)
                            perletter = font.render(self.new, True, self.black)
                            self.screen.blit(perletter,self.letterrect)


                    elif event.key == K_RETURN:
                        self.all_players.append(str(self.naam))
                        self.naam = ""
                        self.letterrect.y += 50

                        if len(self.all_players) == self.playeramount:
                            text = font.render("klik op de gevangenis", True, self.black)
                            textrect = text.get_rect()
                            textrect.center = (640,500)
                            self.screen.blit(text,textrect)


                elif event.type == MOUSEBUTTONDOWN and len(self.all_players) == self.playeramount:
                    loc = event.pos
                    if self.gevangrect.collidepoint(loc) or self.next_rect.collidepoint(loc):

                        return self.all_players



            pygame.display.flip()







