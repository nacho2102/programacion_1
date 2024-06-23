import pygame

pygame.init() # -> Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
screen = pygame.display.set_mode((screen_width, screen_height)) #Se crea una ventana
pygame.display.set_caption("Nombre de la ventana") # -> Se pone el nombre de la ventana
running = True # -> Variable que se utiliza para detener el bucle 
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
    screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # -> Se cierra pygame
