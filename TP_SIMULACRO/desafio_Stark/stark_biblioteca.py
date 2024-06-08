from os import system
from data_Stark_3 import *
import json


def promedio_por_genero (diccionario:dict,clave:str,genero:str)->float:
    contador = 0
    acumulador_fuerza = 0

    for datos in diccionario:
        for key in datos.keys():
            if key == clave and  datos['genero'] == genero:
                acumulador_fuerza = acumulador_fuerza + float(datos[key])
                contador = contador + 1

    if contador > 0 :
        return acumulador_fuerza / contador
    
def clave_max_min_genero (diccionario:dict, clave:str, genero:str, comparacion:str):
    bandera = True
    for personaje in diccionario:
        if personaje["genero"] == genero:
            if comparacion == "MAX":
                if bandera == True or float(personaje[clave]) > clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
            elif comparacion == "MIN":
                if bandera == True or float(personaje[clave]) < clave_maxima:
                    clave_maxima = float(personaje[clave])
                    nombre = personaje["nombre"]
                    bandera = False
    if bandera == True:
        nombre = "No hay personajes con este genero"
    return nombre

def pausa():
    var = input("Presione Enter para continuar...")
    system ("cls")

def listar_por_caracteristica(lista:list, clave_a_buscar:str):
    diccionario_auxiliar = {}

    for personaje in lista:
        clave = personaje[clave_a_buscar].capitalize()
        if clave != "":
            if clave in diccionario_auxiliar:
                diccionario_auxiliar[clave] += " - " + personaje["nombre"]
            else:
                diccionario_auxiliar[clave] = personaje["nombre"]


    for clave, nombres in diccionario_auxiliar.items():
        print(f"{clave}: {nombres}")
        print ("------------------------")
    
def contar_por_caracteristica (lista:list, clave:str):
    lista_auxiliar = []
    print("Color\t\t\t\tCantidad")
    print("----------------------------------------")
    for personaje in lista:
        lista_auxiliar.append(personaje[clave].capitalize())
    set_auxiliar = set(lista_auxiliar)
    for caracteristica in set_auxiliar:
        contador = 0 
        for personaje in lista:
            if caracteristica == personaje[clave].capitalize():
                contador += 1 
        if len(caracteristica) < 10:
            print(f"{caracteristica}\t\t\t\t{contador}")
        else:
            print(f"{caracteristica}\t\t\t{contador}")

def stark_normalizar_datos (lista:list):
    """_summary_
    Recibe como parametro una lista y convierte todos los value numericos de string a entero o flotante segun cada caso.
    Args:
        lista (list): Recibe una lista de diccionarios a recorrer

    Returns:
        bool: Devuelve un booleano, si hace el casteo sera True, si es una lista vacia o si los datos ya fueron normalizados retornara False.
    """    
    retorno = False
    for personaje in lista:
        for key in personaje.keys():
            if type(personaje[key]) != type(int) or type(personaje[key]) != type(float):               
                if personaje[key].isdigit():
                    personaje[key] = int(personaje[key])
                    retorno = True
                else:
                    flag_2 = False
                    flag = False
                    for letra in personaje[key]:
                        if letra.isdigit() == True:
                            flag = True
                        elif letra == ".":
                            flag_2 = True
                        else:
                            flag = False
                    if flag and flag_2:
                        personaje[key] = float(personaje[key])
                        retorno = True
    if retorno == True:
        print("Datos Normalizados")
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    return retorno

"""1.1. Crear la función ”obtener_dato()” la cual recibirá por parámetro un
diccionario el cual representara a un héroe y también recibirá un string que
hace referencia a una “clave” del mismo
Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
llamada “nombre”. Caso contrario la función retornara un False"""

def obtener_dato(diccionario:dict, clave:str) -> bool:
    retorno = False
    if len(diccionario) != 0 and "nombre" in diccionario.keys():
        retorno = diccionario[clave]
        
    return retorno


"""Crear la función 'obtener_nombre" la cual recibirá por parámetro un diccionario el
cual representara a un héroe y devolverá un string el cual contenga su nombre
formateado de la siguiente manera:
Nombre: Howard the Duck
Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
contrario la función retornara un False"""

def obtener_nombre(superheroe:dict) -> str | bool:
    retorno = obtener_dato(superheroe, "nombre")
    if retorno != False:
        retorno = "Nombre: " + retorno

    return retorno
    

"""2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
diccionario el cual representara a un héroe y una key (string) la cual
representará el dato que se desea obtener.
    La función deberá devolver un string el cual contenga el nombre y dato
(key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
CUALQUIER OTRO DATO.
●   El string resultante debe estar formateado de la siguiente manera:
(suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
● Validar siempre que la lista no este vacía. Caso contrario la función
retornara un False
NOTA: Reutilizar las funciones del punto anterior"""

def obtener_nombre_y_dato(diccionario:dict, clave_a_obtener):
    retorno = False
    nombre = obtener_nombre(diccionario)
    clave = obtener_dato(diccionario, clave_a_obtener)

    if nombre != False and clave != False:
        retorno = f"{nombre} | {clave_a_obtener}: {clave}"

    return retorno

#print(obtener_nombre_y_dato(lista_personajes[0], "fuerza"))

"""3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
una key (string) la cual representará el dato al cual se le debe calcular su cantidad
MÁXIMA.
● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
un int o un float. Caso contrario la función retornara un False
● En caso de que el dato que se está buscando en el diccionario es de tipo int o
float retornar el mayor que haya encontrado en la búsqueda.
"""

def obtener_maximo(lista:list, clave:str):
    retorno = False
    flag = True
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):
                break
            if flag == True or personaje[clave] > retorno:
                retorno = personaje[clave]
                flag = False

    return retorno

#stark_normalizar_datos(lista_personajes)
#print(lista_personajes[0])

#print(obtener_maximo(lista_personajes, "fuerza"))


"""3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
una key (string) la cual representará el dato al cual se le debe calcular su cantidad
MÍNIMA.
● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
un int o un float. Caso contrario la función retornara un False
● En caso de que el dato que se está buscando en el diccionario es de tipo int o
float retornar el menor que haya encontrado en la búsqueda."""

def obtener_minimo(lista:list, clave:str):
    retorno = False
    flag = True
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):
                break
            if flag == True or personaje[clave] < retorno:
                retorno = personaje[clave]
                flag = False

    return retorno

#print(lista_personajes[0])
#print(obtener_minimo(lista_personajes, "fuerza"))


"""3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
● La lista de héroes
● Un número que me indique el valor a buscar (puede ser la altura
máxima, la altura mínima o cualquier otro dato)
● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan
con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
3.2
Ejemplo de llamada:
mayor_altura=obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
correspondiente a la altura máxima, y la misma función me podria servir tanto como
para altura menor, como la mayor o alguna altura que yo le especifique también.
"""
def obtener_dato_cantidad(lista:list, numero:int, clave:str):
    lista_numeros = []
    for personaje in lista:
        if personaje[clave] == numero:
            lista_numeros.append(personaje)
    return lista_numeros

""""
3.4 Crear la función 'stark_imprimir_heroes' la cual recibirá un parametro:
● La lista de héroes
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
contrario no hará nada y retornara False
En caso de que la lista no este vacia imprimir la información completa de
todos los heroes de la lista que se le pase
Ejemplo de llamada:
mas_pesado=obtener_maximo(lista_heroes,”peso”)
lista_mas_pesados='obtener_dato_cantidad(lista_heroes,mas_pesado,”peso”)
stark_imprimir_heroes(lista_mas_pesados)->Imprimosóloloshéroesmáspesados
stark_imprimir_heroes(lista_heroes)->Imprimotodosloshéroes
"""
def stark_imprimir_heroes(lista:list):

    if len(lista) == 0:
        return False
    for personaje in lista:
        print("-----------------")
        for clave, valor in personaje.items():
            print(f"{clave.capitalize()}: {valor}")
"""
4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de
héroes y un string que representara el dato/key de los héroes que se requiere sumar.
Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes
de hacer la suma. La función deberá retorna la suma de todos los datos según la key
pasada por parámetro

"""

def sumar_dato_heroe(lista:list, clave:str):
    acumulador = 0
    for personaje in lista:
        if len(personaje) == 0 or type(personaje) != type(dict()):
            break
        
        acumulador += personaje[clave]
    return acumulador

#print(sumar_dato_heroe(lista_personajes, 'altura'))

'''
4.2 Crear la función ‘dividir’ la cual recibirá como parámetro dos números (dividendo
y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar False, caso
contrario realizar la división entre los parámetros y retornar el resultado
'''
def dividir (dividendo, divisor):
    return dividendo / divisor if divisor != 0 else False

#resultado = "Es la respuesta" if x == 42 else "anduviste cerca"

'''print(dividir(50, 2))'''

'''    if divisor == 0:
        retorno = False
    else:
        retorno = dividendo / divisor
    return retorno'''

'''
4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de
héroes y un string que representa el dato del héroe que se requiere calcular el
promedio. La función debe retornar el promedio del dato pasado por parámetro
'''
def calcular_promedio(lista:list, clave:str):
    acumulador = sumar_dato_heroe(lista, clave)
    return dividir(acumulador, len(lista))

'''print(calcular_promedio(lista_personajes, 'peso'))'''

'''
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una
lista de héroes y un string que representa la clave del dato
● Se debe validar que el dato que se encuentra en esa clave sea de tipo int o
float. Caso contrario retornaria False
● Se debe validar que la lista a manipular no esté vacía , en caso de que esté
vacía se retornaria también False
'''
def mostrar_promedio_dato(lista:list, clave:str):
    retorno = True
    
    if len(lista) == 0:
        retorno = False
    else:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):  
                retorno = False
                break
    if retorno == True:
        retorno = calcular_promedio(lista, clave)  

    return retorno

'''print(mostrar_promedio_dato(lista_personajes, 'fuerza'))  '''

'''
5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla,
el cual permite utilizar toda la funcionalidad ya programada.
'''
def imprimir_menu():
    print('\t A- Normalizar datos (No se debe poder acceder a los otros puntos) \n \tB- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB \n \tC- Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n \tD- Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n \tE- Recorrer la lista y determinar cuál es el superhéroe más débil de género M \n \t F- Recorrer la lista y determinar cuál es el superhéroe más débil de género NB \n \t G- Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB \n \t H- Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n \t I- Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n \t J- Listar todos los superhéroes agrupados por color de ojos. \n \t K-Listar todos los superhéroes agrupados por tipo de inteligencia) \n \t L- Salir')

#imprimir_menu()

'''
5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de
número el cual deberá verificar que sea sea un string conformado únicamente por
dígitos. Retornara True en caso de serlo, False caso contrario

'''
def validar_entero(numero:str):
    
    return True if numero.isdigit() else False

#print(validar_entero('2'))

'''
5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú
de opciones y le pedirá al usuario que ingrese el número de una de las opciones
elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara
casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1
y 5.2
'''
def stark_menu_principal():
    retorno = False
    imprimir_menu()
    opcion = input("Ingresa una opcion: ")
    
    if opcion.upper() >= "A" and opcion.upper() <= "L":
        retorno = opcion.upper()

    return retorno

'''opcion = stark_menu_principal()
print(opcion)'''

'''
6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes
y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
funciones con prefijo 'stark_' donde crea correspondiente.

'''
def stark_marvel_app(lista:list):
    
    continuar = True
    bandera = False

    while continuar:

        opcion = stark_menu_principal()
        system('cls')
        if opcion == "A" and bandera != True:
            stark_normalizar_datos(lista)
            bandera = True
        elif bandera == True:
            match(opcion):
                case 'B' | 'b':
                    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero NB
                    lista_no_binario = obtener_dato_cantidad(lista, 'NB', 'genero')
                    for personaje in lista_no_binario:
                        print(obtener_nombre(personaje))
                    

                case 'C' | 'c':
                    # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
                    lista_genero_f= obtener_dato_cantidad(lista, 'F', 'genero')
                    maximo = obtener_maximo(lista_genero_f, 'altura')
                    nombre = obtener_dato_cantidad(lista_genero_f, maximo, 'altura')
                    for personaje in nombre:
                        print(obtener_nombre(personaje))
                case 'D' | 'd':
                    # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
                    lista_genero_m= obtener_dato_cantidad(lista, 'M', 'genero')
                    maximo = obtener_maximo(lista_genero_m, 'altura')
                    nombre = obtener_dato_cantidad(lista_genero_m, maximo, 'altura')
                    for personaje in nombre:
                        print(obtener_nombre(personaje))
                case 'E' | 'e':
                    # E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
                    lista_genero_m= obtener_dato_cantidad(lista, 'M', 'genero')
                    minimo = obtener_minimo(lista_genero_m, 'fuerza')
                    nombre = obtener_dato_cantidad(lista_genero_m, minimo, 'fuerza')
                    for personaje in nombre:
                        print(obtener_nombre(personaje))
                case 'F' | 'f':
                    # F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
                    lista_genero_nb= obtener_dato_cantidad(lista, 'NB', 'genero')
                    minimo = obtener_minimo(lista_genero_nb, 'fuerza')
                    nombre = obtener_dato_cantidad(lista_genero_nb, minimo, 'fuerza')
                    for personaje in nombre:
                        print(obtener_nombre(personaje))
                case 'G' | 'g':
                    # G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de genero NB
                    lista_genero_nb = obtener_dato_cantidad(lista, 'NB', 'genero')
                    promedio = mostrar_promedio_dato(lista_genero_nb, 'fuerza')
                    print(promedio)
                case 'H' | 'h':
                    # H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                    contar_por_caracteristica(lista, "color_ojos")
                case 'I' | 'i':
                    # I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
                    contar_por_caracteristica(lista, "color_pelo")
                case 'J' | 'j':
                    # J. Listar todos los superhéroes agrupados por color de ojos.
                    listar_por_caracteristica(lista, "color_ojos")
                case 'K' | 'k':
                    # K. Listar todos los superhéroes agrupados por tipo de inteligencia
                    listar_por_caracteristica(lista, "inteligencia")
                case 'L' | 'l':
                    continuar = False
            pausa()
        else:
            print("no se han normalizado los datos")
        

'''
Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista.
'''
def generar_json(nombre:str, lista:list, clave:str):
    data = {clave: lista} #lista / valor 
    #otra forma:
    #data = {}
    #data [clave] = lista

    with open(nombre, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False )