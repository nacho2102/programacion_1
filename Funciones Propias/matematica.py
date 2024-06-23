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

def potencia(base:int, exponente:int) -> int:
    '''
    Summary:
    Recibe dos arumentos (Base y potencia), calcula la potencia y retorna el resultado
    
    Args:
    base (int): Numero base 
    exponente (int): Numero exponente
    
    Returns:
    int: resultado de la base elevado al exponente
    '''
    return base ** exponente

def es_par(numero:int) -> bool:
    '''
    Summary: 
        Verifica si el numero ingresao es Par o Impar
        numero: -> int
        return: -> bool    
    '''
    return (numero % 2 == 0)

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

