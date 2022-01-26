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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    time = pygame.time.get_ticks() // 1000 #Milisegundos
    print(time)
        
    surface.fill(white)
    pygame.display.update() 