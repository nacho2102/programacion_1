#list() -> Crea una lista
a = 1
b = "a"
c = True
d = 0.5
lista = list((a, b, c, d))  
print(lista) # -> [1, 'a', True, 0.5]

#append() -> Agrega un elemento al final de la lista
a = 1
b = "a"
c = True
d = 0.5
lista = list((a, b, c, d))  
lista.append("Hola")
print(lista) # -> [1, 'a', True, 0.5, 'Hola']

#insert() -> Agrega un elemento en una posición determinada y desplaza los demás elementos
a = 1
b = "a"
c = True
d = 0.5
lista = list((a, b, c, d))  
lista.insert(2, "Hola")
print(lista) # -> [1, 'a', 'Hola', True, 0.5]  

#extend() -> Agrega una lista al final de la lista
a = 1
b = "a"
c = True
d = 0.5
e = [1, 2, 3]
f = [4, 5, 6]
g = [7, 8, 9]
lista = list((a, b, c, d))  
print(lista) # -> [1, 'a', True, 0.5]
lista.extend([e, f, g])
print(lista) # -> [1, 'a', True, 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]

#pop() -> Elimina un elemento en una posición determinada pasandole el indice
a = 1
b = "a"
c = True
d = 0.5
e = [1, 2, 3]
f = [4, 5, 6]
g = [7, 8, 9]
lista = list((a, b, c, d, e, f, g))  
print(lista) # -> [1, 'a', True, 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista.pop(2)
print(lista) # -> [1, 'a', 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]

#remove() -> Elimina un elemento concreto de la lista
a = 1
b = "a"
c = True
d = 0.5
e = [1, 2, 3]
f = [4, 5, 6]
g = [7, 8, 9]
lista = list((a, b, c, d, e, f, g))  
print(lista) # -> [1, 'a', True, 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista.remove(1)
print(lista) # -> ['a', True, 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]

#clear() -> Elimina todos los elementos de la lista
a = 1
b = "a"
c = True
d = 0.5
e = [1, 2, 3]
f = [4, 5, 6]
g = [7, 8, 9]
lista = list((a, b, c, d, e, f, g))  
print(lista) # -> [1, 'a', True, 0.5, [1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista.clear()
print(lista) # -> []

#sort() -> Ordena los elementos de la lista de menor a mayor o alfabéticamente siempre y cuando sean del mismo tipo de dato
a = 1
b = 2
c = 3
lista = list((c, a, b))  
print(lista) # -> [3, 1, 2]
lista.sort()
print(lista) # -> [1, 2, 3]
a = "a"
b = "b"
c = "c"
lista = list((c, a, b))  
print(lista) # -> ['c', 'a', 'b']
lista.sort()
print(lista) # -> ['a', 'b', 'c']

#sort(reverse=True) -> Ordena los elementos de la lista de mayor a menor o alfabéticamente siempre y cuando sean del mismo tipo de dato
a = 1
b = 2
c = 3
lista = list((c, a, b))  
print(lista) # -> [3, 1, 2]
lista.sort(reverse=True)
print(lista) # -> [3, 2, 1]
a = "a"
b = "b"
c = "c"
lista = list((c, a, b))  
print(lista) # -> ['c', 'a', 'b']
lista.sort(reverse=True)
print(lista) # -> ['c', 'b', 'a']

#sorted() -> Ordena los elementos de la lista de menor a mayor o alfabéticamente siempre y cuando sean del mismo tipo de dato, tambien ordena una lista de tuplas o una lista de diccionarios
a = 1
b = 2
c = 3
lista = list((c, a, b))  
print(sorted(lista)) # -> [1, 2, 3]
a = "a"
b = "b"
c = "c"
lista = list((c, a, b))  
print(sorted(lista)) # -> ['a', 'b', 'c']
lista_tupla = [("b", 2), ("a", 1), ("c", 3)]
print(sorted(lista_tupla)) # -> [('a', 1), ('b', 2), ('c', 3)]
lista_diccionario = [{"b": 2}, {"a": 1}, {"c": 3}]
print(sorted(lista_diccionario, key=lambda x: list(x.values())[0])) # -> [{'a': 1}, {'b': 2}, {'c': 3}]