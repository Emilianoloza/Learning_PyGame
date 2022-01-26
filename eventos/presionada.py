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
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("Arriba")
    if pressed[pygame.K_s]:
        print("Abajo")
    if pressed[pygame.K_a]:
        print("Izquierda")
    if pressed[pygame.K_d]:
        print("Derecha")

    surface.fill(white)
    pygame.display.update() 