#ASCENDENTE:
#Si fuera letras seria de la A a la z.
#Si fueran numeros serian del 0 al 9.

# generos = ["F", "F", "M", "F", "M", "M", "M", "F"]
# nombres = ["Maia","Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
# edades = [20, 19, 21, 25, 23, 24, 26, 22]
# apellidos = ["Garcia", "Lopez", "Lima", "Garcia", "Martino", "Lopez", "Martino", "Grandon"]

# for i in range(len(generos)):
#     print(generos[i] + " " + apellidos[i] + " " + nombres[i] + " " + str(edades[i]))

# for i in range(len(generos)-1):
#     auxiliar = None
#     for j in range(i + 1,len(generos)):
#         if (generos[i] > generos[j]) or (generos[i] == generos[j] and apellidos[i] > apellidos[j]) or (generos[i] == generos[j] and apellidos[i] == apellidos[j] and nombres[i] > nombres[j]):
#             auxiliar = generos[j]
#             generos[j] = generos[i]
#             generos[i] = auxiliar

#             auxiliar = nombres[j]
#             nombres[j] = nombres[i]
#             nombres[i] = auxiliar

#             auxiliar = edades[j]
#             edades[j] = edades[i]
#             edades[i] = auxiliar

#             auxiliar = apellidos[j]
#             apellidos[j] = apellidos[i]
#             apellidos[i] = auxiliar
'''elif generos[i]==generos[j] and nombres[i] > nombres[j]:
                    auxiliar = generos[j]
                    generos[j] = generos[i]
                    generos[i] = auxiliar

                    auxiliar = nombres[j]
                    nombres[j] = nombres[i]
                    nombres[i] = auxiliar

                    auxiliar = edades[j]
                    edades[j] = edades[i]
                    edades[i] = auxiliar
'''
# for i in range(len(generos)):
#     print(generos[i] + " " + apellidos[i] + " " + nombres[i] + " " + str(edades[i]))

""""
nombre="Dairon"
nombres = ["Maia","Sebastiana", "Alan", "Daniela", "Pedro", "Leandro", "Alan", "Luisa"]
numeros=[[20, 19, 21, 25],[23, 24, 26, 22]]"""


"""for i in nombre:
    print(i)"""

"""for i in range (len (nombre)):
    print(nombre[i])"""

"""for i in range (len (nombres)):
    for j in range (len (nombres[i])):
        print(nombres[i][j])"""

"""bandera=False

for i in range (len (numeros)):
    for j in range (len (numeros[i])):
        if bandera==False or numeros[i][j] > numero_maximo:
            numero_maximo=numeros[i][j]
        if bandera==False or numeros[i][j] < numero_minimo:
            numero_minimo=numeros[i][j]
            bandera=True
print(numero_maximo, numero_minimo)"""

#print(matriz)
#ordenamiento de cada fila de una matriz

"""
for i in range (len (matriz)):
    for j in range (len (matriz[i])):
        for k in range (len (matriz[i])):
            if matriz [i][j]<matriz [i][k]:
                auxiliar=matriz [i][j]
                matriz[i][j]=matriz[i][k]
                matriz[i][k]=auxiliar
                
print(matriz)
"""
