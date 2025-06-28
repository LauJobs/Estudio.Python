# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.


lista = [1,2,3,4,5]

lista.append(6)
lista.insert(2, int('10'))
del lista[0]
lista.insert(0, int('0'))
print(lista)

#Asi lo hizo el, en la parte de cambiar un valor uso "lista[0]=0" ahorando una linea de codigo 
#que yo use para primero eliminar y luego poner el valor pedido.

print("\nEjercicio 1:")

lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2, 10)
lista[0] = 0
print(lista)