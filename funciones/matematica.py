def suma (numero_1:int, numero_2:int) -> int:
    return numero_1 + numero_2
def resta (numero_1:int, numero_2:int) -> int:
    return numero_1 - numero_2        
def multiplicacion (numero_1:int, numero_2:int) -> int:
    return numero_1 * numero_2
def division (numero_1:int, numero_2:int) -> int:
    return numero_1 / numero_2
def promedio (acumulador:int, contador:int) -> int:
    return acumulador / contador

def calcular_factorial (natural:int) -> int:
    """
    Summary:
            Calcula el factorial de un numero "n" de lementos.
    Args:
        natural(int): Numero natural mayor o igual 0.
    Returns:
        int: Devuelve resultado. En caso de un argumento negativo retornara como error "-999".
    """
    resultado = 1

    if natural >= 0:
        for numero in range(natural, 0, -1):
            resultado *= numero
    else:
        resultado = -999
    return resultado

def validar_numero(numero) -> bool:
    """
    Summary:
        Valida que el argumento sea un numero
    Args:
        numero (int/float): Un numero entero o flotante.
    Returns:
        bool: True si el numero es entero o flotante. False de lo contrario.
    """    
    for i in numero:
        if i == "." or i.isnumeric():
            retorno = True
        else:
            retorno = False
            break
    return retorno