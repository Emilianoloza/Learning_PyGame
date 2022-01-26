import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Texto")

white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

#Obtenemos la fuente
fuente = pygame.font.Font('freesansbold.ttf', 50)

#Crear el texto
texto = fuente.render("Hola mundo", True, red)
rect = texto.get_rect()
rect.center = (ancho // 2, alto // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        surface.fill(white)
        surface.blit(texto, rect)
    pygame.display.update() 