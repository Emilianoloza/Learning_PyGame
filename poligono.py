import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Poligonos")

white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 
    surface.fill(white) 
    #Triangulo
    #(surface, color, (x1,y1), (x2,y2), (x3,y3))
    pygame.draw.polygon(surface,blue,((0,400),(100,300),(200,400)))

    #Pentagono
    #(surface, color, (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5))
    pygame.draw.polygon(surface,red,((146,0),(291,106),(236,277),(56,277),(0,106)))

    pygame.display.update() 