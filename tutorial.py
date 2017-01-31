import pygame, time, random, sys
from main import main

pygame.init()

tut1 = pygame.image.load("images/Tutorialplaatjes/tut1.png")
tut2 = pygame.image.load("images/Tutorialplaatjes/tut2.png")
tut3 = pygame.image.load("images/Tutorialplaatjes/tut3.png")
tut4 = pygame.image.load("images/Tutorialplaatjes/tut4.png")
tut5 = pygame.image.load("images/Tutorialplaatjes/tut5.png")
tut6 = pygame.image.load("images/Tutorialplaatjes/tut6.png")
tut7 = pygame.image.load("images/Tutorialplaatjes/tut7.png")
tut8 = pygame.image.load("images/Tutorialplaatjes/tut8.png")
tut9 = pygame.image.load("images/Tutorialplaatjes/tut9.png")
tut10 = pygame.image.load("images/Tutorialplaatjes/tut10.png")
fullscreen = pygame.FULLSCREEN
width = 1280
height = 720
screen = pygame.display.set_mode((width,height), (fullscreen))
white = (255, 255, 255)

def rules():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut1.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules2()

def rules2():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut2.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules3()

def rules3():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut3.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules4()

def rules4():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut4.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules5()

def rules5():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut5.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules6()

def rules6():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut6.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules7()

def rules7():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut7.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules8()

def rules8():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut8.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        rules9()

def rules9():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut9.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        print("hi")

def rules10():

        redSquare = pygame.image.load('images/Tutorialplaatjes/tut10.png')
        screen.fill((white))
        screen.blit(redSquare, (0, 0))
        pygame.display.flip()

        running = True
        while (running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if redSquare.get_rect().collidepoint(x, y):
                        print("ha")

class Tutorial:
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()



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
        NextText, NextRect = self.text_objects("Begin tutorial slideshow", midText, black)
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
                    # screen.fill((255,255,255))
                    # screen.blit(tut1,(0,0))
                    # pygame.display.flip()
                    # time.sleep(5)
                    # screen.fill((255,255,255))
                    # screen.blit(tut2,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut3,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut4,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut5,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut6,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut7,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut8,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut9,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut10,(0,0))
                    # time.sleep(5)
                    # pygame.display.flip()
                    # screen.fill((255,255,255))
                    # screen.blit(tut1,(0,0))
                    # time.sleep(1)
                    rules()
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







