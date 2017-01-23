import pygame, sys
from pygame.locals import *
pygame.init()

width = 1280
height = 720
size = (width, height)
screen = pygame.display.set_mode(size)
black = 0,0,0
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
screen.fill(white)
pygame.display.set_caption("Instructies")

#buttons
def instruction_buttons(text,loc,box_size, color):
    fontObj = pygame.font.SysFont('freesans', 22)
    questtext = fontObj.render(text, True, color)
    questbuttontextrect = questtext.get_rect()
    questbuttontextrect.center = loc
    questbuttontext = pygame.draw.rect(screen,white,questbuttontextrect,0)
    questbuttonbackground = questbuttontext.inflate(box_size)
    questbuttonbackground = pygame.draw.rect(screen, color, questbuttonbackground, 3)
    screen.blit(questtext,questbuttontext)
    return questbuttonbackground





#titel, boat afbeelding, titel tekst
def title_boat_etc():
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textsurface = fontObj.render("Instructies", True, black) # string to text, boolean for anti-aliasing, colot text, color background
    rectsurface = textsurface.get_rect() #creates rectangle same size as text
    rectsurface.center = (640,50) #places rectangle in correct place
    border = rectsurface.inflate(25,25) # creates another rectangle, slightly larger than the text rect, to form the border
    border = pygame.draw.rect(screen,black,border,3) # draws border rect on display screen and specifies color, rect to draw and width
    screen.blit(textsurface, rectsurface) #puts textsurface on drawn textrectangle on screen

    # Creates boat image next to instructions title
    img = (pygame.image.load("capture.png"))
    img_x = border.right
    img_y = 12
    screen.blit(img, (img_x,img_y))



#lines voor in de textbox
spellines = ["Spel", " ","Het doel van het spel is om van de gevangenis naar een boot te gaan om mee te vluchten. Onderweg heb ", "je quests die je moet voltooien en kom je power-ups, surprisekaarten, de politielijn, battles en andere ",
         "spelers tegen. De basis regels van het spel zijn:", " ", " ", "-Je moet 4 of hoger gooien om de gevangenis te ontsnappen en op het centraal station te komen, ", "-Je moet 5 of hoger gooien om de ontsnappingsboot te betreden",
         "-Als je achter de politielijn komt te staan, verlies je het spel", " ", "De volgende secties zullen laten zien hoe quests, power ups, surprisekaarten en battles werken."]

poweruplines = ["Power ups", "", "Power ups worden gebruikt om de speler die ze gebruikt een voordeel te geven, ze hoeven niet per se gelijk",
               "gebruikt te worden maar kunnen op elk punt in het spel ingezet worden.", " ", " ", "-Je krijgt een power up als je langs een power up vakje loopt, je hoeft er dus niet per se op te landen.",
               "-Spelers kunnen een power up bewaren en die bij een volgende beurt inzetten.",
               "-De speler mag maar 1 power up per beurt activeren",
               "-Een speler mag meerdere power ups hebben"]

surprise_kaarten = ["Surprise kaarten", " ", "-Je mag maar een surprise kaart per beurt gebruiken, dus wanneer je van een surprise kaart op een nieuwe", "surprise kaart komt mag je geen nieuwe surprise kaart trekken"]

battleslines = ["Battles", " ", "Een battle begint als 2 spelers op hetzelfde vakje staan of in de battle arena. Tijdens het gevecht gooien ", "beide spelers met de dobbelstenen, waarna de speler met het hoogste getal wint. De verliezende",
                "speler moet zijn/haar pion terug bewegen naar zijn/haar back-up fiche.", " ",
            "-Mocht een van de spelers een kaart hebben die betrekking heeft op de battle, krijgt de instructie op het ", "kaartje voorrang over het dobbelen.",
            "-Je kan niet vechten in de gevangenis",
            "-Je kan wel vechten op het laatste vakje voor je de boot opgaat aan het eind van het spel",
            "-Als er gelijkspel is, moeten beide spelers opnieuw gooien"]


# tekst box met uitleg onderwerpen spel
def text_box(listname):
    fontObj = pygame.font.SysFont('freesans', 22)
    textrect_w = width / 6 * 4
    textrect_h = height / 6 * 4
    textrect = Rect(30, 30, textrect_w, textrect_h)
    textrect.center = 640, 360
    textrect = pygame.draw.rect(screen, white, textrect, 2)

    boxborder = textrect.inflate(25,25)
    boxborder.center = textrect.center
    boxborder = pygame.draw.rect(screen,black,boxborder,2)

    for line in listname:
        perline = fontObj.render(line, True, black)
        screen.blit(perline, textrect)
        textrect.y +=20


#Terug knop
def terug_knop():
    fontObj = pygame.font.SysFont('freesansbold', 32)
    terugtekst = fontObj.render("Terug", True, black)
    rectterug = terugtekst.get_rect()
    rectterug.topleft = 32,20
    border = rectterug.inflate(50,20)
    border = pygame.draw.rect(screen,black,border,3)
    onscreen = screen.blit(terugtekst,rectterug)
    return border

spel = instruction_buttons("spel", (380, 450),(35,20), blue)
power_ups = instruction_buttons("power ups", (485, 450), (35, 20), green)
surprisekaarten = instruction_buttons("surprise kaarten", (640, 450), (35, 20), black)
battles = instruction_buttons("battles", (775, 450), (30, 20), red)
buttonlist = [spel, power_ups, surprisekaarten,battles]
terugknop = terug_knop()

# functies roepen
title_boat_etc()
text_box(spellines)
terug_knop()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        #make clickable
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()


            if power_ups.collidepoint(pos) == True:

                screen.fill(white)
                title_boat_etc()
                text_box(poweruplines)
            elif spel.collidepoint(pos):
                screen.fill(white)
                title_boat_etc()
                text_box(spellines)
            elif surprisekaarten.collidepoint(pos):
                screen.fill(white)
                title_boat_etc()
                text_box(surprise_kaarten)
            elif battles.collidepoint(pos):
                screen.fill(white)
                title_boat_etc()
                text_box(battleslines)
            elif terugknop.collidepoint(pos):
                print("ok")#linkt naar hoofdmenu

            terug_knop()
            quest = instruction_buttons("spel", (380, 450), (35, 20), blue)
            power_ups = instruction_buttons("power ups", (485, 450), (35, 20), green)
            surprisekaarten = instruction_buttons("surprise kaarten", (640, 450), (35, 20), black)
            battles = instruction_buttons("battles", (775, 450), (30, 20), red)
            buttonlist = [quest, power_ups, surprisekaarten, battles]






    pygame.display.flip()

#later terug knop verbinden met menu