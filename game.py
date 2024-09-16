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
inicialRedimencionado = pygame.transform.scale(inicial, (630, 450))
inicialRect = inicialRedimencionado.get_rect()

# Nave
nave = pygame.image.load("img/ship.png")
naverect = nave.get_rect()
naverect.x = 320
naverect.y = 420
pontos = 0
fontePontos = pygame.font.Font(None, 32)
text_color = (0, 255, 150)


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

def criarMonstro():
    monstro = pygame.image.load("img/invader0.png")
    monstroRedimencionado = pygame.transform.scale(monstro, (60, 60))
    monstroRect = monstroRedimencionado.get_rect()
    monstroRect.x = random.randint(10,600)
    monstroRect.y = random.randint(50,300)
    listaMonstros.append(monstroRedimencionado)
    listaMonstrosRect.append(monstroRect)

for i in range(0, 20):
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
        if event.type == pygame.QUIT or qtdVidas == 0:
            pygame.quit()
            sys.quit()
    if estado == "menu":
        screen.blit(inicialRedimencionado, inicialRect)
        if keys[pygame.K_SPACE]:
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
        
        # Verifica se a bala acertou o monstro, se sim, destroi
    
        if balaAcertouMonstro():
            pontos += 10

        if balaAcertouNave():
            qtdVidas -= 1
        

        # Deixa so um monstro atirar por vez 
        if tiroMRect.y > 430:
            monstroAtirar(len(listaMonstrosRect), listaMonstrosRect)
    
        tiroRect.y -= 10
        tiroMRect.y += 5

        text = fontePontos.render("Pontuação: " + str(pontos), True, (255,255,0))

        # mostrarVidas(vidas)

        screen.blit(back_image, (0,0))
        screen.blit(nave, naverect)
        screen.blit(text, (10, 10))
        
        mostrarMonstros()
        desenharTiroPlayer()
        desenharTiroMonstro()
        if qtdVidas == 0:
            text = fontePontos.render("GAME OVER", True, (255,255,0))
            screen.blit(back_image, (0,0))
            screen.blit(text, (250, 240))
            time.sleep(0.5)
            estado = "finish"
      
        mostrarVidas(qtdVidas)

    pygame.display.flip()

    time.sleep(0.015)