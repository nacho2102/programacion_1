#keys() -> Retorna todas las claves de un diccionario
diccionario = {'key1': 1, 'key2': 2, 'key3': 3}
print(diccionario.keys())# -> dict_keys(['key1', 'key2', 'key3'])
if 'key1' in diccionario.keys():# -> Compara si la clave 'key1' existe en el diccionario
    print('key1 existe')# -> Imprime 'key1 existe'
else:# -> Si la clave 'key1' no existe
    print('key1 no existe')# -> Imprime 'key1 no existe'

#get() -> Retorna el valor de una clave en un diccionario
diccionario = {'key1': 1, 'key2': 2, 'key3': 3}
print(diccionario.get('key1'))# -> 1
print(diccionario.get('key4'))# -> None, porque la clave 'key4' no existe
print(diccionario.get('key4', 'No existe'))# -> 'No existe' 

#items() -> Retorna todas las claves y valores de un diccionario
diccionario = {'key1': 1, 'key2': 2, 'key3': 3}
print(diccionario)# -> {'key1': 1, 'key2': 2, 'key3': 3}
print(diccionario.items())# -> dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

#pop() -> Elimina una clave y retorna su valor
diccionario = {'key1': 1, 'key2': 2, 'key3': 3}
print(diccionario.pop('key1'))# -> 1
print(diccionario)# -> {'key2': 2, 'key3': 3}

#clear() -> Elimina todos los elementos de un diccionario
diccionario = {'key1': 1, 'key2': 2, 'key3': 3}
diccionario.clear()
print(diccionario)# -> {}