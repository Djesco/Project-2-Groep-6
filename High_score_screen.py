import pygame, sys
from pygame.locals import *
from database import *

pygame.init()

class HS:
    def __init__(self):

        width = 1280
        height = 720
        size = (width, height)
        screen = pygame.display.set_mode(size)
        self.black = 0, 0, 0
        white = (255, 255, 255)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        green = (0, 255, 0)
        screen.fill(white)
        pygame.display.flip()
       # q = pygame.image.load("images/wolken.jpg")
        #screen.blit(q,(0,0))
        font = pygame.font.Font('freesansbold.ttf', 36)
        hs_text = font.render("High Scores", True, self.black)
        fontrect = hs_text.get_rect()
        fontrect.center = (640,50)
        screen.blit(hs_text,fontrect)

        hsrect = Rect(500,500,100,100)
        hsrect.center = (640, 200)

        hslist = download_scores()
        print()

        for i in range(len(hslist)):
            str1, str2 = hslist[i]
            score = str1 + " " + str(str2)
            hstext = font.render(score, True, self.black)
            screen.blit(hstext,hsrect)
            hsrect.y += 37

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            pygame.display.flip()
HS()

