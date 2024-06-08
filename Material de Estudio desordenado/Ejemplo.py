#Adolescente: 13 a 17
edad = int(input("Ingrese edad"))
while edad < 0 or edad > 120:
    edad = int(input("Error reingrese edad"))

if not(edad >= 13) or not(edad <= 17):
    print("No es adolescente")

#if not(edad >= 13 and edad <= 17):    
#leyes de Morgan 'if not(edad >= 13) or not(edad <= 17):'

