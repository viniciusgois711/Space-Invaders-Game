import pygame
import time
import sys

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width,height))
back_image = pygame.image.load("Space.png")


nave = pygame.image.load("Nave.bmp")
naverect = nave.get_rect()
naverect.x = 320
naverect.y = 420

# Tiro
tiro = pygame.image.load("Nave.bmp")
tiroRect = tiro.get_rect()
tiroRect.x = 0
tiroRect.y = 420


def tiro(x,y):
    screen.blit(tiro, tiroRect)

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
        tiro(naverect.x, tiroRect.y)


    screen.blit(back_image, (0,0))
    screen.blit(nave, naverect)
    pygame.display.flip()

    time.sleep(0.015)