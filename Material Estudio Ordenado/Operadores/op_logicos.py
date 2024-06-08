#AND -> compara dos condiciones y devuelve True si las dos son True
a = True
b = True
op_and = a and b
print(op_and) # -> True
a = True
b = False
op_and = a and b
print(op_and) # -> False
a = False
b = True
op_and = a and b
print(op_and) # -> False
a = False
b = False
op_and = a and b
print(op_and) # -> False

#OR -> compara dos condiciones y devuelve True si una de las dos es True
a = True
b = True
op_or = a or b
print(op_or) # -> True
a = True
b = False
op_or = a or b
print(op_or) # -> True
a = False
b = True
op_or = a or b
print(op_or) # -> True
a = False
b = False
op_or = a or b
print(op_or) # -> False

#NOT -> invierte el valor de una variable
a = True
op_not = not a
print(op_not) # -> False
a = False
op_not = not a
print(op_not) # -> True

