#Diccionarios

def listar_diccionario (diccionario:dict) -> str:# -> Recibe un diccionario y lo imprime
    for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
        print(f"{clave} {valor}")# -> Imprime la clave y el valor

def listar_key_diccionario (diccionario:dict, key:str) -> str:# -> Recibe un diccionario y una clave y imprime su valor
    for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
        if clave == key:# -> Compara si la clave es igual a la clave pasada
            print(f"{key} {valor}")# -> Imprime la clave y el valor   

def listar_value_diccionario (diccionario:dict, value:str) -> str:# -> Recibe un diccionario y un valor y imprime su clave
    for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
        if valor == value:# -> Compara si el valor es igual al valor pasado
            print(f"{clave} {value}")# -> Imprime la clave y el valor

def agregar_key_diccionario (diccionario:dict, key:str, value:str) -> dict:# -> Recibe un diccionario, una clave y un valor y agrega una nueva clave con el valor
    nuevo = {key:value}# -> Crea un nuevo diccionario con la clave y el valor
    diccionario.update(nuevo)# -> Agrega el nuevo diccionario al diccionario
    return diccionario# -> Retorna el diccionario

def quitar_key_diccionario (diccionario:dict, key:str) -> dict:# -> Recibe un diccionario y una clave y la elimina del diccionario
    diccionario.pop(key)# -> Elimina la clave del diccionario
    return diccionario# -> Retorna el diccionario

def modificar_key_diccionario (diccionario:dict, key:str, value:str) -> dict:# -> Recibe un diccionario, una clave y un valor y modifica la clave con el valor
    diccionario[key] = value# -> Modifica la clave del diccionario con el valor
    return diccionario# -> Retorna el diccionario

#Listas de diccionarios

def listar_lista_diccionarios (lista:list) -> str:# -> Recibe una lista de diccionarios y la imprime
    for diccionario in lista:# -> Recorre la lista de diccionarios
        for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
            print(f"{clave} {valor}")# -> Imprime la clave y el valor

def listar_key_lista_diccionarios (lista:list, key:str) -> str:# -> Recibe una lista de diccionarios y una clave y la imprime
    for diccionario in lista:# -> Recorre la lista de diccionarios
        for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
            if clave == key:# -> Compara si la clave es igual a la clave pasada
                print(f"{key} {valor}")# -> Imprime la clave y el valor

def listar_value_lista_diccionarios (lista:list, value:str) -> str:# -> Recibe una lista de diccionarios y un valor y la imprime
    for diccionario in lista:# -> Recorre la lista de diccionarios
        for clave, valor in diccionario.items():# -> Recorre la clave y el valor del diccionario
            if valor == value:# -> Compara si el valor es igual al valor pasado
                print(f"{clave} {value}")# -> Imprime la clave y el valor

def agregar_key_lista_diccionarios (lista:list, key:str, value:str) -> list:# -> Recibe una lista de diccionarios, una clave y un valor y agrega una nueva clave con el valor
    nuevo = {key:value}# -> Crea un nuevo diccionario con la clave y el valor
    for diccionario in lista:# -> Recorre la lista de diccionarios
        diccionario.update(nuevo)# -> Agrega el nuevo diccionario al diccionario
    return lista# -> Retorna la lista

def quitar_key_lista_diccionarios (lista:list, key:str) -> list:# -> Recibe una lista de diccionarios y una clave y la elimina de la lista
    for diccionario in lista:# -> Recorre la lista de diccionarios
        diccionario.pop(key)# -> Elimina la clave del diccionario
    return lista# -> Retorna la lista

def modificar_key_lista_diccionarios (lista:list, key:str, value:str) -> list:# -> Recibe una lista de diccionarios, una clave y un valor y modifica la clave con el valor
    for diccionario in lista:# -> Recorre la lista de diccionarios
        diccionario[key] = value# -> Modifica la clave del diccionario con el valor
    return lista# -> Retorna la lista

def modificar_key_lista_diccionarios_especifico (lista:list, key_modificar:str, value_modificar:str, value_criterio:str) -> list:# -> Recibe una lista de diccionarios, una clave y un valor y modifica la clave con el valor
    for diccionario in lista:# -> Recorre la lista de diccionarios
        for key in diccionario.keys():# -> Recorre la clave del diccionario
            if diccionario[key] == value_criterio:# -> Compara si el valor es igual al valor pasado
                diccionario[key_modificar] = value_modificar# -> Modifica la clave del diccionario con el valor
    return lista