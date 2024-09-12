import pygame
import time
import sys
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width,height))
back_image = pygame.image.load("Space.png")

# Nave
nave = pygame.image.load("Nave.bmp")
naverect = nave.get_rect()
naverect.x = 320
naverect.y = 420

# Tiro
tiro = pygame.image.load("Nave.bmp")
tiroRect = tiro.get_rect()

# Monstro
monstro = pygame.image.load("Nave.bmp")
monstroRect = monstro.get_rect()
listaMonstro = []
listaMonstro.append(monstroRect)
listaMonstro.append(monstroRect)
listaMonstro.append(monstroRect)
listaMonstro.append(monstroRect)
listaMonstro.append(monstroRect)


def atirar(localNave):
    tiroRect.x = localNave
    tiroRect.y -= 4
    screen.blit(tiro, tiroRect)

# qtdMonstro = 0
# while qtdMonstro < 5:
#     listaMonstro[qtdMonstro].x = random.randint(100, 600)
#     listaMonstro[qtdMonstro].y = random.randint(30, 200)

#     qtdMonstro += 1

qtdM = 0
def blit():
    screen.blit(tiro, tiroRect)
    screen.blit(back_image, (0,0))
    screen.blit(nave, naverect)


    while qtdM < 5:
        listaMonstro[qtdM].x = random.randint(200, 300)

        listaMonstro[qtdM].y = random.randint(200, 300)

        screen.blit(monstro, listaMonstro[qtdM])

        qtdM += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        naverect.x -= 10
        if naverect.left < 0:
            naverect.x = 0
        
    if keys[pygame.K_d]:
        naverect.x += 10
        if naverect.right > 640:
            naverect.right = 640

    if keys[pygame.K_SPACE]:
        tiroRect.x = naverect.x
        tiroRect.y = 420
        while tiroRect.y > 30:
            atirar(naverect.x)
            pygame.display.flip()
            blit()

    blit()

    # listaMonstro[0].x = 300

    # listaMonstro[0].y = 100

    # screen.blit(monstro, listaMonstro[0])

    # listaMonstro[1].x = 200
    # listaMonstro[1].y = 300
    # screen.blit(monstro,listaMonstro[1])

    # listaMonstro[2].x = 100
    # listaMonstro[2].y = 200
    # screen.blit(monstro,listaMonstro[2])


    pygame.display.flip()

    time.sleep(0.015)