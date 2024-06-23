import pygame

pygame.init() # -> Se inicializa pygame
screen_width = 500 # -> Ancho de la ventana
screen_height = 500 # -> Alto de la ventana
imagen_1 = pygame.image.load("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/Material Estudio Ordenado/Pygame/imagenes/Home.png") # -> Carga la imagen
pj = pygame.image.load("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/Material Estudio Ordenado/Pygame/imagenes/pj.png") # -> Carga la imagen del pj
roca = pygame.image.load("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/Material Estudio Ordenado/Pygame/imagenes/roca.png") # -> Carga la imagen de la roca
pj_r = pygame.transform.scale(pj,(50,75)) # -> Escala la imagen
roca_r = pygame.transform.scale(roca,(50,75)) # -> Escala la imagen
rect_pj = pj_r.get_rect() # -> Crea un rectángulo del pj
rect_pj.centerx = 200
rect_pj.centery = 250
rect_roca = roca_r.get_rect() # -> Crea un rectángulo de la roca
rect_roca.center = (300, 250) # -> Centra la roca
rescala = pygame.transform.scale(imagen_1,(screen_width,screen_height)) # -> Escala la imagen
screen = pygame.display.set_mode((screen_width, screen_height)) # Se crea una ventana
screen.blit(rescala,(0,0)) # -> Rellena la ventana con la imagen
screen.blit(pj_r,rect_pj) # -> Rellena la ventana con el pj
screen.blit(roca_r,rect_roca) # -> Rellena la ventana con la roca
running = True # -> Variable que se utiliza para detener el bucle
while running: # -> Cuerpo del bucle
    for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
        if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
            running = False # -> Se detiene el bucle
        if event.type == pygame.MOUSEBUTTONDOWN :
            if rect_pj.collidepoint(event.pos):
                print("CLICK sobre el jugador")
            if rect_roca.collidepoint(event.pos):
                print("CLICK sobre la roca")
        if rect_pj.colliderect(rect_roca) != True:
            if event.type == pygame.KEYDOWN: # -> Si el evento es de pulsar una tecla
                if event.key == pygame.K_UP: # -> Si la tecla pulsada es arriba
                    print("Arriba") # -> Imprime un mensaje
                    rect_pj.centery = rect_pj.centery - 5
                if event.key == pygame.K_DOWN: # -> Si la tecla pulsada es abajo
                    print("Abajo") # -> Imprime un mensaje
                    rect_pj.centery = rect_pj.centery + 5
                if event.key == pygame.K_LEFT: # -> Si la tecla pulsada es izquierda
                    print("Izquierda") # -> Imprime un mensaje
                    rect_pj.centerx = rect_pj.centerx - 5                
                if event.key == pygame.K_RIGHT: # -> Si la tecla pulsada es derecha
                    print("Derecha") # -> Imprime un mensaje
                    rect_pj.centerx = rect_pj.centerx + 5             
    screen.blit(rescala,(0,0))
    screen.blit(roca_r,rect_roca)            
    screen.blit(pj_r,rect_pj)
    pygame.display.flip() # -> Actualiza la ventana
pygame.quit() # -> Se cierra pygame