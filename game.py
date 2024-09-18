import pygame
import time
import sys
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width,height))
back_image = pygame.image.load("img/Space.png")

# Imagem Inicial
inicial = pygame.image.load("img/logo.png")
inicialRedimencionado = pygame.transform.scale(inicial, (630, 350))
inicialRect = inicialRedimencionado.get_rect()

# Nave
nave = pygame.image.load("img/ship.png")
naverect = nave.get_rect()
naverect.x = 320
naverect.y = 420
pontos = 0
fontePontos = pygame.font.Font(None, 32)
text_color = (0, 255, 150)

# Vidas

qtdVidas = 3
vidas = pygame.image.load("img/heart.png")
vidasRedimencionadas = pygame.transform.scale(vidas, (25,25))
vidasRect = vidasRedimencionadas.get_rect()
vidasRect.x = 600
vidasRect.y = 10

# Tiro Monstro
tiroM = pygame.image.load("img/bala.png")
tiroMRedimencionado = pygame.transform.scale(tiroM, (30,30))
tiroMRect = tiroMRedimencionado.get_rect()

def desenharTiroMonstro():
    screen.blit(tiroMRedimencionado, tiroMRect)

# Tiro player
tiro = pygame.image.load("img/bala.png")
tiroRedimencionado = pygame.transform.scale(tiro, (30,30))
tiroRect = tiroRedimencionado.get_rect()

def desenharTiroPlayer():
    screen.blit(tiroRedimencionado, tiroRect)

# Monstro
listaMonstrosRect = []
listaMonstros = []

def desenharMonstro(i):
    monstro = pygame.image.load("img/invader0.png")
    monstroRedimencionado = pygame.transform.scale(monstro, (60, 60))
    monstroRect = monstroRedimencionado.get_rect()

    if i <= 4:
        monstroRect.x = 85 + i*100
        monstroRect.y = 40
    elif i >= 5 and i <= 9:
        monstroRect.x = i*100 - 415
        monstroRect.y = 130
    elif i >= 10 and i <= 14:
        monstroRect.x = i*100 - 915
        monstroRect.y = 220
    elif i >= 15:
        monstroRect.x = i*100 - 1415
        monstroRect.y = 320

    listaMonstros.append(monstroRedimencionado)
    listaMonstrosRect.append(monstroRect)

def criarMonstro():
    for i in range(0, 20):
        desenharMonstro(i)

criarMonstro()
def mostrarMonstros():
    for i in range(0,len(listaMonstrosRect)):
        screen.blit(listaMonstros[i], listaMonstrosRect[i])

def monstroAtirar(qtdMonstrosVivos, listaMonstrosRect):        
    monstroAleatorio = random.randint(0,qtdMonstrosVivos-1)
    tiroMRect.x = listaMonstrosRect[monstroAleatorio].x + 15
    tiroMRect.y = listaMonstrosRect[monstroAleatorio].y

monstroAtirar(20, listaMonstrosRect)

def balaAcertouMonstro():
    acertou = False
    acertado = 0
    for i in range(0, len(listaMonstrosRect)):
        x = listaMonstrosRect[i].x
        y = listaMonstrosRect[i].y
        crop = pygame.Rect((x, y), (30, 30))
        if tiroRect.colliderect(crop):
            acertou = True
            acertado = i

    if acertou:
        listaMonstrosRect.pop(acertado)
    
    return acertou

def balaAcertouNave():
    x = naverect.x
    y = naverect.y
    crop = pygame.Rect((x,y+40), (30,30))
    if tiroMRect.colliderect(crop):
        return True

def mostrarVidas(vidas):
    for x in range(0,vidas):    
        vidasRect.x = 600 - x*50
        vidasRect.y = 10
        screen.blit(vidasRedimencionadas, vidasRect)

estado = "menu"

while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if estado == "menu":
        screen.blit(inicialRedimencionado, inicialRect)
        text = fontePontos.render("aperte 'P' para começar",  True, (255,255,0))
        screen.blit(text, (200, 400))
        if keys[pygame.K_p]:
            estado = "jogando"

    if estado == "jogando":
        if keys[pygame.K_a]:
            naverect.x -= 5
            if naverect.left < 0:
                naverect.x = 0
            
        if keys[pygame.K_d]:
            naverect.x += 5
            if naverect.right > 640:
                naverect.right = 640
        
        if keys[pygame.K_SPACE]:
            tiroRect.x = naverect.x + 9 # + 9 para ficar no centro da nave
            tiroRect.y = 420
        
        tiroRect.y -= 10
        tiroMRect.y += 5

        if balaAcertouMonstro():
            pontos += 10
            tiroRect.y = -40

        if balaAcertouNave():
            qtdVidas -= 1

        # Deixa so um monstro atirar por vez 
        if tiroMRect.y > 430:
            monstroAtirar(len(listaMonstrosRect), listaMonstrosRect)

        text = fontePontos.render("Pontuação: " + str(pontos), True, (255,255,0))

        screen.blit(back_image, (0,0))
        screen.blit(nave, naverect)
        screen.blit(text, (10, 10))
        
        mostrarMonstros()
        desenharTiroPlayer()
        desenharTiroMonstro()
        mostrarVidas(qtdVidas)

        if pontos == 200:
            estado = "acabou"
            text = fontePontos.render("YOU WIN, aperte 'R' para reiniciar", True, (255,255,0))

        if qtdVidas == 0:
            estado = "acabou"
            text = fontePontos.render("GAME OVER, aperte 'R' para reiniciar", True, (255,255,0))
            qtdVidas = 3
            
    elif estado == "acabou":
        
        screen.blit(back_image, (0,0))
        screen.blit(text, (130, 220))
        
        if keys[pygame.K_r]:
            screen.blit(back_image, (0,0))
        
            estado = "menu"
            listaMonstros.clear()
            listaMonstrosRect.clear()
            pontos = 0
            vidas = 3
            criarMonstro()
        
    pygame.display.flip()
    
    time.sleep(0.015) 
