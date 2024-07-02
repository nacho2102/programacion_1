import json
import random
import pygame
import pygame.image
from pygame.locals import *

from os import system

def cargar_archivo(archivo_json:json, key):
    with open(archivo_json, "r") as archivo:
        data = json.load(archivo)
        print("Archivo cargado exitosamente")
    return(data[key])

def guardar_json(archivo_json:str, lista:list):
    lista = {"score": lista}
    with open(archivo_json, 'w') as archivo:
        json.dump(lista, archivo, indent=4)

def guardar_puntaje(puntaje, nick):
    score = {"nombre": nick, "puntaje": puntaje}
    lista_score = cargar_archivo(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\score.json", 'score')
    lista_score.append(score)
    guardar_json(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\score.json", lista_score)

def ordenar_scores(archivo_cargado):
    for scores_1 in range(len(archivo_cargado) - 1):
                for scores_2 in range(scores_1 + 1, len(archivo_cargado)):
                            if archivo_cargado[scores_1]['puntaje'] < archivo_cargado[scores_2]['puntaje']:
                                aux = archivo_cargado[scores_1]
                                archivo_cargado[scores_1] = archivo_cargado[scores_2]
                                archivo_cargado[scores_2] = aux
                            elif archivo_cargado[scores_1]['puntaje'] == archivo_cargado[scores_2]['puntaje']:
                                if archivo_cargado[scores_1]['nombre'] < archivo_cargado[scores_2]['nombre']:
                                    aux = archivo_cargado[scores_1]
                                    archivo_cargado[scores_1] = archivo_cargado[scores_2]
                                    archivo_cargado[scores_2] = aux
    return archivo_cargado  

def top_scores(archivo_cargado):
    scores_ordenados = ordenar_scores(archivo_cargado)
    top_scores = scores_ordenados[:5]
    return top_scores
def listar_palabras(archivo_cargado, idioma):
    palabras = []
    for i in archivo_cargado:
        if i[idioma] not in palabras:
            palabras.append(i[idioma])
    return palabras

def aleatorio(palabras):
    if len(palabras) > 0:
        retorno = random.choice(palabras)
        palabras.remove(retorno)
    else:
        retorno = None
    return retorno

def validar_letra(letra_ingresada, palabra):
    posicion = 0
    retorno = False
    posiciones = []
    puntaje = 0
    for i in palabra:
        if letra_ingresada == i:
            posiciones.append(posicion)
            retorno = (letra_ingresada, posiciones)
            puntaje += 1
        posicion += 1
    return retorno, puntaje

def imprimir_lineas(palabra, screen):
    cordenada_x_inicial = 25
    cordenada_x_final = 50
    for i in range(len(palabra)):
        pygame.draw.line(screen, (0, 0, 0), (cordenada_x_inicial, 50), (cordenada_x_final, 50), 5) # Se dibuja una línea roja por la mitad de la pantalla recibienodo por parámetro(pantalla, color, coordenadas y tamaños)
        cordenada_x_inicial += 50
        cordenada_x_final += 50

def imprimir_letras(letra_ingresada, posiciones, screen):
    contador = 0
    for posicion in posiciones:
        contador += 1
        match(posicion):
            case 0:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada.upper(), True, (0, 0, 0)) # -> Texto
                screen.blit(text,(25, 30))
            case 1:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(75, 30))
            case 2:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(125, 30))
            case 3:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(175, 30))
            case 4:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(225, 30))
            case 5:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(275, 30))
            case 6:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(325, 30))
            case 7:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(375, 30))
            case 8:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(425, 30))
            case 9:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(475, 30))
            case 10:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(525, 30))
            case 11:
                font = pygame.font.SysFont("Arial Narrow", 25) # -> Fuente
                text = font.render(letra_ingresada, True, (0, 0, 0)) # -> Texto
                screen.blit(text,(575, 30))
    return contador

def generar_ahorcado(contador, screen):
    if contador == 1:
        error_1 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\1.png")
        error_1 = pygame.transform.scale(error_1,(80, 150))
        screen.blit(error_1,(400, 300))
    elif contador == 2:
        error_2 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\2.png")
        error_2 = pygame.transform.scale(error_2,(80, 150))
        screen.blit(error_2,(400, 300))
    elif contador == 3:
        error_3 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\3.png")
        error_3 = pygame.transform.scale(error_3,(80, 150))
        screen.blit(error_3,(400, 300))
    elif contador == 4:
        error_4 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\4.png")
        error_4 = pygame.transform.scale(error_4,(80, 150))
        screen.blit(error_4,(400, 300))
    elif contador == 5:
        error_5 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\5.png")
        error_5 = pygame.transform.scale(error_5,(80, 150))
        screen.blit(error_5,(400, 300))
    elif contador == 6:
        error_6 = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\6.png")
        error_6 = pygame.transform.scale(error_6,(80, 150))
        screen.blit(error_6,(400, 300))
    pygame.draw.line(screen, (0, 0, 0), (436, 332), (446, 332), 3)
    pygame.draw.line(screen, (0, 0, 0), (440, 284), (440, 303), 3)

def ingresar_nombre(screen, menu, idioma, retorno):
    font_1 = pygame.font.SysFont("Arial Narrow", 50) # -> Fuente
    font_2 = pygame.font.SysFont("Arial Narrow", 30) # -> Fuente
    match(idioma):
        case "ES":
            match(retorno):
                case "Ganaste":
                    text_ganaste_perdiste = font_1.render("GANASTE!", True, (252, 227, 3))
                    text_nick = font_2.render("Ingrese su NICK", True, (0, 0, 0))
                case "Perdiste":
                    text_ganaste_perdiste = font_1.render("PERDISTE!", True, (250, 0, 0))
                    text_nick = font_2.render("Ingrese su NICK", True, (0, 0, 0))
                
        case "EN":  
            match(retorno):
                case "Ganaste":
                    text_ganaste_perdiste = font_1.render("YOU WIN!", True, (252, 227, 3))
                    text_nick = font_2.render("Enter your NICK", True, (0, 0, 0))
                case "Perdiste":
                    text_ganaste_perdiste = font_1.render("YOU LOSE!", True, (250, 0, 0))
                    text_nick = font_2.render("Enter your NICK", True, (0, 0, 0))
    screen.blit(text_ganaste_perdiste,(300,180))
    screen.blit(text_nick,(300,212))
    nick = []
    letra = None
    pos_x = 300
    menu_r = menu
    ingresar_nombre = True
    while ingresar_nombre:
        for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
            if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
                retorno = "Salir"
                ingresar_nombre = False
            if event.type == MOUSEBUTTONDOWN:
                if menu_r.collidepoint(event.pos):
                    retorno = "Menu"
                    ingresar_nombre = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nick = "".join(nick)
                    retorno = nick
                    ingresar_nombre = False
                else:
                    letra = pygame.key.name(event.key)
                    if len(letra) == 1:  # Verifica si `letra` es un solo carácter
                        nick.append(letra)
                        font = pygame.font.SysFont("Arial Narrow", 50)  # Fuente
                        text = font.render(letra, True, (250, 0, 0))
                        screen.blit(text, (pos_x, 250))
                        pos_x += 50  # Mover la posición para la siguiente letra
        pygame.display.flip()
    return retorno 
    

def config_juego(palabras, screen):
    screen_width = 800 # -> Ancho de la ventana 
    screen_height = 600 # -> Alto de la ventana
    jugar_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\Fondo.gif")
    jugar_fondo = pygame.transform.scale(jugar_imagen,(screen_width, screen_height))
    menu_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\menu.png")
    menu_r = pygame.transform.scale(menu_imagen,(150, 125))
    rect_menu = menu_r.get_rect()
    rect_menu.centerx = (100)
    rect_menu.centery = (550)
    screen.blit(jugar_fondo,(0,0))
    screen.blit(menu_r, rect_menu)
    palabra = aleatorio(palabras)
    if palabra != None:
        imprimir_lineas(palabra, screen)
    else:
        print("No hay palabras")
        palabra = None
    return palabra, rect_menu

def selector_idioma():
    screen_width = 800 # -> Ancho de la ventana 
    screen_height = 600 # -> Alto de la ventana
    fuente = pygame.font.SysFont("Times New Roman", 40) # -> Fuente
    texto_seleccion = fuente.render("Seleccione || Select", True, (255, 0, 0)) # -> Texto\
    texto_seleccion_2 = fuente.render("Idioma || Language", True, (255, 0, 0))
    texto_idioma_es = fuente.render("Español", True, (255, 0, 0))
    texto_idioma_en = fuente.render("English", True, (255, 0, 0))
    imagen_menu = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Menu.gif")
    menu = pygame.transform.scale(imagen_menu,(screen_width, screen_height))
    imagen_idioma_es = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Idiomas\Español.jpg")
    idioma_es = pygame.transform.scale(imagen_idioma_es,(100, 50))
    rect_idioma_es = idioma_es.get_rect()
    rect_idioma_es.center = (250, 400)
    imagen_idioma_en = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Idiomas\Ingles.jpg")
    idioma_en = pygame.transform.scale(imagen_idioma_en,(100, 50))
    rect_idioma_en = idioma_en.get_rect()
    rect_idioma_en.center = (550, 400)
    screen = pygame.display.set_mode((screen_width, screen_height)) #Se crea una ventana
    pygame.display.set_caption("Ahorcado") # -> Se pone el nombre de la ventana
    screen.blit(menu,(0,0)) # -> Rellena la ventana con la imagen
    screen.blit(texto_seleccion,(200, 100)) # -> Rellena la ventana con el texto_seleccion
    screen.blit(texto_seleccion_2,(260, 150)) 
    screen.blit(texto_idioma_es,(185, 325)) 
    screen.blit(texto_idioma_en,(490, 325)) 
    screen.blit(idioma_es, rect_idioma_es) 
    screen.blit(idioma_en, rect_idioma_en) 
    pantalla_idioma = True
    idioma = None 
    while pantalla_idioma:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantalla_idioma = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if rect_idioma_es.collidepoint(event.pos):
                    print("CLICK ES")
                    idioma = "ES"
                    pantalla_idioma = False
                if rect_idioma_en.collidepoint(event.pos):
                    print("CLICK EN")
                    idioma = "EN"
                    pantalla_idioma = False
        pygame.display.flip()
    return idioma

def menu_principal(idioma):
    menu_principal = True
    screen_width = 800 # -> Ancho de la ventana 
    screen_height = 600 # -> Alto de la ventana
    screen = pygame.display.set_mode((screen_width, screen_height))
    if idioma == "ES": #Se crea una ventana
        imagen_menu = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Menu.gif")
        jugar_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Español\Jugar.png")
        puntajes_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Español\Puntaje.png")
        salir_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Español\Salir.png")
    elif idioma == "EN":
        imagen_menu = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Menu.gif")
        jugar_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Ingles\Play.png")
        puntajes_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Ingles\Scores.png")
        salir_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\Ingles\Exit.png")
    menu = pygame.transform.scale(imagen_menu,(screen_width, screen_height))       
    jugar = pygame.transform.scale(jugar_imagen,(100, 50))
    rect_jugar = jugar.get_rect()
    rect_jugar.center = (400, 100)
    puntajes = pygame.transform.scale(puntajes_imagen,(150, 50))
    rect_puntajes = puntajes.get_rect()
    rect_puntajes.center = (400, 300)
    salir = pygame.transform.scale(salir_imagen,(100, 50))
    rect_salir = salir.get_rect()
    rect_salir.center = (400, 500)
    screen = pygame.display.set_mode((screen_width, screen_height)) #Se crea una ventana
    pygame.display.set_caption("Ahorcado") # -> Se pone el nombre de la ventana
    screen.blit(menu,(0,0))
    screen.blit(jugar, rect_jugar)
    screen.blit(puntajes, rect_puntajes)
    screen.blit(salir, rect_salir)
    while menu_principal:
        for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
            if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
                menu_principal = False # -> Se detiene el bucle
            if event.type == pygame.MOUSEBUTTONDOWN :
                if rect_jugar.collidepoint(event.pos):
                    print("CLICK JUGAR")
                    retorno = "Jugar"
                    menu_principal = False
                if rect_puntajes.collidepoint(event.pos):
                    print("CLICK PUNTUAJE")
                    retorno = "Puntajes"
                    menu_principal = False
                if rect_salir.collidepoint(event.pos):
                    print("CLICK SALIR")
                    retorno = "Salir"
                    menu_principal = False
        pygame.display.flip() # -> Actualiza la ventana
    return retorno

def juego(idioma):
    fondo_musica = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Musica\cherryblossom.mp3")
    fondo_musica.set_volume(0.7)
    fondo_musica.play(-1)
    jugar = True
    archivo = cargar_archivo(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\datos.json", 'ahorcado')
    palabras = listar_palabras(archivo, idioma)
    print(palabras)
    screen_width = 800 # -> Ancho de la ventana 
    screen_height = 600 # -> Alto de la ventana
    screen = pygame.display.set_mode((screen_width, screen_height))
    puntaje_total = 0
    while jugar:
        configurar = True
        while configurar:
            config = config_juego(palabras, screen)
            configurar = False
        font = pygame.font.SysFont("Arial Narrow", 50) # -> Fuente
        text = font.render(str(puntaje_total), True, (250, 0, 0))
        screen.blit(text,(700,500))
        palabra = config[0]
        if palabra == None:
            retorno = "Ganaste"
            menu = config[1]
            nick = ingresar_nombre(screen, menu, idioma, retorno)
            if nick != "Menu" and nick !="Salir":                
                retorno = "Ganaste", puntaje_total, nick
            elif nick == "Menu":
                error_sonido.stop()
                fondo_musica.stop()
                retorno = "Menu"
            else:
                error_sonido.stop()
                fondo_musica.stop()
                retorno = "Salir"                
            print("Fin de juego")
            jugar = False
        else:
            print(palabra)
            menu = config[1]
            juego = True
            contador_letras = 0
            contador = 0
            puntaje = 0
            repetida = None
            while juego:
                for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
                    if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
                        retorno = "Salir"
                        juego = False # -> Se detiene el bucle
                    if event.type == pygame.KEYDOWN: # -> Si el evento es de dejar de pulsar una tecla
                        letra = pygame.key.name(event.key)
                        validacion = validar_letra(letra, palabra)[0]
                        if validacion != False and letra != repetida:
                            repetida = letra
                            contador_letras += imprimir_letras(letra,validacion[1],screen)
                            puntaje += validar_letra(letra, palabra)[1]
                            if contador_letras == len(palabra):
                                efecto_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\success.mp3")
                                efecto_sonido.set_volume(0.5)
                                efecto_sonido.play()
                                retorno = "Siguiente"
                                juego = False
                        elif validacion == False:
                            contador = contador + 1
                            generar_ahorcado(contador, screen)
                            match(contador):
                                case 1:
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\latido.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play(-1)
                                case 2:
                                    error_sonido.stop()
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\latido_2.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play(-1)
                                case 3:
                                    error_sonido.stop()
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\latido_3.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play(-1)
                                case 4:
                                    error_sonido.stop()
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\latido_4.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play(-1)
                                case 5:
                                    error_sonido.stop()
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\latido_5.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play(-1)
                                case 6:
                                    error_sonido.stop()
                                    error_sonido = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Efectos\Juego\game_over.mp3")
                                    error_sonido.set_volume(1.0)
                                    error_sonido.play()
                                    retorno = "Perdiste"
                                    juego = False
                    if event.type == pygame.MOUSEBUTTONDOWN :
                        if menu.collidepoint(event.pos):
                            print("CLICK MENU")
                            retorno = "Menu"  
                            juego = False
                pygame.display.flip()
            if retorno == "Menu":
                fondo_musica.stop()
                if contador != 0:
                    error_sonido.stop()
                jugar = False
            elif retorno == "Perdiste":
                print("Perdiste")
                nick = ingresar_nombre(screen, menu, idioma, retorno)
                if nick != "Menu" and nick !="Salir":                
                    puntaje_total += puntaje
                    retorno = "Perdiste", puntaje_total, nick
                elif nick == "Menu":
                    retorno = "Menu"
                else:
                    retorno = "Salir" 
                error_sonido.stop()
                fondo_musica.stop()
                jugar = False
            elif retorno == "Siguiente":
                if contador != 0:
                    error_sonido.stop()
                puntaje_total += puntaje
                pass
            elif retorno == "Salir":                   
                retorno == "Salir"
                error_sonido.stop()
                fondo_musica.stop()
                jugar = False
            pygame.display.flip()
    return retorno
    
def puntajes(idioma):
    fondo_musica = pygame.mixer.Sound(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\sonidos\Musica\cherryblossom.mp3")
    fondo_musica.set_volume(1.0)
    fondo_musica.play(-1)
    scores = cargar_archivo(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\score.json", 'score')
    top_5_scores = top_scores(scores)
    print(top_5_scores)
    screen_width = 800 # -> Ancho de la ventana 
    screen_height = 600 # -> Alto de la ventana
    jugar_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Juego\Fondo.gif")
    jugar_fondo = pygame.transform.scale(jugar_imagen,(screen_width, screen_height))
    menu_imagen = pygame.image.load(r"C:\Users\nacho\OneDrive\Escritorio\Facultad\1er Cuatrimestre\Programacion 1\Facultad\Parciales\Parcial_2\imagenes\Menu\menu.png")
    menu_r = pygame.transform.scale(menu_imagen,(150, 125))
    rect_menu = menu_r.get_rect()
    rect_menu.centerx = (100)
    rect_menu.centery = (550)
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(jugar_fondo,(0,0))
    screen.blit(menu_r, rect_menu)
    pos_y = 100
    font = pygame.font.SysFont("Arial Narrow", 75) # -> Fuente
    text = font.render(f"TOP 5", True, (250, 0, 0))
    screen.blit(text,(100,25))
    contador = 0
    color_1 = 0
    color_2 = 0
    color_3 = 0
    for score in top_5_scores:
        font = pygame.font.SysFont("Arial Narrow", 50) # -> Fuente
        match(idioma):
            case "ES":
                text = font.render(f"{score['nombre'].upper()} | PUNTAJE:{score['puntaje']}", True, (color_1, color_2, color_3))
            case "EN":
                text = font.render(f"{score['nombre'].upper()} | SCORE:{score['puntaje']}", True, (color_1, color_2, color_3))
        screen.blit(text,(100,pos_y))
        pos_y += 50
        if contador == 1:
            color_1 = 255
            color_2 = 255
            color_3 = 255
        elif contador == 2:
            color_1 = 255
            color_2 = 0
            color_3 = 0
        elif contador == 3:
            color_1 = 0
            color_2 = 255
            color_3 = 0
        else:
            color_1 = 0
            color_2 = 0
            color_3 = 255
        contador += 1
    puntajes = True
    while puntajes:
        for event in pygame.event.get(): # -> Cuerpo del bucle para eventos
            if event.type == pygame.QUIT: # -> Si el evento es de cerrar la ventana
                puntajes = False # -> Se detiene el bucle
                retorno = "Salir"
            if event.type == pygame.MOUSEBUTTONDOWN :
                if rect_menu.collidepoint(event.pos):
                    print("CLICK MENU")
                    retorno = "Menu"
                    puntajes = False
        pygame.display.flip()
    fondo_musica.stop()
    return retorno