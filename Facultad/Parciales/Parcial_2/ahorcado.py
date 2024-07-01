import pygame
import pygame.image
from biblioteca import *
pygame.init() # -> Se inicializa pygame
pygame.mixer.init() # -> Se inicializa el mixer
pygame.mixer.music.set_volume(1.0)
idioma = None
run = True
while run:
    fondo_musica = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Musica\campfire.mp3")
    fondo_musica.set_volume(1.0)
    fondo_musica.play(-1)
    if idioma == None:
        idioma = selector_idioma()    
    opcion = menu_principal(idioma)
    fondo_musica.stop()
    if opcion == "Jugar":
        sub_opcion = juego(idioma)
        if sub_opcion != "Salir":
            if sub_opcion[0] == "Ganaste" or sub_opcion[0] == "Perdiste":
                guardar_puntaje(sub_opcion[1], sub_opcion[2])                
        elif sub_opcion == "Salir":
            run = False
        else:
            pass
    elif opcion == "Puntajes":
        sub_opcion_2 = puntajes(idioma)
        if sub_opcion_2 == "Salir":
            run = False
        else:
            pass
    elif opcion == "Salir":
        run = False
pygame.quit() # -> Se cierra pygame
