import pygame

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
        NextText, NextRect = self.text_objects("Volgende >", smallText, black)
        NextRect.center = ((width - 50), (height - 25))
        PrevText, PrevRect = self.text_objects("< Vorige", smallText, black)
        PrevRect.center = (50, (height - 25))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() == (1, 0, 0)
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
        if 100 > mouse[0] > 0 and height > mouse[1] > (height - 50):
            pygame.draw.rect(screen, bright_yellow, (0, (height - 50), 100, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("meep")
                    #laad current afbeelding nr - 1
        else:
            pygame.draw.rect(screen, yellow, (0, (height - 50), 100, 50))
        if width > mouse[0] > (width - 100) and height > mouse[1] > (height - 50):
            pygame.draw.rect(screen, bright_yellow, ((width - 100), (height - 50), 100, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mep")
                    #laad current afbeelding nr + 1
        else:
            pygame.draw.rect(screen, yellow, ((width - 100), (height - 50), 100, 50))
        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        screen.blit(SkipText, SkipRect)
        screen.blit(NextText, NextRect) 
        screen.blit(PrevText, PrevRect)
        pygame.display.update()
        return self
#sws tutorial laden maar voeg skip button toe die je naar de game smijt
