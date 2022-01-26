import pygame
import sys

#Inicializamos la libreria
pygame.init()

#Damos los valores de ancho y alto de la pantalla
surface = pygame.display.set_mode((800, 600)) #(ancho, alto)
pygame.display.set_caption("Colores")

#Creamos colores para usar
red = pygame.Color(255, 0, 0) #R, G, B = 0-255
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#Tambien se pueden utilizar tuplas para generar colores
white = (255, 255, 255)

#Iniciamos un bucle para mantener la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si el usuario presiona la X
            pygame.quit() #Cierra la ventana
            sys.exit()
    surface.fill(white) 
    pygame.display.update() #Actualiza la pantalla