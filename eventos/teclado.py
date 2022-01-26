import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Eventos del Teclado")

white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = 'Izquierda'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = 'Derecha'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = 'Arriba'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = 'Abajo'
            print(message)

        if event.type == pygame.KEYUP:
            #print('Tecla soltada')
            pass
    surface.fill(white)
    pygame.display.update() 