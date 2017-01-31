import pygame, time, random, sys
from main_menu import *

pygame.init()

fullscreen = pygame.FULLSCREEN
width = 1280
height = 720
screen = pygame.display.set_mode((width,height), (fullscreen))
white = (255, 255, 255)


class Tutorial:
    def __init__(self, previous_screen):
        self.prevscr =previous_screen

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
        self.prevscr = previous_screen

    def rules(self):

        plaatje = pygame.image.load('images/Tutorialplaatjes/tut1.png')
        screen.fill((white))
        screen.blit(plaatje, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if plaatje.get_rect().collidepoint(x, y):
                        return

    def rules2(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut2.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules3(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut3.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules4(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut4.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules5(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut5.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules6(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut6.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules7(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut7.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules8(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut8.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules9(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut9.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return

    def rules10(self):

            plaatje = pygame.image.load('images/Tutorialplaatjes/tut10.png')
            screen.fill((white))
            screen.blit(plaatje, (0, 0))
            pygame.display.flip()

            running = True
            while (running):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if plaatje.get_rect().collidepoint(x, y):
                            return



    def update(self, screen, width, height, events, dt):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        blue = (0, 0, 175)
        red = (175 ,0 ,0)
        bright_red = (255, 0 ,0)
        bright_blue = (0, 0, 255)
        yellow = (200, 200, 0)
        bright_yellow = (255, 255, 0)
        screen.fill(white)       
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        TitleText, TitleRect = self.text_objects("Speluitleg", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        BackText, BackRect = self.text_objects("< Terug", midText, white)
        BackRect.center = (62.5, 25)
        SkipText, SkipRect = self.text_objects("Speluitleg overslaan >", smallText, white)
        SkipRect.center = ((width - 100), 25)
        NextText, NextRect = self.text_objects("Begin tutorial", midText, black)
        NextRect.center = (650, 385)

        mouse = pygame.mouse.get_pos()



        if 125 > mouse[0] > 0 and (50 > mouse[1] > 0):
            pygame.draw.rect(screen, bright_red, (0, 0, 125, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from main_menu import Main_menu
                    m = Main_menu()
                    return m
        else:
            pygame.draw.rect(screen, red, (0, 0, 125, 50))
        if width > mouse[0] > (width - 200) and 50 > mouse[1] > 0:
            pygame.draw.rect(screen, bright_blue, ((width - 200), 0, 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from playeramount import Player_select
                    pm = Player_select()
                    return pm
        else:
            pygame.draw.rect(screen, blue, ((width - 200), 0, 200, 50))

        # if width > mouse[0] > (width - 100) and height > mouse[1] > (height - 50):
        #     pygame.draw.rect(screen, bright_yellow, ((width - 100), (height - 50), 100, 50))
        if width > mouse[0] > (width/3) and height > mouse[1] > (height/2):
            pygame.draw.rect(screen, bright_yellow, ((width/3), (height/2), 450, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rules()
                    self.rules2()
                    self.rules3()
                    self.rules4()
                    self.rules5()
                    self.rules6()
                    self.rules7()
                    self.rules8()
                    self.rules9()
                    self.rules10()
                    return self.prevscr
                    #laad current afbeelding nr + 1
        else:
            # pygame.draw.rect(screen, yellow, ((width - 100), (height - 50), 100, 50))
            pygame.draw.rect(screen, yellow, ((width/3), (height/2), 450, 50))
        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        screen.blit(SkipText, SkipRect)
        screen.blit(NextText, NextRect)
        pygame.display.update()
        return self







