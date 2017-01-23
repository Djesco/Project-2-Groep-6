import pygame

class Options:    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def play_music(self):
        pygame.mixer.music.load("menu music.mp3")
        pygame.mixer.music.play(loops = 999, start = 0.0)
        pygame.mixer.music.set_volume(0.2)

    def update(self, screen, width, height, events, dt):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        blue = (0, 0, 175)
        red = (175, 0 ,0)
        green = (0, 175, 0)
        bright_red = (255,0,0)
        bright_green = (0, 255, 0)
        click = pygame.mouse.get_pressed() == (1, 0, 0)
        mouse = pygame.mouse.get_pos()
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        screen.fill(white)
        TitleText, TitleRect = self.text_objects("Opties", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        BackText, BackRect = self.text_objects("< Terug", midText, white)
        BackRect.center = (62.5, 25)
        VolumeText, VolumeRect = self.text_objects("Muziek", midText, white)
        VolumeRect.center = (((width/2) - 100), (height/3))
        AanText, AanRect = self.text_objects("Aan", smallText, white)
        AanRect.center = (((width/2) + 60), (height/3))
        UitText, UitRect = self.text_objects("Uit", smallText, white)
        UitRect.center = (((width/2) + 117.5), (height/3))
        pygame.draw.rect(screen, blue, (((width/2) - 150), ((height/3) - 25), 300, 50))        
        if 125 > mouse[0] > 0 and (50 > mouse[1] > 0):
            pygame.draw.rect(screen, bright_red, (0, 0, 125, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    from main_menu import Main_menu
                    m = Main_menu()
                    return m
        else:
            pygame.draw.rect(screen, red, (0, 0, 125, 50))
        if ((width/2) + 142.5) > mouse[0] > ((width/2) + 92.5) and ((height/3) + 15) > mouse[1] > ((height/3) - 15):
            pygame.draw.rect(screen, bright_red, (((width/2) + 92.5), ((height/3) - 15), 50, 30))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.pause()
        else:
            pygame.draw.rect(screen, red, (((width/2) + 92.5), ((height/3) - 15), 50, 30))
        if ((width/2) + 85) > mouse[0] > ((width/2) + 35) and ((height/3) + 15) > mouse[1] > ((height/3) - 15):
            pygame.draw.rect(screen, bright_green, (((width/2) + 35), ((height/3) - 15), 50, 30))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.play_music()
        else:
            pygame.draw.rect(screen, green, (((width/2) + 35), ((height/3) - 15), 50, 30))
        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        screen.blit(VolumeText, VolumeRect)   
        screen.blit(AanText, AanRect)
        screen.blit(UitText, UitRect)     
        pygame.display.update()
        return self

