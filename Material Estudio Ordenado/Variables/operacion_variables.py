# Concatención de variables str
a = "Hola"
b = "Mundo"
var_str = a + " " + b
print(var_str)# -> "Hola Mundo"

# Formateo de variables str
a = "Hola"
b = "Mundo"
var_str = f"{a} {b}"    
var_str_2 = "{} {}".format(a, b)
print(var_str)# -> "Hola Mundo"

# Casteo de variables
# Casteo de str a int
a = "5"
b = int(a)
print(b)# -> 5
# Casteo de int a str
a = 5
b = str(a)
print(b)# -> "5"    
# Casteo de str a float
a = "5.5"
b = float(a)
print(b)# -> 5.5
# Casteo de float a str
a = 5.5
b = str(a)
print(b)# -> "5.5"