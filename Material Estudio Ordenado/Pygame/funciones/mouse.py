import pygame

pygame.init() #Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
screen = pygame.display.set_mode((screen_width, screen_height)) # -> Se crea una ventana
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    pygame.mouse.set_visible(False) # -> Oculta el mouse
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
        if event.type == pygame.MOUSEBUTTONDOWN : # -> Si el evento es de pulsar el mouse
            print(event.pos) # -> Imprime la coordenada del mouse
        if event.type == pygame.MOUSEBUTTONUP : # -> Si el evento es de dejar de pulsar el mouse
            print(event.pos) # -> Imprime la coordenada del mouse
        if event.type == pygame.MOUSEMOTION : # -> Si el evento es de mover el mouse
            print(event.pos) # -> Imprime la coordenada del mouse
            pygame.mouse.set_visible(True) # -> Muestra el mouse
        if event.type == pygame.MOUSEWHEEL : # -> Si el evento es de hacer scroll
            print(event.y) # -> Imprime el valor del scroll, 1 para arriba y -1 para abajo
    screen.fill((255, 255, 255)) # Se pinta el fondo de la ventana
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # Fin