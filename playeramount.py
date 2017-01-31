import pygame
from Game import Game

class Player_select:
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def update(self, screen, width, height, events, dt):
        grid = colloms, rows = 32, 21
        white = (255, 255, 255)
        black = (0, 0, 0)
        red  = (175, 0 ,0)
        bright_red = (255, 0 ,0)
        blue = (0, 0, 175)
        bright_blue = (0, 0, 255)
        green = (0, 175, 0)
        bright_green = (0, 255, 0)
        yellow = (200, 200, 0)
        bright_yellow = (255, 255, 0)
        screen.fill(white)
        mouse = pygame.mouse.get_pos()
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        TitleText, TitleRect = self.text_objects("Kies het aantal spelers", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        BackText, BackRect = self.text_objects("< Terug", midText, white)
        BackRect.center = (62.5, 25)
        S3Text, S3Rect = self.text_objects("3 Spelers", midText, white)
        S3Rect.center = ((width/2), ((height/6) * 2))
        S4Text, S4Rect = self.text_objects("4 Spelers", midText, white)
        S4Rect.center = ((width/2), ((height/6) * 3))
        S5Text, S5Rect = self.text_objects("5 Spelers", midText, white)
        S5Rect.center = ((width/2), ((height/6) * 4))
        S6Text, S6Rect = self.text_objects("6 Spelers", midText, white)
        S6Rect.center = ((width/2), ((height/6) * 5))
        if 125 > mouse[0] > 0 and (50 > mouse[1] > 0):
            pygame.draw.rect(screen, bright_red, (0, 0, 125, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from tutorial import Tutorial
                    tut = Tutorial(self)
                    return tut
        else:
            pygame.draw.rect(screen, red, (0, 0, 125, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and (((height/6) * 2) + 25) > mouse[1] > (((height/6) * 2) - 25):
            pygame.draw.rect(screen, bright_red, (((width/2) - 100), (((height/6) * 2) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game  = Game(screen, colloms, rows, width, height, 3)
                    return game
        else:
            pygame.draw.rect(screen, red, (((width/2) - 100), (((height/6) * 2) - 25), 200, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and (((height/6) * 3) + 25) > mouse[1] > (((height/6) * 3) - 25):
            pygame.draw.rect(screen, bright_blue, (((width/2) - 100), (((height/6) * 3) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game  = Game(screen, colloms, rows, width, height, 4)
                    return game
        else:
            pygame.draw.rect(screen, blue, (((width/2) - 100), (((height/6) * 3) - 25), 200, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and (((height/6) * 4) + 25) > mouse[1] > (((height/6) * 4) - 25):
            pygame.draw.rect(screen, bright_green, (((width/2) - 100), (((height/6) * 4) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game  = Game(screen, colloms, rows, width, height, 5)
                    return game
        else:
            pygame.draw.rect(screen, green, (((width/2) - 100), (((height/6) * 4) - 25), 200, 50))
        if ((width/2) + 100) > mouse[0] > ((width/2) - 100) and (((height/6) * 5) + 25) > mouse[1] > (((height/6) * 5) - 25):
            pygame.draw.rect(screen, bright_yellow, (((width/2) - 100), (((height/6) * 5) - 25), 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game  = Game(screen, colloms, rows, width, height, 6)
                    return game
        else:
            pygame.draw.rect(screen, yellow, (((width/2) - 100), (((height/6) * 5) - 25), 200, 50))
        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        screen.blit(S3Text, S3Rect)
        screen.blit(S4Text, S4Rect)
        screen.blit(S5Text, S5Rect)
        screen.blit(S6Text, S6Rect)
        pygame.display.update()
        return self

#minimaal 3 spelers
