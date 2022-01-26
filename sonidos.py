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

#Cargamos nuestro sonido
pygame.mixer.music.load("sounds/moneda.mp3")
#Configuramos el volumen
pygame.mixer.music.set_volume(1) #Float -> 0.0 - 1.0
#Reproducimos el sonido
pygame.mixer.music.play(2, 0.0) #Reproduce el sonido 2 veces, y comenzará en 0.0 segundos

#Funciones extras para manipular la reproduccion
pygame.mixer.music.stop() #Detenemos la reproduccion
pygame.mixer.music.pause() #Pausa la reproduccion
pygame.mixer.music.rewind() #Reinicia la reproduccion
pygame.mixer.music.fadeout(500) #Fadeout de 500 milisegundos

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        
    surface.fill(white)
    pygame.display.update() 