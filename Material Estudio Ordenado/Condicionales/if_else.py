#if condicion: -> si se cumple la condicion entonces
    #bloque de instrucciones
#(opcional)elif condicion: -> sino si se comple esta otra condicion entonces
    #bloque de instrucciones
#else: -> si no se cumple ninguna condicion
    #bloque de instrucciones

a = 5
b = 10

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual que b")

if a == b:
    print("a es igual que b")
elif a != b:
    print("a es diferente que b")
else:
    print("no se puede comparar los valores")

if a >= b:
    print("a es mayor o igual que b")
elif a <= b:
    print("a es menor o igual que b")
else:
    print("no se puede comparar los valores")

if a in b:
    print("a se encuentra en b")
elif a is b:
    print("a es igual que b")
elif a not in b:
    print("a no se encuentra en b")
elif a is not b:
    print("a no es igual que b")
else:
    print("no se puede comparar los valores")

if a >= b and a == b:
    print("a es mayor o igual que b y a es igual que b")
elif a <= b or a == b:
    print("a es menor o igual que b o a es igual que b")
elif a != b and not a == b:
    print("a es diferente que b y a no es igual que b")
else:
    print("no se puede comparar los valores")

#if condicion: -> si se cumple la condicion entonces
    #bloque de instrucciones
    #if condicion: -> si se cumple la condicion entonces
        #bloque de instrucciones
    #else: -> si no se cumple la condicion
        #bloque de instrucciones
#else: -> si no se cumple la condicion
    #bloque de instrucciones
if a > b:
    print("a es mayor que b")
    if a == b:
        print("a es igual que b")
    elif a != b:
        print("a es diferente que b")
    else:
        print("no se puede comparar los valores")
else:
    print("a no es mayor que b")