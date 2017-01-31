import pygame
from options import Options
from tutorial import Tutorial
from Endscreen import Endscreen

class Main_menu:

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
        screen.fill(white)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        TitleText, TitleRect = self.text_objects("Ontsnapperdam", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        StartText, StartRect = self.text_objects("Start", midText, white)
        StartRect.center = ((width/2),(height/3))
        ExitText, ExitRect = self.text_objects("Afsluiten", midText, white)
        ExitRect.center = ((width/2),((height/3)*2))
        OptionsText, OptionsRect = self.text_objects("Opties", midText, white)
        OptionsRect.center= ((width/2),(height/2))
        HighscoreText, HighscoreRect = self.text_objects("Highscores", midText, white)
        HighscoreRect.center = ((width/2), (height/6) * 5)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() == (1, 0, 0)
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and ((height/3) + 25) > mouse[1] > ((height/3) - 25):
            pygame.draw.rect(screen, brigth_green, (((width/2) - 100), ((height/3) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tut = Tutorial(self)
                    return tut
        else:
            pygame.draw.rect(screen, green, (((width/2) - 100), ((height/3) - 25), 200, 50))


        if ((width/2) + 100) > mouse[0] > ((width/2) -100) and (((height/3) * 2) + 25) > mouse[1] > (((height/3) * 2) - 25):
            pygame.draw.rect(screen, brigth_red, (((width/2) - 100), (((height/3) * 2) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exit()
        else:
            pygame.draw.rect(screen, red, (((width/2) - 100), (((height/3) * 2) - 25), 200, 50))


        if ((width/2) + 100) > mouse[0] > ((width/2) -100) and ((height/2) + 25) > mouse[1] > ((height/2) -25):
            pygame.draw.rect(screen, brigth_blue, (((width/2) - 100), ((height/2) -25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    op = Options()
                    return op
        else:
            pygame.draw.rect(screen, blue, (((width/2) - 100), ((height/2) -25), 200, 50))


        if ((width/2) + 100) > mouse[0] > ((width/2) -100) and (((height/6) * 5) +25) > mouse[1] > (((height/6) * 5) - 25):
            pygame.draw.rect(screen, brigth_red, (((width/2) - 100), (((height/6) * 5) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end = Endscreen("Highscores")
                    return end
        else:
            pygame.draw.rect(screen, red, (((width/2) - 100), (((height/6) * 5) - 25), 200, 50))

        screen.blit(TitleText, TitleRect)
        screen.blit(StartText, StartRect)
        screen.blit(ExitText, ExitRect)
        screen.blit(OptionsText, OptionsRect)
        screen.blit(HighscoreText, HighscoreRect)
        pygame.display.update()
        return self
