import pygame
import sys

#Inicializamos la libreria
pygame.init()

ancho = 800
alto = 600

#Damos los valores de ancho y alto de la pantalla
surface = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption("Rectangulos")

#Tambien se pueden utilizar tuplas para generar colores
white = (255, 255, 255)
red = (115, 38, 80)
green = (0, 255, 0)

rectangulo = pygame.Rect(100, 150, 120, 60) #(x, y, ancho, alto)
rectangulo.center = (ancho//2, alto//2)

#Rectangulo usando tuplas
#Las desventajas de usar tuplas es que no se pueden utilizar las funciones de pygame
#Como center
rectangulo2 = (100, 100, 80, 40)

#Iniciamos un bucle para mantener la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si el usuario presiona la X
            pygame.quit() #Cierra la ventana
            sys.exit() 
    surface.fill(white) 
    pygame.draw.rect(surface,red,rectangulo) #(surface, color, rectangulo)
    pygame.draw.rect(surface,green,rectangulo2)
    pygame.display.update() #Actualiza la pantalla