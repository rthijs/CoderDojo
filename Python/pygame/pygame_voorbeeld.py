import pygame

VENSTER_BREEDTE = 640
VENSTER_HOOGTE = 480
FPS = 60

pygame.init()
spel_venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
klok = pygame.time.Clock()

aan_het_spelen = True

while aan_het_spelen:

    # Testen op events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # de speler wil het venster sluiten dus: stoppen met spelen
            aan_het_spelen = False

    # Dingen tekenen
    # TODO

    # Het frame genereren en tonen op het scherm
    pygame.display.update()

    # de game-klok een tik verder zetten met de snelheid die we gekozen hebben
    klok.tick(FPS)

pygame.quit()