import pygame

class Options:    
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def play_music(self):
        pygame.mixer.music.load("menu music.mp3")
        pygame.mixer.music.play(loops = 999, start = 0.0)
        pygame.mixer.music.set_volume(0.2)

    def update(self, screen, width, height):
        white = (255, 255, 255)
        black = (0, 0 , 0)
        blue = (0, 0, 175)
        red = (175, 0 ,0)
        green = (0, 175, 0)
        bright_red = (255,0,0)
        bright_green = (0, 255, 0)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() == (1, 0, 0)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        screen.fill(white)
        TitleText, TitleRect = self.text_objects("Opties", largeText, black)
        TitleRect.center = ((width/2),(height/10))
        BackText, BackRect = self.text_objects("< Terug", midText, black)
        BackRect.center = ((width - 62.5), 25)
        VolumeText, VolumeRect = self.text_objects("Muziek", midText, black)
        VolumeRect.center = (((width/2) - 100), (height/3))
        AanText, AanRect = self.text_objects("Aan", smallText, black)
        AanRect.center = (((width/2) + 60), (height/3))
        UitText, UitRect = self.text_objects("Uit", smallText, black)
        UitRect.center = (((width/2) + 117.5), (height/3))
        pygame.draw.rect(screen, blue, (((width/2) - 150), ((height/3) - 25), 300, 50))
        pygame.draw.rect(screen, red, (((width/2) + 92.5), ((height/3) - 15), 50, 30))
        pygame.draw.rect(screen, green, (((width/2) + 35), ((height/3) - 15), 50, 30))
        if (width) > mouse[0] > (width - 100) and (50 > mouse[1] > 0):
            pygame.draw.rect(screen, bright_red, ((width - 125), 0, 125, 50))
            if click:
                from main_menu import Main_menu
                m = Main_menu()
                return m.update(screen, width, height)
        else:
            pygame.draw.rect(screen, red, ((width - 125), 0, 125, 50))
        if ((width/2) + 142.5) > mouse[0] > ((width/2) + 92.5) and ((height/3) + 15) > mouse[1] > ((height/3) - 15):
            pygame.draw.rect(screen, bright_red, (((width/2) + 92.5), ((height/3) - 15), 50, 30))
            if click:
                pygame.mixer.music.pause()
        if ((width/2) + 85) > mouse[0] > ((width/2) + 35) and ((height/3) + 15) > mouse[1] > ((height/3) - 15):
            pygame.draw.rect(screen, bright_green, (((width/2) + 35), ((height/3) - 15), 50, 30))
            if click:
                self.play_music()
        screen.blit(TitleText, TitleRect)
        screen.blit(BackText, BackRect)
        screen.blit(VolumeText, VolumeRect)   
        screen.blit(AanText, AanRect)
        screen.blit(UitText, UitRect)     
        pygame.display.update()
        return self

