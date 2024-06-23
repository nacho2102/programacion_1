from cadena_de_caracteres import *

#Ordenar lista
def ordenar_lista_ascendente(lista:list)-> list:# -> Ordena una lista de menor a mayor
    for i in range(len(lista) - 1):# -> Itera en la cantidad de elementos que tiene la lista - 1
        for j in range(i + 1, len(lista)):# -> Itera en la cantidad de elementos que tiene la lista iniciando en i + 1
            if lista[i] > lista[j]:# -> Compara el valor de la lista en i si es mayor que el valor de la lista en j
                auxiliar = lista[i]# -> Guarda el valor de la lista en i en la variable auxiliar
                lista[i] = lista[j]# -> Reemplaza el valor de la lista en i por el valor de la lista en j
                lista[j] = auxiliar# -> Reemplaza el valor de la lista en j por el valor de la lista en auxiliar
    return lista # -> Devuelve la lista ordenada de menor a mayor

def ordenar_lista_descendente(lista:list)-> list:# -> Ordena una lista de mayor a menor
    for i in range(len(lista) - 1):# -> Itera en la cantidad de elementos que tiene la lista - 1
        for j in range(i + 1, len(lista)):# -> Itera en la cantidad de elementos que tiene la lista iniciando en i + 1
            if lista[i] < lista[j]:# -> Compara el valor de la lista en i si es menor que el valor de la lista en j
                auxiliar = lista[i]# -> Guarda el valor de la lista en i en la variable auxiliar
                lista[i] = lista[j]# -> Reemplaza el valor de la lista en i por el valor de la lista en j
                lista[j] = auxiliar# -> Reemplaza el valor de la lista en j por el valor de la lista en auxiliar
    return lista # -> Devuelve la lista ordenada de mayor a menor

def ordenar_lista(lista:list, criterio:str = "ASC")-> list:# -> Ordena una lista
    for i in range(len(lista) - 1):# -> Itera en la cantidad de elementos que tiene la lista - 1
        for j in range(i + 1, len(lista)):# -> Itera en la cantidad de elementos que tiene la lista iniciando en i + 1
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]): # -> Compara el valor de la lista en i si es mayor que el valor de la lista en j si el criterio es ASC, menor si el criterio es DESC
                auxiliar = lista[i]# -> Guarda el valor de la lista en i en la variable auxiliar
                lista[i] = lista[j]# -> Reemplaza el valor de la lista en i por el valor de la lista en j
                lista[j] = auxiliar# -> Reemplaza el valor de la lista en j por el valor de la lista en auxiliar
    return lista # -> Devuelve la lista ordenada de menor a mayor

def ordernar_listas_parallelas (lista_1:list,lista_2:list, criterio:str = "ASC")-> list:# -> Ordena dos listas que pueden tener diferentes tipos de datos tomando la lista 1 como referencia para ordernar también la lista 2
    for i in range(len(lista_1) - 1):# -> Itera en la cantidad de elementos que tiene la lista 1 - 1
        for j in range(i + 1, len(lista_1)):# -> Itera en la cantidad de elementos que tiene la lista 1, iniciando en i + 1
            if (criterio == "ASC" and lista_1[i] > lista_1[j]) or (criterio == "DESC" and lista_1[i] < lista_1[j]):# -> Compara el valor de la lista 1 en i si es mayor que el valor de la lista 1 en j si el criterio es ASC, menor si el criterio es DESC
                auxiliar = lista_1[i]# -> Guarda el valor de la lista 1 en i en la variable auxiliar
                lista_1[i] = lista_1[j]# -> Reemplaza el valor de la lista 1 en i por el valor de la lista en j
                lista_1[j] = auxiliar# -> Reemplaza el valor de la lista 1 en j por el valor de la lista en auxiliar

                auxiliar = lista_2[i]# -> Guarda el valor de la lista 2 en i en la variable auxiliar
                lista_2[i] = lista_2[j]# -> Reemplaza el valor de la lista 2 en i por el valor de la lista en j
                lista_2[j] = auxiliar# -> Reemplaza el valor de la lista en 2 j por el valor de la lista en auxiliar
            elif lista_1[i] == lista_1[j]:# -> Compara el valor de la lista 1 en i si es igual que el valor de la lista 1 en j, si es el caso se ordena en criterio a partir de la lista 2
                if (criterio == "ASC" and lista_2[i] > lista_2[j]) or (criterio == "DESC" and lista_2[i] < lista_2[j]):# -> Compara el valor de la lista 2 en i si es igual que el valor de la lista 2 en j
                    auxiliar = lista_1[i]# -> Guarda el valor de la lista 1 en i en la variable auxiliar
                    lista_1[i] = lista_1[j]# -> Reemplaza el valor de la lista 1 en i por el valor de la lista en j
                    lista_1[j] = auxiliar# -> Reemplaza el valor de la lista 1 en j por el valor de la lista en auxiliar

                    auxiliar = lista_2[i]# -> Guarda el valor de la lista 2 en i en la variable auxiliar
                    lista_2[i] = lista_2[j]# -> Reemplaza el valor de la lista 2 en i por el valor de la lista en j
                    lista_2[j] = auxiliar# -> Reemplaza el valor de la lista en 2 j por el valor de la lista en auxiliar
    return lista_1, lista_2 

def ordenar_listas_mixta (matriz:list, criterio:str = "ASC")-> list:# -> Ordena una lista de listas que pueden tener diferentes tipos de datos
    for i in range(len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista
        for j in range(len(matriz[i])-1):# -> Itera en la cantidad de elementos que tiene la lista - 1
            for k in range(j+1, len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista iniciando en j + 1
                if type(matriz[i][j]) == type(str()) and type(matriz[i][k]) == type(str()) or (type(matriz[i][j]) == type(int()) and type(matriz[i][k]) == type(int())) or (type(matriz[i][j]) == type(float()) and type(matriz[i][k]) == type(float())):# -> Compara el tipo de dato de la lista en i en j con el tipo de dato de la lista en i en k sean el mismo.
                    if (criterio == "ASC" and matriz[i][j] > matriz[i][k]) or (criterio == "DESC" and matriz[i][j] < matriz[i][k]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en i en k si el criterio es ASC, menor si el criterio es DESC
                        aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                        matriz[i][j] = matriz[i][k]# -> Reemplaza el valor de la lista en i en j por el valor de la lista en i en k
                        matriz[i][k] = aux# -> Reemplaza el valor de la lista en i en k por el valor de la variable aux
                elif type(matriz[i][j]) == type(str()) and (type(matriz[i][k]) == type(int()) or type(matriz[i][k]) == type(float())):# -> Compara que el tipo de dato de la lista en i en j sea STR y el tipo de dato de la lista en i en j sea INT o FLOAT
                    if (criterio == "ASC" and ord(matriz[i][j]) > matriz[i][k]) or (criterio == "DESC" and ord(matriz[i][j]) < matriz[i][k]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en i en k si el criterio es ASC, menor si el criterio es DESC
                        aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                        matriz[i][j] = matriz[i][k]# -> Reemplaza el valor de la lista en i en j por el valor de la lista en i en k
                        matriz[i][k] = aux# -> Reemplaza el valor de la lista en i en k por el valor de la variable aux
                elif type(matriz[i][k]) == type(str()) and (type(matriz[i][j]) == type(int()) or type(matriz[i][j]) == type(float())):# -> Compara que el tipo de dato de la lista en i en k sea STR y el tipo de dato de la lista en i en j sea INT o FLOAT
                    if (criterio == "ASC" and (matriz[i][j]) > ord(matriz[i][k])) or (criterio == "DESC" and (matriz[i][j]) < ord(matriz[i][k])):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en i en k si el criterio es ASC, menor si el criterio es DESC
                        aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                        matriz[i][j] = matriz[i][k]# -> Reemplaza el valor de la lista en i en j por el valor de la lista en i en k
                        matriz[i][k] = aux# -> Reemplaza el valor de la lista en i en k por el valor de la variable aux
    return matriz# -> Devuelve la lista ordenada

#Mayor valor de una lista
def mayor_valor_lista (lista:list)-> int:# -> Devuelve el valor mayor de una lista
    i_0 = True# -> Variable que indica si es el primer valor de la lista
    for i in range (len (lista)):# -> Itera en la cantidad de elementos que tiene la lista
        if i_0 == True or lista[i] > mayor:# -> Compara si es primer valor de la lista o si el valor de la lista en i es mayor que el valor de la variable mayor
            mayor = lista [i]# -> Guarda el valor de la lista en i en la variable mayor
            i_0 = False# -> Indica que ya no es el primer valor de la lista
    return mayor# -> Devuelve el valor de la variable mayor

#Menor valor de una lista
def menor_valor_lista (lista:list)-> int:# -> Devuelve el valor menor de una lista
    i_0 = True# -> Variable que indica si es el primer valor de la lista
    for i in range (len (lista)):# -> Itera en la cantidad de elementos que tiene la lista
        if i_0 == True or lista[i] < menor:# -> Compara si es primer valor de la lista o si el valor de la lista en i es menor que el valor de la variable menor
            menor = lista [i]# -> Guarda el valor de la lista en i en la variable menor
            i_0 = False# -> Indica que ya no es el primer valor de la lista
    return menor# -> Devuelve el valor de la variable menor

#Mayor/Menor valor de una lista
def max_min_valor_lista (lista:list, criterio:str = "MAX")-> list:# -> Devuelve el valor mayor o menor de una lista
    i_0 = True# -> Variable que indica si es el primer valor de la lista
    for i in range (len (lista)):# -> Itera en la cantidad de elementos que tiene la lista
        if  criterio == "MAX":# -> Compara si el criterio es MAX
            if i_0 == True or lista[i] > max_min:# -> Compara si es primer valor de la lista o si el valor de la lista en i es mayor que el valor de la variable max_min
                max_min = lista [i]# -> Guarda el valor de la lista en i en la variable max_min
                i_0 = False# -> Indica que ya no es el primer valor de la lista
        elif criterio == "MIN":# -> Compara si el criterio es MIN        
            if i_0 == True or lista[i] < max_min:# -> Compara si es primer valor de la lista o si el valor de la lista en i es menor que el valor de la variable max_min
                max_min = lista [i]# -> Guarda el valor de la lista en i en la variable max_min
                i_0 = False# -> Indica que ya no es el primer valor de la lista
        else:# -> Compara si el criterio es incorrecto
            print("Criterio incorrecto")# -> Imprime el criterio incorrecto
    return max_min# -> Devuelve el valor de la variable max_min

def normalizar_lista(lista:list)-> list:# -> Devuelve la lista normalizada
    normalizado = False # -> Variable que indica si la lista ya se normalizo
    for i in range(len (lista)):# -> Itera en la cantidad de elementos que tiene la lista
        if validar_int_float(lista[i]) == True:# -> Compara si la lista en i es numerica
            lista[i] = float(lista[i])# -> Convierte la lista en i a flotante
            normalizado = True# -> Indica que la lista ya se normalizo
        elif validar_str(lista[i]) == True:# -> Compara si la lista en i es string
            lista[i] = lista[i]# -> La lista en i se mantiene igual
            normalizado = True# -> Indica que la lista ya se normalizo
    

#Ordenar Matriz
def matriz_ordenada (matriz:list, criterio:str = "ASC")-> list:# -> Devuelve la matriz ordenada por el criterio ASC o DESC
    for i in range(len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista
        for j in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
            for k in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
                if k == len(matriz[i])-1:# -> Compara si es el ultimo valor de la lista
                    for l in range(i+1, len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista iniciando en i+1
                        for m in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
                            if type(matriz[i][j]) == type(int()) and type(matriz[l][m]) == type(int()) or type(matriz[i][j]) == type(float()) and type(matriz[l][m]) == type(float()) or type(matriz[i][j]) == type(str()) and type(matriz[l][m]) == type(str()):# -> Compara el tipo de dato de la lista en i en j con el tipo de dato de la lista en l en m sean el mismo.
                                if (criterio == "ASC" and matriz[i][j] > matriz[l][m]) or (criterio == "DESC" and matriz[i][j] < matriz[l][m]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m
                            elif type(matriz[i][j]) == type(str()) and (type(matriz[l][m]) == type(int()) or type(matriz[l][m]) == type(float())):# -> Compara que el tipo de dato de la lista en i en j sea STR y el tipo de dato de la lista en l en m sea INT o FLOAT
                                if (criterio == "ASC" and ord(matriz[i][j]) > matriz[l][m]) or (criterio == "DESC" and ord(matriz[i][j]) < matriz[l][m]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m
                            elif type(matriz[l][m]) == type(str()) and (type(matriz[i][j]) == type(int()) or type(matriz[i][j]) == type(float())):# -> Compara que el tipo de dato de la lista en l en m sea STR y el tipo de dato de la lista en i en j sea INT o FLOAT
                                if (criterio == "ASC" and (matriz[i][j]) > ord(matriz[l][m])) or (criterio == "DESC" and (matriz[i][j]) < ord(matriz[l][m])):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m        
    matriz = ordenar_listas_mixta(matriz, criterio)# -> Llama a la funcion ordenar_listas_mixta para ordenar los indices por separado
    return matriz# -> Devuelve la matriz
                            
def matriz_ordenada (matriz:list, criterio:str = "ASC")-> list:# -> Devuelve la matriz ordenada por el criterio ASC o DESC
    for i in range(len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista
        for j in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
            for k in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
                if k == len(matriz[i])-1:# -> Compara si es el ultimo valor de la lista
                    for l in range(i+1, len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista iniciando en i+1
                        for m in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
                            if type(matriz[i][j]) == type(int()) and type(matriz[l][m]) == type(int()) or type(matriz[i][j]) == type(float()) and type(matriz[l][m]) == type(float()) or type(matriz[i][j]) == type(str()) and type(matriz[l][m]) == type(str()):# -> Compara el tipo de dato de la lista en i en j con el tipo de dato de la lista en l en m sean el mismo.
                                if (criterio == "ASC" and matriz[i][j] > matriz[l][m]) or (criterio == "DESC" and matriz[i][j] < matriz[l][m]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m
                            elif type(matriz[i][j]) == type(str()) and (type(matriz[l][m]) == type(int()) or type(matriz[l][m]) == type(float())):# -> Compara que el tipo de dato de la lista en i en j sea STR y el tipo de dato de la lista en l en m sea INT o FLOAT
                                if (criterio == "ASC" and ord(matriz[i][j]) > matriz[l][m]) or (criterio == "DESC" and ord(matriz[i][j]) < matriz[l][m]):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m
                            elif type(matriz[l][m]) == type(str()) and (type(matriz[i][j]) == type(int()) or type(matriz[i][j]) == type(float())):# -> Compara que el tipo de dato de la lista en l en m sea STR y el tipo de dato de la lista en i en j sea INT o FLOAT
                                if (criterio == "ASC" and (matriz[i][j]) > ord(matriz[l][m])) or (criterio == "DESC" and (matriz[i][j]) < ord(matriz[l][m])):# -> Compara el valor de la lista en i en j si es mayor que el valor de la lista en l en m si el criterio es ASC, menor si el criterio es DESC
                                    aux = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable aux
                                    matriz[i][j] = matriz[l][m]# -> Guarda el valor de la lista en l en m en la lista en i en j
                                    matriz[l][m] = aux# -> Guarda el valor de la variable aux en la lista en l en m        
    matriz = ordenar_listas_mixta(matriz, criterio)# -> Llama a la funcion ordenar_listas_mixta para ordenar los indices por separado
    return matriz# -> Devuelve la matriz

def max_min_matriz(matriz:list, criterio:str = "MAX")-> list:# -> Devuelve el valor maximo o minimo de una matriz
    matriz = matriz_ordenada(matriz)# -> Llama a la funcion matriz_ordenada para ordenar la matriz
    i_num = True# -> Variables que indican si es el primer valor de la lista o si el valor de la lista en i es mayor o menor que el valor de la variable max_min_num
    i_alpha = True# -> Variables que indican si es el primer valor de la lista o si el valor de la lista en i es mayor o menor que el valor de la variable max_min_num
    for i in range(len(matriz)):# -> Itera en la cantidad de elementos que tiene la lista
        for j in range(len(matriz[i])):# -> Itera en la cantidad de elementos que tiene la lista en i
            if type(matriz[i][j]) == type(int()) or type(matriz[i][j]) == type(float()):# -> Compara el tipo de dato de la lista en i en j sea INT o FLOAT
                if i_num or (criterio == "MAX" and matriz[i][j] > max_min_num) or (criterio == "MIN" and matriz[i][j] < max_min_num):# -> Compara el valor de la lista en i en j si es mayor que el valor de la variable max_min_num si el criterio es MAX, menor si el criterio es MIN
                    max_min_num = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable max_min_num
                    i_num = False# -> Cambia el valor de la variable i_num a False
            elif type(matriz[i][j]) == type(str()):# -> Compara el tipo de dato de la lista en i en j sea STR
                if i_alpha or (criterio == "MAX" and matriz[i][j] > max_min_alpha) or (criterio == "MIN" ):
                    max_min_alpha = matriz[i][j]# -> Guarda el valor de la lista en i en j en la variable max_min_alpha
                    i_alpha = False# -> Cambia el valor de la variable i_alpha a False
    return max_min_num, max_min_alpha# -> Devuelve el valor maximo o minimo de la matriz

