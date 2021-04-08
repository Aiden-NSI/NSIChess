#importation des modules nécessaires
import pygame
import pygame.gfxdraw
import os.path
pygame.init()  # essential for pygame
pygame.font.init()  # text

#créations des variables nécessaires
background = pygame.image.load("res/fondfull.jpg")
background = pygame.transform.scale(background, (1280, 720))
BACK = pygame.image.load(os.path.join("res", "back.png"))
large = pygame.font.Font("res/Polices/MilkyNice-Clean.ttf", 50)
vsmall = pygame.font.Font("res/Polices/MilkyNice-Clean.ttf", 17)
WHITE = (255, 255, 255)
VIOLET = (51, 51, 102)

# Cette fonction crée des rectangle avec des angles arrondis
def rounded_rect(surf, color, rect, radius=10, border=2, incolor=(VIOLET)):
    if min(rect[2], rect[3]) > 2 * (radius + border):
        _filled_rounded_rect(surf, color, rect, radius)
        rect = (rect[0] + border, rect[1] + border,
                rect[2] - 2*border, rect[3] - 2*border)
        _filled_rounded_rect(surf, incolor, rect, radius)

def _filled_rounded_rect(surf, color, rect, r):
    for x, y in [(rect[0] + r, rect[1] + r),
                 (rect[0] + rect[2] - r - 1, rect[1] + r),
                 (rect[0] + r, rect[1] + rect[3] - r - 1),
                 (rect[0] + rect[2] - r - 1, rect[1] + rect[3] - r - 1)]:
        pygame.gfxdraw.aacircle(surf, x, y, r, color)
        pygame.gfxdraw.filled_circle(surf, x, y, r, color)

    pygame.draw.rect(surf, color, (rect[0] + r, rect[1], rect[2] - 2*r, rect[3]))
    pygame.draw.rect(surf, color, (rect[0], rect[1] + r, rect[2], rect[3] - 2*r))


class ABOUT:
    HEAD = large.render("About NSI-Chess", True, WHITE)

    with open(os.path.join("res", "about.txt"), "r") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

# c'est l'écran
def showScreen(screen):
    screen.blit(background, (0, 0))
    rounded_rect(screen, (255, 255, 255), (150, 10, 500, 60), 16, 4)
    rounded_rect(screen, (255, 255, 255), (50, 80, 700, 380), 10, 4)

    screen.blit(ABOUT.HEAD, (180, 12))
    for cnt, i in enumerate(ABOUT.TEXT):
        screen.blit(i, (70, 90 + cnt*18))

    screen.blit(BACK, (750, 0))
    pygame.display.update()

# Fonction principale appellée quand on appuie sur le mennu principal
def main(screen):
    showScreen(screen)
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 750 < x < 800 and 0 < y < 50:
                    return 1
