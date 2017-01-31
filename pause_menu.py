import pygame, time
from main_menu import Main_menu
from tutorial import Tutorial
class Pause_menu:
    def __init__(self, previous_screen):
        self.prevscr = previous_screen

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(self, screen, width, height, events, dt):
        black = (0,0,0)
        white = (255,255,255)
        red = (175, 0 ,0)
        brigth_red = (255,0,0)
        green = (0, 175, 0)
        brigth_green = (0, 255, 0)
        blue = (0, 0, 175)
        brigth_blue = (0, 0, 255)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        mouse = pygame.mouse.get_pos()
        TitleText, TitleRect = self.text_objects("Gepauzeerd", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        ResumeText, ResumeRect = self.text_objects("Hervatten", midText, white)
        ResumeRect.center = ((width/2),(height/3))
        MMText, MMRect = self.text_objects("Terug naar hoofdmenu", midText, white)
        MMRect.center = ((width/2),((height/3)*2))
        TutText, TutRect = self.text_objects("Speluitleg", midText, white)
        TutRect.center= ((width/2),(height/2)) 
        screen.fill(white)
        if ((width/2) + 150) > mouse[0] > ((width/2) - 150) and ((height/3) + 25) > mouse[1] > ((height/3) - 25):
            pygame.draw.rect(screen, brigth_green, (((width/2) - 150), ((height/3) - 25), 300, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return self.prevscr
        else:
            pygame.draw.rect(screen, green, (((width/2) - 150), ((height/3) - 25), 300, 50))
        if ((width/2) + 150) > mouse[0] > ((width/2) -150) and (((height/3) * 2) + 25) > mouse[1] > (((height/3) * 2) - 25):
            pygame.draw.rect(screen, brigth_red, (((width/2) - 150), (((height/3) * 2) - 25), 300, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m = Main_menu()
                    return m
        else:
            pygame.draw.rect(screen, red, (((width/2) - 150), (((height/3) * 2) - 25), 300, 50))

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
        if ((width/2) + 150) > mouse[0] > ((width/2) -150) and ((height/2) + 25) > mouse[1] > ((height/2) -25):
            pygame.draw.rect(screen, brigth_blue, (((width/2) - 150), ((height/2) -25), 300, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tut = Tutorial(self)
                    return tut

        else:
            pygame.draw.rect(screen, blue, (((width/2) - 150), ((height/2) -25), 300, 50)) 
        screen.blit(TitleText, TitleRect)
        screen.blit(ResumeText, ResumeRect)
        screen.blit(MMText, MMRect)
        screen.blit(TutText, TutRect)
        pygame.display.flip()
        return self
