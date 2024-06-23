import pygame
from pygame.locals import K_x

pygame.init() #Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
font = pygame.font.SysFont("Arial Narrow", 15) # -> Fuente
text = font.render("HOLA MUNDO", True, (250, 0, 0)) # -> Texto
screen = pygame.display.set_mode((screen_width, screen_height)) # -> Se crea una ventana
screen.blit(text,(250,250)) # -> Rellena la ventana con el texto
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # Fin