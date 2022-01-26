import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Objects")

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
    #draw
    #1.- Donde se pintara la figura
    #2.- Color de la figura

    pygame.draw.rect(surface,red,(100, 100, 80, 40)) 
    pygame.draw.circle(surface,green, (200,300), 100) #(surface, color, (x,y), radio)
    pygame.draw.line(surface,blue,(100,100),(200,300), 2) #(surface, color, (x1,y1), (x2,y2), grosor)

    pygame.display.update() 