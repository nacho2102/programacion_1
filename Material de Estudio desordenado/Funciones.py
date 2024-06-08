variable_a = 5
id_variable_a = id(variable_a)

variable_b = 10
id_variable_b = id(variable_b)

print(f"Id variable a = {id_variable_a}")
print(f"Id variable b = {id_variable_b}")


def funcion(variable):
    variable = variable + 1
    print(f"Id variable= {id(variable)} y el valor es {variable}")
    return variable

variable_a_2 = funcion(variable_a)
variable_b_2 = funcion(variable_b)

print(f"Id variable a despues = {id_variable_a} y el valor es {variable_a_2}")
print(f"Id variable b despues = {id_variable_b} y el valor es {variable_b_2}")

#////////////////////////

lista_ordena = [1, 2, 3, 4, 5]
id_variable_a = id(lista_ordena)

print(f"Id lista_ordena a = {id_variable_a}")

def funcion(lista:list):
    lista.append(6)
    print(f"Id lista= {id(lista)} y el valor es {lista}")

funcion(lista_ordena)

print(f"Id lista_ordena a despues = {id_variable_a} y el valor es {lista_ordena}")

def promedio_por_genero (diccionario:dict,clave:str,genero:str)->float:
    """_summary_

    Args:
        diccionario (dict): _description_
        key (str): _description_

    Returns:
        float: _description_
        ctrl+shift+2
    """    
    contador = 0
    acumulador_fuerza = 0

    for datos in diccionario:
        for key in datos.keys():
            if key == clave and  datos['genero'] == genero:
                acumulador_fuerza = acumulador_fuerza + float(datos[key])
                contador = contador + 1

    if contador > 0 :
        return acumulador_fuerza / contador