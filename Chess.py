#ici nous allons code le jeu d'échec
# ------------- INITIALISATION-------------------
import pygame
import sys
import sound



pygame.init()  # essential for pygame
pygame.font.init()  # text

# DEFINITION DE LA FENETRE
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption('ChessNSI')

# Création de la Police (pas la prison)
policem = pygame.font.SysFont("monospace", 38)
polices = pygame.font.SysFont("monospace", 20)

#Definition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# importation des images
background = pygame.image.load("res/menu.jpg").convert()

#lancement de la sicmu
music = sound.Music()
music.play(load={})

running = True
# boucle tant que condition est vrai
while running :

    # appliquer l'arrière plan
    screen.blit(background, (0, 0))

    # Boutons sur le Menu
    screen.blit(policem.render("ChessNSI", True, WHITE), (65, 60))
    pygame.draw.line(screen, (255, 255, 255), (60, 100), (235, 100), 4)
    screen.blit(polices.render("Version 0.12 alpharoméo", True, WHITE), (230, 100,0,40))

    screen.blit(policem.render("SinglePlayer", True, WHITE), (300, 180, 240, 40))
    screen.blit(policem.render("Preferences", True, WHITE), (0, 440, 210, 40))
    screen.blit(policem.render("About", True, WHITE), (680, 440, 110, 40))

    #position de la souris
    x, y = pygame.mouse.get_pos()

    #si souris sur texte devient noir
    if (300, 180, 240, 40)[0] < x < sum((300, 180, 240, 40)[::2]) and (300, 180, 240, 40)[1] < y < sum((300, 180, 240, 40)[1::2]):
        screen.blit(policem.render("SinglePlayer", True, BLACK), (300, 180, 240, 40)[:2])
    if (0, 440, 210, 40)[0] < x < sum((0, 440, 210, 40)[::2]) and (0, 440, 210, 40)[1] < y < sum((0, 440, 210, 40)[1::2]):
        screen.blit(policem.render("Preferences", True, BLACK), (0, 440, 210, 40)[:2])
    if (680, 440, 110, 40)[0] < x < sum((680, 440, 110, 40)[::2]) and (680, 440, 110, 40)[1] < y < sum((680, 440, 110, 40)[1::2]):
        screen.blit(policem.render("About", True, BLACK), (680, 440, 110, 40)[:2])
    if (230, 100, 0, 40)[0] < x < sum((230, 100, 0, 40)[::2]) and (230, 100, 0, 40)[1] < y < sum((230, 100 , 0, 40)[1::2]):
        screen.blit(polices.render("Version 0.12 alpharoméo", True, BLACK), (230, 100, 0, 40)[:2])

    #Lancement du jeu quand on appuies sur SinglePlayer

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            music.stop()
            pygame.quit()
            print("fermeture du jeu")
