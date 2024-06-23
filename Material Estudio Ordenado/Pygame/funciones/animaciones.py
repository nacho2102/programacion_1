import pygame

black = (0, 0, 0) # -> Color negro
white = (255, 255, 255) # -> Color blanco

pygame.init() # -> Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana 
screen_height = 500 # -> Alto de la ventana
screen = pygame.display.set_mode((screen_width, screen_height)) #Se crea una ventana
pos_X = 250
pos_Y = 250
speed_X = 5
speed_Y = 5
pos_rect_X = 250
pos_rect_Y = 250
max_x = False
running = True # -> Variable que se utiliza para detener el bucle 
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
        if event.type == pygame.KEYDOWN: # -> Si el evento es de pulsar una tecla
            if event.key == pygame.K_DOWN: # -> Si el evento es de pulsar una tecla
                pos_Y += speed_Y
            if event.key == pygame.K_UP: # -> Si el evento es de dejar de pulsar una tecla
                pos_Y -= speed_Y
            if event.key == pygame.K_RIGHT: # -> Si el evento es de pulsar una tecla
                pos_X += speed_X
            if event.key == pygame.K_LEFT: # -> Si el evento es de dejar de pulsar una tecla
                pos_X -= speed_X
    screen.fill(white)# Se pinta el fondo de la ventana
    if pos_rect_X < 500 and max_x == False:
        for i in range(0, 481, 1):
            pos_rect_X = i
            if i == 480:
                max_x = True
    elif max_x == True:
        for i in range(480, 9, -1):
            pos_rect_X = i
            if i == 10:
                max_x = False
            
    pygame.draw.rect(screen, (black), (pos_rect_X, pos_rect_Y, 10, 10))
    pygame.draw.circle(screen, (black), (pos_X, pos_Y), 75)    
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # -> Se cierra pygame