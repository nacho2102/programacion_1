import pygame

pygame.init() #Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
screen = pygame.display.set_mode((screen_width, screen_height)) # -> Se crea una ventana
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
    screen.fill((255, 255, 255)) # Se pinta el fondo de la ventana
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75) # Se dibuja un círculo azul en el centro recibienodo por parámetro(pantalla, color, coordenadas, radio)
    pygame.draw.rect(screen, (255, 255, 0), (30, 30, 60, 60)) # Se dibuja un rectángulo amarillo en la esquina inferior izquierda recibienodo por parámetro(pantalla, color, (coordenadas y tamaños))
    pygame.draw.line(screen, (255, 0, 0), (250, 0), (250, 500), 5) # Se dibuja una línea roja por la mitad de la pantalla recibienodo por parámetro(pantalla, color, coordenadas y tamaños)
    pygame.display.flip()# Muestra los cambios en  la pantalla
pygame.quit() # Fin
