import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Imagenes")

white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

#Cargamos nuestra imagen
image = pygame.image.load("images/sol.png")

#Centramos nuestra imagen
rect = image.get_rect()
rect.center = (ancho // 2, alto // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        surface.fill(white)
        surface.blit(image, rect)
    pygame.display.update() 