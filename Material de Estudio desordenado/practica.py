import json 
from data_Stark import lista_personajes
# 1.1. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
# que indicará el nombre y extensión del archivo a leer (Ejemplo:
# archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
# retornara un string con la información del mismo.

def leer_archivo (archivo_nombre:str):
    if len(archivo_nombre) == 0:
        contenido = False  
    else:          
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido

# print(leer_archivo("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/Material de Estudio desordenado/archivo.txt"))
# print(leer_archivo('Material de Estudio desordenado/exel.csv'))

# 1.2. Crear la función 'guardar_archivo' la cual recibirá por parámetro un
# string que indicará el nombre con el cual se guardará el archivo junto
# con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
# tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no
# existir, lo creara y en caso de existir, lo va a sobreescribir
# Se creó el archivo: nombre_archivo.csv

def guardar_archivo(archivo_nombre:str, contenido_archivo:str):
    if len(contenido_archivo) == 0:
        retorno = False
    else:
        with open(archivo_nombre, 'w+') as archivo:
            archivo.write(contenido_archivo)
        retorno = f"Se creó el archivo: {archivo_nombre}"
    return retorno

# print(guardar_archivo("nuevo_archivo.csv", 'Hola \n pedro'))


# 1.3. Crear la función generar_csv()
# La función va a recibir el nombre y extensión del archivo csv de los
# superhéroes (Puede ser ruta absoluta o relativa) y la lista de los
# mismos.
# Si la lista no está vacía la función deberá guardar en un string la
# información en formato csv (separado con comas) con la cabecera
# correspondiente.
# Una vez generado el string debería usar la función de 1.2 para guardar
# ese string generado al archivo.
# Si la lista está vacia retornar False

def generar_csv(nombre_csv:str, lista:list):
    if len(lista) == 0:
        retorno = False
    else:
        claves = ""
        datos = ""
        for key in lista[0].keys():
            claves += key + ","
        claves += '\n'
        for personaje in lista:
            for dato in personaje.values():
                datos += dato + ","
            datos += '\n'
        guardar_archivo(nombre_csv, claves + datos)
        

# generar_csv('nuevo.csv', lista_personajes)


# 1.4. Crear la función leer_csv() que va a recibir el nombre y extensión de
# donde se ubica el archivo a leer (Ruta absoluta o relativa)
# La función se tiene que encargar de generar una lista de superhéroes
# en base al contenido de ese archivo csv que se le paso. Pueden usar
# la cabecera de ese csv para generar las claves de cada uno de los
# diccionarios.
# La función debe retornar la lista de diccionarios si es que existe el
# archivo y sino False.

def leer_csv(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'r') as archivo:
        lista 

leer_csv('nuevo.csv')


# 1.5. Crear la función generar_json() que va a recibir el nombre y extensión
# de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
# lista de los superhéroes y el nombre de la lista.
# Si la lista no está vacía debería guardar en un diccionario de una sóla
# clave la lista de superhéroes,el nombre de clave debería ser la del
# tercer parámetro que sería el nombre de la lista. (Hecho en la clase pasada!!!!)

# 1.6. Crear la función leer_json() que va a recibir el nombre y extensión de
# donde se ubica el archivo a leer (Ruta absoluta o relativa), y también el
# nombre de la lista a leer por ejemplo en la imagen anterior la lista está
# en la clave “heroes”
# Si el archivo existe deberia leer el archivo json y retornar la lista
# obtenida.