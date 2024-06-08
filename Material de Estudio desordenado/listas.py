import random
datosPersonales = ['leo', "messi", 37, "argentino"]

def mostrarDatos(datos:list):
    """_summary_

    Args:
        datos (list): _description_
    """
    for i in range(len(datos)):
        print(datos[i])

datosPersonales.append('miami')

#mostrarDatos(datosPersonales)

numeros = []

for numero in range(10):
    numeroRandom = random.randint(1, 1000)
    numeros.append(numeroRandom)
    
#mostrarDatos(numeros)


def buscarDato(lista, indice):
    retorno = False    
    if indice >= 0 and indice < len(lista):
        retorno = lista[indice]
    return retorno
        
#buscarDato(numeros, 0)
#buscarDato(numeros, 9)

#mostrarDatos(datosPersonales)
#datosPersonales.remove(37)
#mostrarDatos(datosPersonales)

itemBorrado = datosPersonales.pop()
#mostrarDatos(datosPersonales)
#print(f" fue borrado {itemBorrado}")


numerosAux = []

contador = 0

'''
for i in range(len(numeros2)):
    if numeros2[i - contador] == 5:
        numeros2.pop(i - contador)
        contador += 1

'''

"""for numero in numeros2:
    if numero != 5:
        numerosAux.append(numero)"""

#mostrarDatos(numerosAux)

numerosMinimo = None

numeros2 = [0, 2, 4, 5, 8, 9]

for i in range(len(numeros2)):
    for j in range(len(numeros2)-i):
        if i > 0 and numeros2[j] > numeros2[j+1]:
            aux = numeros2[j + 1]
            numeros2[j + 1] = numeros2[j]
            numeros2[j] = aux
        
mostrarDatos(numeros2)

""" 1) Crear una lista de entre 10 a 15 numeros, todos los numeros tiene se ser de forma ramdom
    2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera ([indice] valor)
    3) Determinar cuál es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice] valor)
    4) Determinar cuál es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice] valor)
    5) Calcular promedio
Para todo usar funciones, con "nombres claros y representativos"
"""

import random

#1 1) Crear una lista de entre 10 a 15 numeros, todos los numeros tiene se ser de forma ramdom

def crear_lista_numeros_random(tope):
    numeros = []
    for i in range (tope):
        numeros.append(random.randint(0, 99))

    return numeros

tope = random.randint(10,15)
lista = crear_lista_numeros_random(5)

#2 2) Recorrer la lista imprimiendo por consola la lista, de la siguiente manera ([indice] valor)

def mostrar_lista(lista):
    for i in range(len(lista)):
        print (f"([{i}] {lista[i]})" )

#mostrar_lista(lista)


#3 3) Determinar cuál es el numero mas grande, imprimiendo por consola de la siguiente manera ([indice] valor)

def buscar_num_max(lista):
    numero_max = lista[0]
    for i in range(len(lista)):
        if lista[i] > numero_max:
            numero_max = lista[i]
    return numero_max

def buscar_indice(lista, numero):
    retorno = -1
    for i in range(len(lista)):
        if numero == lista[i]:
            retorno = i
    return retorno
            
def mostrar_informacion(indice, valor):
    print(f"([{indice}] {valor})")

#valor = buscar_num_max(lista)
#indice = buscar_indice(lista, valor)

#mostrar_informacion(indice, valor)

            
#print(lista)
#print(buscar_num_max(lista))

# 4) Determinar cuál es el numero mas chico, imprimiendo por consola de la siguiente manera ([indice] valor)

def buscar_num_min(lista):
    numero_min = lista[0]
    for i in range(len(lista)):
        if lista[i] < numero_min:
            numero_min = lista[i]
    return numero_min

#valor = buscar_num_min(lista)
#indice = buscar_indice(lista, valor)

#mostrar_informacion(indice, valor)

#5) Calcular promedio

def sumar_elementos_lista(lista):
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    return acumulador

def calcular_promedio(lista):
    promedio = 0
    acumulador = sumar_elementos_lista(lista)
    if len(lista) > 0:
        promedio = acumulador / len(lista)
    
    return promedio

print(lista)
print(calcular_promedio(lista))





edades = []

acumulador = 0 
bandera = False

for i in range(5):
    edad = input("Ingrese una edad: ")
    edad =  int (edad)
    edades.append(edad)
    acumulador += edad 

promedio_edad = acumulador / len(edades)

edad_minima = edades[0]

# for i in range(len(edades)):
#     # if bandera == False or edades[i] > edad_maxima:
#     if i == 0 or edades[i] > edad_maxima:
#         edad_maxima = edades[i]
#         # bandera = True
#     if edades[i] < edad_minima:
#         edad_minima = edades[i]

for edad in edades:
    if bandera == False or edad > edad_maxima:
        edad_maxima = edad
        bandera = True
    if edad < edad_minima:
        edad_minima = edad

for i in range (len(edades)):
    print (edades[i]) 

print (promedio_edad)
print (edad_maxima)
print (edad_minima)