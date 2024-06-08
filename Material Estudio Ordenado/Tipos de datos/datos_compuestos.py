"lista/list()"
lista = ["i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "i_6", "i_7", "i_8", "i_9"]# lista[0] -> lista["indice 0"]
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#lista de enteros/int
lista_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]#lista de cadenas/str
lista_3 = [True, False, True, False, True, False, True, False, True, False]#lista de booleanos
lista_4 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]#lista de flotantes
lista_5 = [True, False, "a", "b", 1, 2, 1.0, 2.0]#lista mixta
#se puede modificar
lista = [1, 2, 3]
print(lista) # -> [1, 2, 3]
lista[0] = 2
print(lista) # -> [2, 2, 3]

"tupla/tup()"
tupla = ("i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "i_6", "i_7", "i_8", "i_9")# tupla[0] -> tupla["indice 0"]
tupla_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)#tupla de enteros/int
tupla_2 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")#tupla de cadenas/str
tupla_3 = (True, False, True, False, True, False, True, False, True, False)#tupla de booleanos
tupla_4 = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)#tupla de flotantes
tupla_5 = (True, False, "a", "b", 1, 2, 1.0, 2.0)#tupla mixta
#no se puede modificar
tupla = (1, 2, 3)
print(tupla) # -> (1, 2, 3)
tupla[0] = 2
print(tupla) # -> error

"conjunto/set()"  
conjunto = {"i_0", "i_1", "i_2", "i_3", "i_4", "i_5", "i_6", "i_7", "i_8", "i_9"}#no se puede acceder por indice, solo en su totalidad, pero si puede iterar y no almacena datos dupliados
conjunto_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}#conjunto de enteros/int    
conjunto_2 = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}#conjunto de cadenas/str 
conjunto_3 = {True, False, True, False, True, False, True, False, True, False}#conjunto de booleanos
conjunto_4 = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0}#conjunto de flotantes
conjunto_5 = {True, False, "a", "b", 1, 2, 1.0, 2.0}#conjunto mixto
#no se puede modificar
conjunto = {1, 2, 3}
print(conjunto) # -> {1, 2, 3}
conjunto[0] = 2
print(conjunto) # -> error  
#se puede redifinir
conjunto = {1, 2, 3}
print(conjunto) # -> {1, 2, 3}
conjunto = {2, 3, 4}
print(conjunto) # -> {2, 3, 4}

"diccionario/dict()"
diccionario = {
    'key_1/clave_1': 'value/valor','key_2/clave_2': 'value/valor',
    'key_3/clave_3': 'value/valor','key_4/clave_4': 'value/valor'
}#almacena datos/'valor' dentro de clave/'key', la key pude ser definida como str o int
#se la llama por su key
diccionario_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
print(diccionario_1['a']) # - > 1
diccionario_2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
print(diccionario_2[1]) # -> a