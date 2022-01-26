import pygame
import sys

pygame.init()

ancho = 800
alto = 600

surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Mover imagen por teclado")

white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)
blue = (0, 0, 255)

image = pygame.image.load("images/sol.png")
rect = image.get_rect()
rect.center = (ancho // 2, alto // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        rect.y -= 5
    if pressed[pygame.K_a]:
        rect.x -= 5
    if pressed[pygame.K_s]:
        rect.y += 5
    if pressed[pygame.K_d]:
        rect.x += 5

    #Validaciones
    if rect.left < 0:
        rect.left = 0
    if rect.right > ancho:
        rect.right = ancho
    
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > alto:
        rect.bottom = alto

    surface.fill(white)
    surface.blit(image, rect)
    pygame.display.update() 