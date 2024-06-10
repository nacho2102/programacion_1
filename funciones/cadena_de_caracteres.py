def contar_caracteres (variable:str)->int:
    """
    Summary:
        Cuenta la cantidad de caracteres de una cadena de caracteres.
    Args:
        variable(str): Cadena de caracteres.
    Returns:
        int: Longitud de la cadena.
    """
    contador = 0
    for letra in variable:
        contador  = contador + 1

    return contador

def capitalizar (variable:str)->str:
    """
    Summary:
        Convierte la primer letra de una cadena de caracteres en mayuscula.
    Args:
        variable(str): Cadena de caracteres.
    Returns:
        str: Primera letra en mayuscula.
    """    
    cantidad = contar_caracteres(variable)
    if ord(variable[0]) >= 97 and ord(variable[0]) <= 122:
        for i in range (cantidad):
            if i == 0 :
                inicial = chr(ord(variable[i])-32)
                #print(inicial) 
                retorno = inicial
            else:
                retorno += variable[i]
    else:
        retorno = variable
    return retorno

def convertir_mayuscula (variable:str)->str:
    """
    Summary:
        Convierte la cadena de caracteres en mayuscula.
    Args:
        variable(str): Cadena de caracteres.
    Returns:
        str: Cadena de caracteres en mayuscula.
    """    
    cantidad = contar_caracteres(variable)
    mayuscula = ''
    for i in range (cantidad):
        if ord(variable[i]) >= 97 and ord(variable[i]) <= 122:
            letra = chr(ord(variable[i])-32)
            mayuscula += letra
        else:
            mayuscula += variable[i]
    
    return mayuscula

def convertir_minuscula (variable:str)->str:
    """
    Summary:
        Convierte la cadena de caracteres en minuscula.
    Args:
        variable(str): Cadena de caracteres.
    Returns:
        str: Cadena de caracteres en minuscula.
    """    
    cantidad = contar_caracteres(variable)
    minuscula = ''
    for i in range (cantidad):
        if ord(variable[i]) >= 65 and ord(variable[i]) <= 90:
            letra = chr(ord(variable[i])+32)
            minuscula += letra
        else:
            minuscula += variable[i]
        
    return minuscula

def validar_str(variable:str)->bool:
    """
    Summary:
        Valida que la cadena de caracteres contenga solo letras.
    Args:
        variable(str): Cadena de caracteres.
    Returns:
        bool: True si la cadena de caracteres contiene solo letras. False de lo contrario.
    """    
    for letra in variable:
            if letra == " " or letra.isalpha():
                retorno = True
            else:
                retorno = False
                break
    return retorno