"""Funciones Parte I

1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

2. Crear una función que verifique si un número dado por argumento es par o impar. 
   La función debe imprimir un mensaje indicando si el número es par o impar.
   
3. Define una función que encuentre el máximo de tres números. 
   La función debe aceptar tres argumentos y devolver el número más grande.
   
4. Diseña una función que calcule la potencia de un número. 
   La función debe recibir la base y el exponente como argumentos y devolver el resultado.

5. Realizar el mismo ejercicio del item 2, pero sin utilizar el operador % 

"""
# 1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def validar_entero(cadena:str) -> bool:
   '''
   Valida un valor determinando si es o no un numero entero
   Recibe un dato el tipo STR.
   Retorna un True si es entero o False si no lo es.
   '''

   retorno = True

   for caracter in cadena:
      if caracter < "0" or caracter > "9":
         retorno = False
         break
   
   return retorno

#2. Crear una función que verifique si un número dado por argumento es par o impar. 
#   La función debe imprimir un mensaje indicando si el número es par o impar.
def es_par(numero:int) -> bool:
   '''
   Summary: 
      Verifica si el numero ingresao es Par o Impar
      numero: -> int
      return: -> bool    
   '''
   return (numero % 2 == 0) 



# 3. Define una función que encuentre el máximo de tres números. 
#    La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_numero_maximo(numero_1:int, numero_2:int, numero_3:int) -> int:
   '''Halla el mayor de 3 numeros ingresados'''
   retorno = None
   if numero_1 == numero_2 and numero_1 == numero_3:
      retorno = numero_1
   else:
      if numero_1 > numero_2 and numero_1 > numero_3:
         retorno = numero_1
      elif numero_2 > numero_3:
         retorno = numero_2
      else:
         retorno = numero_3
   return retorno

# 4. Diseña una función que calcule la potencia de un número. 
#    La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia_numero(base:int, exponente:int) -> int:
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

# 5. Realizar el mismo ejercicio del item 2, pero sin utilizar el operador % 

def es_par_2(numero:int) -> bool:
   '''
   Summary: 
      Verifica si el numero ingresao es Par o Impar
      numero: -> int
      return: -> bool 
   '''
   retorno = False
   if numero != 0:
      if numero < 0:
         numero *= -1
      while numero > 1:
         numero -= 2
      if numero == 0:
         retorno = True
   return retorno
