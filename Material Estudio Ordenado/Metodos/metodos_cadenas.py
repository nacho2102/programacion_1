#upper() -> Convierte una cadena en mayúsculas
mayuscula = "hola"
mayuscula = mayuscula.upper()
print(mayuscula) # -> "HOLA"

#lower() -> Convierte una cadena en minúsculas
minuscula = "HOLA"
minuscula = minuscula.lower()
print(minuscula) # -> "hola"

#capitalize() -> Convierte la primera letra de una cadena en mayúscula
capitalize = "hola mundo"
capitalize = capitalize.capitalize()
print(capitalize) # -> "Hola mundo"

#find() -> Busca una subcadena dentro de una cadena y retorna la posicion de la subcadena, si no hay coincidencia retorna -1
find = "hola mundo"
find = find.find("mundo")
print(find) # -> 4

#index() -> Busca una subcadena dentro de una cadena y retorna la posicion de la subcadena, si no hay coincidencia lanza una excepción
index = "hola mundo"
index = index.index("mundo")
print(index) # -> 4

#isnumeric() -> Verifica si una cadena contiene solo números
numeros = "123"
numeros = numeros.isnumeric()
print(numeros) # -> True
numeros = "123a"
numeros = numeros.isnumeric()
print(numeros) # -> False   

#isalpha() -> Verifica si una cadena contiene solo letras
letras = "hola"
letras = letras.isalpha()
print(letras) # -> True
letras = "hola mundo"
letras = letras.isalpha()
print(letras) # -> False, porque el espacio no es una letra

#count() -> Cuenta la cantidad de veces que aparece una subcadena dentro de una cadena
count = "hola mundo"
count = count.count("o")
print(count) # -> 2 

#startwith() -> Verifica si una cadena empieza con una subcadena
startswith = "hola mundo"
startswith = startswith.startswith("hola")
print(startswith) # -> True

#endswith() -> Verifica si una cadena termina con una subcadena
endswith = "hola mundo"
endswith = endswith.endswith("mundo")
print(endswith) # -> True

#replace() -> Reemplaza una subcadena por otra subcadena
replace = "hola mundo"
replace = replace.replace("hola", "Hola")
print(replace) # -> "Hola mundo"

#split() -> Divide una cadena en subcadenas y retorna una lista
split = "hola,mundo"
split = split.split(",")
print(split) # -> ["hola", "mundo"]

#join() -> Une una lista de subcadenas en una cadena
join = ["hola", "mundo"]
join = join.join(" ")
print(join) # -> "hola mundo"
