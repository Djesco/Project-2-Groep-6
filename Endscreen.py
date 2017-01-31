import pygame
import sys
from pygame.locals import *
from database import *


class Endscreen:
    def __init__(self, name):
        self.name = name

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



    def update(self, screen, width, height, events, dt):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        blue = (0, 0, 175)
        red = (175 ,0 ,0)
        bright_red = (255, 0 ,0)
        screen.fill(white)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        if self.name != "Highscores":
            TitleText, TitleRect = self.text_objects("{} heeft gewonnen!".format(self.name), largeText, black)
        else:
            TitleText, TitleRect = self.text_objects("Highscores".format(self.name), largeText, black)
        TitleRect.center = ((width/2),(height/10))
        BackText, BackRect = self.text_objects("< Menu", midText, white)
        BackRect.center = (62.5, 25)
        mouse = pygame.mouse.get_pos()

        font = pygame.font.Font('freesansbold.ttf', 36)


        hsrect = Rect(500,500,100,100)
        hsrect.center = (width//3, 200)

        hslist = download_scores()

        for i in range(len(hslist)):
            name, score = hslist[i]
            display = "Name: " + name + ", Turns: " + str(score)
            hstext = font.render(display, True, black)
            screen.blit(hstext,hsrect)
            hsrect.y += 32




        if 125 > mouse[0] > 0 and (50 > mouse[1] > 0):
            pygame.draw.rect(screen, bright_red, (0, 0, 125, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from main_menu import Main_menu
                    m = Main_menu()
                    return m
        else:
            pygame.draw.rect(screen, red, (0, 0, 125, 50))



        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        pygame.display.update()
        return self
