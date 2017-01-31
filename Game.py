import pygame
import random
from database import *
from policeline import *
from pygame.locals import *
import time
from Endscreen import *
from pause_menu import Pause_menu #ook nieuw
import Board as b
from Player import *

class Game:
    def __init__(self, screen, cols, rows, width, height, playeramount):
        self.screen = screen
        self.columns = cols
        self.rows = rows
        self.width = width
        self.height = height
        self.playeramount = playeramount
        self.board = self.Createboard()
        self.players = self.Createplayers(screen)
        self.policeline = Policeline()
        self.policelineturn = 0
        self.turn = 0
        self.cooldown = 0.5
        self.turnstart = True
        self.walk = 0
        self.background = pygame.image.load('images/tiles/rotterdam.png')


    def MoveDirection(self, player, dt):
        key = pygame.key.get_pressed()
        self.cooldown = self.cooldown - dt
        if self.cooldown < 0.0:
            if key[pygame.K_UP]:
                if self.gettile(player.pos.x, player.pos.y-1).isTraversable()and not self.player.lastdirection == "down":
                    player.pos.y -= 1
                    self.cooldown = 0.5
                    self.walk -= 1
                    self.player.lastdirection = "up"
            elif key[pygame.K_DOWN]:
                if self.gettile(player.pos.x, player.pos.y + 1).isTraversable() and not self.player.lastdirection == "up":
                    self.players[self.turn].pos.y += 1
                    self.cooldown = 0.5
                    self.walk -= 1
                    self.player.lastdirection = "down"
            elif key[pygame.K_RIGHT]:
                if self.gettile(player.pos.x + 1 , player.pos.y).isTraversable() and not self.player.lastdirection == "left":
                    self.players[self.turn].pos.x += 1
                    self.cooldown = 0.5
                    self.walk -= 1
                    self.player.lastdirection = "right"
            elif key[pygame.K_LEFT]:
                if self.gettile(player.pos.x-1, player.pos.y).isTraversable() and not self.player.lastdirection == "right":
                    self.players[self.turn].pos.x -= 1
                    self.cooldown = 0.5
                    self.walk -= 1
                    self.player.lastdirection = "left"

    def changeturn(self):
        if self.walk == 0:
            x = random.randrange(1, 33)
            for i in b.kanskaarten:
                if (self.player.pos.x, self.player.pos.y) == i:
                    image = pygame.image.load("images/Surprisekaarten/surprise"+str(x)+".png")
                    self.screen.blit(image, (10, 10))
                    pygame.display.flip()
                    time.sleep(5)
            y = random.randrange(1, 11)
            for j in b.powerups:
                if (self.player.pos.x, self.player.pos.y) == j:
                    image = pygame.image.load("images/Power-ups/powerup"+str(y)+".png")
                    self.screen.blit(image,(10,10))
                    pygame.display.flip()
                    time.sleep(5)
            self.turnstart = True
            self.turn = (self.turn + 1) % self.playeramount
            self.player.playerturns += 1
            self.player = self.players[self.turn]



    def gettile(self, x, y):
        return self.board[x, y]

    def dice(self):
        if self.turnstart:
            size = 256
            spots_size = size // 10
            midden = int(size / 2)
            links = boven = int(size / 4)
            rechts = onder = size - links
            keer = 20
            spots = (0, 0, 0)
            screen = self.screen
            self.message_display("{}'s turn".format(self.player.name), self.player.img, 0)
            pygame.display.update()
            for i in range(keer):
                cijfer = random.randint(1, 6)
                pygame.draw.rect(screen, white, [0, 0, size, size])
                if cijfer % 2 == 1:
                    pygame.draw.circle(screen, spots, (midden, midden), spots_size)
                if cijfer == 2 or cijfer == 3 or cijfer == 4 or cijfer == 5 or cijfer == 6:
                    pygame.draw.circle(screen, spots, (links, onder), spots_size)
                    pygame.draw.circle(screen, spots, (rechts, boven), spots_size)
                if cijfer == 4 or cijfer == 5 or cijfer == 6:
                    pygame.draw.circle(screen, spots, (links, boven), spots_size)
                    pygame.draw.circle(screen, spots, (rechts, onder), spots_size)
                if cijfer == 6:
                    pygame.draw.circle(screen, spots, (midden, onder), spots_size)
                    pygame.draw.circle(screen, spots, (midden, boven), spots_size)

                pygame.display.update()
                time.sleep(0.1)
            time.sleep(1)
            if self.board[self.player.pos.x, self.player.pos.y].start:
                if cijfer >= 4:
                    self.message_display("You got out of jail", self.player.img, 64)
                    self.walk = cijfer
                else:
                    self.walk = 0

            elif self.board[self.player.pos.x, self.player.pos.y].arrow:
                if len(self.player.quests) > 1:
                    self.message_display("Not enough quests", colors.yellow(), 64)
                    self.walk = 0
                elif cijfer >= 4:
                    self.message_display("You got on the boat", self.player.img, 64)
                    self.player.pos.x, self.player.pos.y = boat

            else:
                self.walk = cijfer
            self.turnstart = False

    def isarrested(self):
        if self.player.pos.x < self.policeline.x and self.walk == 0:
            self.message_display("{} has been arrested".format(self.player.name), colors.blue(), 64)
            self.players.remove(self.player)
            self.playeramount -= 1
            self.changeturn()

    def TileAction(self, player):
        if (player.pos.x, player.pos.y) in self.player.quests:
            self.message_display("Quest Complete", colors.yellow(), 0)
            player.removequest((player.pos.x, player.pos.y))
        elif self.board[player.pos.x, player.pos.y].arrow:
                self.walk = 0
        elif self.board[player.pos.x, player.pos.y].policeline and not self.policeline.activated:
            self.policelineturn = self.turn
            self.message_display("Policeline activated", colors.blue(), 64)
            self.policeline.activated = True
        if self.walk == 0:
            if self.board[player.pos.x, player.pos.y].police:
                self.message_display("Next turn you'll walk backwards!", self.player.img, 0)
                if (player.pos.x, player.pos.y) == (28,4):
                    player.lastdirection = "up"
                else:
                    player.lastdirection = "left"
            if self.policeline.activated and (self.turn == 0):
                self.policeline.move()



    def update(self, screen, width, height, events, dt):
        self.player = self.players[self.turn]
        self.draw(screen)
        self.isarrested()
        self.dice()
        self.MoveDirection(self.player, dt)
        self.TileAction(self.player)
        if self.board[self.player.pos.x, self.player.pos.y].boat:
            self.player.playerturns += 1
            insert_players(self.player.name)
            upload_score(self.player.name, self.player.playerturns)
            end = Endscreen(self.player.name)
            return end
        self.changeturn()


        # menu balk in game start
        red = (175, 0, 0)
        bright_red = (255, 0, 0)
        blue = (0, 0, 175)
        bright_blue = (0, 0, 255)
        largeText = pygame.font.Font(None ,75)
        midText = pygame.font.Font(None, 37)
        smallText = pygame.font.Font(None, 25)
        mouse = pygame.mouse.get_pos()
        SkipText, SkipRect = self.text_objects("Menu", midText, white)
        SkipRect.center = ((width - 100), 25)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p = Pause_menu(self)
                    return p
        if width > mouse[0] > (width - 200) and 50 > mouse[1] > 0:
            pygame.draw.rect(screen, bright_red, ((width - 200), 0, 200, 50))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    p = Pause_menu(self)
                    return p
        else:
            pygame.draw.rect(screen, red, ((width - 200), 0, 200, 50))
        screen.blit(SkipText, SkipRect)
        # menu balk in game eind
        pygame.display.update()
        return self


    def drawplayers(self, screen, cSize, rSize):
        for i in range(self.playeramount):
            if self.board[self.players[i].pos.x, self.players[i].pos.y].start:
                self.players[i].draw(screen, cSize, rSize, ((i -3) * rSize))
            elif self.players[i].is_in(lambda x: x.is_same(self.players[i].pos), self.players[i+1:]):
                self.players[i].draw(screen, cSize, rSize, ((self.playeramount - i) * (cSize//18)))
            else:
                self.players[i].draw(screen, cSize, rSize, 0)

    def drawboard(self, screen, cSize, rSize):
        for x in range(self.columns):
            for y in range(self.rows):
                self.board[x,y].draw(screen, cSize, rSize)
                self.board[x,y].drawarenas(screen, cSize, rSize)
                self.board[x, y].drawpoliceline(screen, cSize, rSize)
        self.drawplayers(screen, cSize, rSize)
        self.board[starttile].drawprison(screen, cSize, rSize)


    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.background, (self.width, self.height)), (0, 0))
        cSize = self.width // self.columns
        rSize = self.height // (self.rows + 2)
        self.drawboard(screen, cSize, rSize)
        self.player.drawquests(screen, cSize, rSize)
        self.policeline.draw(screen, cSize, rSize, self.columns)

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, color, offset):
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = self.text_objects(text, largeText, color)
        TextRect.center = ((self.width/2, (self.height/2 + offset)))
        self.screen.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def typename(self, screen):
        screen = self.screen
        name = ""
        font = pygame.font.Font(None, 50)
        while True:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == K_RETURN:
                        return name
                elif evt.type == QUIT:
                    return
            screen.fill((0, 0, 0))
            block = font.render(name, True, (255, 255, 255))
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            pygame.display.flip()

    def Createplayers(self,screen):
            from Namen_input import Namen
            spelernamen = Namen(self.playeramount, screen)
            spelerlijst = spelernamen.check()
            playerlist = []
            for i in spelerlijst:
                name = i
                player = Player(Vector2(0, 10), colors.randomcolor(), name)
                playerlist.append(player)
            return playerlist

    def Createboard(self):
        board = {}
        i = 0
        i2 = 0
        for y in range(self.rows):
            for x in range(self.columns):
                if x == 0:
                    board[x-1,y] = Nothing(Vector2(x,y))
                if y == 0:
                    board[x, y-1] = Nothing(Vector2(x, y))
                if x == self.columns -1:
                    board[self.columns, y] = Nothing(Vector2(x, y))
                if y == self.rows -1:
                    board[x, self.rows] = Nothing(Vector2(x, y))
                if (x, y) == starttile:
                    board[x, y] = Starttile(Vector2(x, y))
                elif (x,y) == arrow:
                    board[x, y] = Arrow(Vector2(x, y))
                elif (x,y) == boat:
                    board[x, y] = Boat(Vector2(x, y))

                elif (x, y) in landmarks:
                    board[x,y] = Landmark(Vector2(x,y), landmarkimgs[i])
                    i += 1
                elif (x, y) in powerups:
                    board[x, y] = Landmark(Vector2(x, y), powerupimgs[i2])
                    i2 += 1

                elif (x, y) in kanskaarten:
                    board[x,y] = Kans(Vector2(x,y))
                elif (x, y) in policesquares:
                    board[x,y] = Police(Vector2(x,y))
                elif (x, y) in whitetiles:
                    board[x,y] = White(Vector2(x,y))
                else:
                    board[x,y] = Nothing(Vector2(x,y))
                if (x, y) in arenas:
                    board[x,y].setArena(True)
                if (x, y) in line:
                    board[x,y].setPoliceline(True)
        return board

