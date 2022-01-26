import pygame
import sys

#Inicializamos la libreria
pygame.init()

#Damos los valores de ancho y alto de la pantalla
surface = pygame.display.set_mode((800, 600)) #(ancho, alto)
pygame.display.set_caption("Mi primer juego")

#Iniciamos un bucle para mantener la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #Si el usuario presiona la X
            pygame.quit() #Cierra la ventana
            sys.exit()
    
