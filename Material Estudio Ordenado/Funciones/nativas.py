#input() -> Permite que el usuario ingrese un valor
variable = input("Ingresa un valor:")
print(variable)# -> "VALOR INGRESADO"

#print() -> Imprime en pantalla
print("Hola Mundo")

#dir() -> Devuelve una lista con los atributos de la variable
variable = "Hola"
atributos = dir(variable)
print(atributos)

#len() -> Retorna la longitud de una cadena o la cantidad de elementos de una lista
longitud = "hola mundo"
longitud = len(longitud)
print(longitud) # -> 10 
lista = ["hola", "mundo"]
longitud = len(lista)
print(longitud) # -> 2

#type() -> Devuelve el tipo de dato de la variable
variable = 5
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'int'>
variable = 5.5
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'float'>
variable = "Hola Mundo"
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'str'>
variable = True
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'bool'>
variable = None
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'NoneType'>
variable = [1, 2, 3, 4, 5]
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'list'>
variable = (1, 2, 3, 4, 5)
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'tuple'>
variable = {1, 2, 3, 4, 5}
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'set'>
variable = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5}
tipo_de_dato = type(variable)
print(tipo_de_dato)# -> <class 'dict'>