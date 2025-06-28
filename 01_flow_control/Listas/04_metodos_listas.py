import os
os.system("clear")

#Añadir y Insertar elemtnos a las listas.

lista=[1,2,3,4,5]
#Append agraga un dato a la lista pero al final.(numeros)
lista.append(12)
print(lista)

#Insert lo que hace es agregar un dato en un lugar espesifico.
lista1 = ["a","b","c","d","e"]
lista1.insert(3,'h')
print(lista1)


#Agrega un elementos a la lista.
lista.extend("hola")
print(lista)

#Eliminar elementos de la listas 

Anotacion = [1,2,3,4,5]
#remove elimina el primer elemento que encuentre del valor que le pedimos, pero no elimina a todos ellos solo al primero que aparazca.
Anotacion.remove(1)
print(Anotacion)

#pop elimina el ultimo valor 
libreta = [1,2,3,4,5]
libreta.pop()
print(libreta)

#Del un elemento de la lista que elijamos
lista2 = [23,12,213421,4,423,43]
del lista2[-1]
print(lista2)

#Clear elimina todo el contenido de la lista
lista4 = [1,2,3,4,5]
lista4.clear()
print(lista4)

#Elimina un rango de elementos 

lista3 = [2,3,4,5,6,7,8,9,10]
del lista3[3:]
print(lista3)

#Ordena la listas de menor a mayor
lista5 = [1,23,4,56,4]
lista5.sort()
print(lista5)

#Aqui ordenamos la listas de menor a mayor y creamos una lista nueva, en vez de SORT seria SORTED

lista6 = [2,234,423,42,53]
lista_sorted = sorted(lista6)
print(lista_sorted)
#Si es texto los ordena por abecedario, contando la letra incial
print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)
#Pero si tiene mayusculas ordena las mayusculas primero, en este caso lo que hace para evitar este tipo de problematica
#Es esto:
print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']

print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False