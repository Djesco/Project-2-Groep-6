import pygame


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
