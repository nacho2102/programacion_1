# MODOS DE APERTURA
# "r" -> solo lectura, si el archivo no existe, lanza un error de I/O
# "r+" -> lectura y escritura, si el archivo no existe, lanza un error de I/O
# "w" -> solo escritura, si el archivo no existe, lo crea, si existe, lo sobreescribe
# "w+" -> escritura y lectura, si el archivo no existe, lo crea, si existe, lo sobreescribe
# "a" -> solo escritura, agrega al final del archivo, si el archivo no existe, lo crea
# "a+" -> lectura y escritura, agrega al final del archivo, si el archivo no existe, lo crea

def abrir_archivo (archivo_nombre:str):# -> Recibe un archivo de texto/direccion de archivo 
    if len(archivo_nombre) == 0:# -> Compara la longitud del archivo con 0 para saber si esta vacio
        contenido = False# -> Si la longitud es 0, el archivo esta vacio, por lo tanto, el contenido es falso  
    else:# -> De lo contrario, el archivo no esta vacio        
        with open(archivo_nombre, 'r') as archivo:# -> Abre el archivo solo para leerlo con "r".
            contenido = archivo.read()# -> Guarda el contenido del archivo en la variable "contenido"
    return contenido# -> Retorna el contenido

def guardar_archivo(archivo_nombre:str, contenido_archivo:str): # -> Recibe un archivo o una dirección de archivo y el contenido a guardar
    if len(contenido_archivo) == 0:# -> Compara la longitud del contenido con 0 para saber si esta vacio
        retorno = False# -> Si la longitud es 0, el contenido esta vacio, por lo tanto, el retorno es falso
    else:# -> De lo contrario, el contenido no esta vacio
        with open(archivo_nombre, 'w+') as archivo:# -> Abre el archivo para sobreescribirlo con "w+"
            archivo.write(contenido_archivo)# -> Escribe el contenido en el archivo
        retorno = f"Se creó el archivo: {archivo_nombre}"# -> Retorna el mensaje archivo creado
    return retorno# -> Retorna el retorno

def generar_csv(nombre_csv:str, lista:list):# -> Recibe un nombre de archivo y una lista de diccionarios
    if len(lista) == 0:# -> Compara la longitud de la lista con 0 para saber si esta vacia
        retorno = False# -> Si la longitud es 0, la lista esta vacia, por lo tanto, el retorno es falso
        return retorno# -> Retorna el retorno
    else:# -> De lo contrario, la lista no esta vacia
        claves = ""# -> Crea una cadena vacia para las claves
        datos = ""# -> Crea una cadena vacia para los datos
        for key in lista[0].keys():# -> Recorre las keys del primer diccionario de la lista
            claves += key + ","# -> Agrega la key y una coma a la cadena de claves
        claves += '\n'# -> Agrega un salto de linea a la cadena de claves
        for personaje in lista:# -> Recorre la lista de diccionarios
            for dato in personaje.values():# -> Recorre los valores de cada diccionario
                datos += dato + ","# -> Agrega el valor y una coma a la cadena de datos
            datos += '\n'# -> Agrega un salto de linea a la cadena de datos
        guardar_archivo(nombre_csv, claves + datos)# -> Guarda el archivo con la cadena de claves y la cadena de datos

def leer_csv(archivo_csv:str):# -> Recibe el nombre de un archivo csv/direccion de archivo
    lista = []# -> Crea una lista vacia
    with open(archivo_csv, mode='r', encoding='utf-8') as file:# -> Abre el archivo para leerlo con "r"
            encabezados = file.readline().strip().split(',')# -> Lee la primera línea para obtener los encabezados con .readline(), con .strip() elimina los espacios en blanco al principio y al final, y con .split(',') separa los encabezados por comas
            for linea in file:# -> Lee todas las lineas del archivo iterando en cada linea
                valores = linea.strip().split(',')# ->Asigna a la variable valores el valor de la linea eliminando con .strip() los espacios en blanco al principio y al final, y con .split(',') separa los valores por comas
                fila = {encabezados[i]: valores[i] for i in range(len(encabezados))}# -> Crea una lista de diccionario con los encabezados y los valores de la linea
                lista.append(fila)# -> Agrega a la lista la lista de diccionario
    return lista# -> Retorna la lista

#Se debe importar JSON para trabajar con JSON
import json

def leer_json(archivo_json:str):# -> Recibe el nombre de un archivo json/direccion de archivo
    with open(archivo_json, 'r') as archivo:# -> Abre el archivo para leerlo con "r"
        lista = json.load(archivo)# -> Carga el contenido del archivo json en la variable lista
    return lista# -> Retorna la lista

def cargar_json(archivo_json:json, key):# -> Recibe el nombre de un archivo json/direccion de archivo que contenga una lista de diccionarios y una clave que seria el nombre de la lista
    with open(archivo_json, "r") as archivo:# -> Abre el archivo para leerlo con "r"
        data = json.load(archivo)# -> Carga el contenido del archivo json en la variable data
        print("Archivo cargado exitosamente")# -> Imprime el mensaje de archivo cargado exitosamente
    return(data[key])# -> Retorna la lista

def guardar_json(archivo_json:str, lista:list):# -> Recibe el nombre de un archivo json/direccion de archivo y una lista de diccionarios
#En caso de que se trate de una lista de diccionarios:
    #lista = {"nombre_lista": lista}# -> Crea una lista de diccionario con el nombre que se le desee dar a la lista
    with open(archivo_json, 'w') as archivo:# -> Abre el archivo para sobreescribirlo con "w"
        json.dump(lista, archivo, indent=4)# -> Escribe el contenido de la lista en el archivo


