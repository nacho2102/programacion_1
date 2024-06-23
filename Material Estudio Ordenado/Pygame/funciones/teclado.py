import pygame
from pygame.locals import K_x

pygame.init() #Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
screen = pygame.display.set_mode((screen_width, screen_height)) # -> Se crea una ventana
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
        if event.type == pygame.KEYDOWN: # -> Si el evento es de pulsar una tecla
            if event.key == pygame.K_x: # -> Si la tecla pulsada es x
                print("La tecla x se ha pulsado") # -> Imprime un mensaje
            print(event.key) # -> Imprime el valor de la tecla pulsada
            print(pygame.key.name(event.key)) # -> Imprime el nombre de la tecla pulsada
        if event.type == pygame.KEYUP: # -> Si el evento es de dejar de pulsar una tecla
            print(event.key) # -> Imprime el valor de la tecla pulsada
        pressed_keys = pygame.key.get_pressed() # -> Obtiene las teclas pulsadas
        if True in pressed_keys: # -> Si hay alguna tecla pulsada
            if pressed_keys[K_x]: # -> Si la tecla pulsada es x
                print("Se presiono la tecla X") # -> Imprime un mensaje
        
    screen.fill((255, 255, 255)) # Se pinta el fondo de la ventana
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # Fin