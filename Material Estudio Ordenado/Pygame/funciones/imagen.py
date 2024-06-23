import pygame

pygame.init() # -> Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana
screen_height = 500 # -> Alto de la ventana
imagen_1 = pygame.image.load("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/Material Estudio Ordenado/Pygame/imagenes/Home.png") # -> Carga la imagen
rescala = pygame.transform.scale(imagen_1,(screen_width,screen_height)) # -> Escala la imagen
screen = pygame.display.set_mode((screen_width, screen_height)) # Se crea una ventana
screen.blit(rescala,(0,0)) # -> Rellena la ventana con la imagen
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # -> Se cierra pygame