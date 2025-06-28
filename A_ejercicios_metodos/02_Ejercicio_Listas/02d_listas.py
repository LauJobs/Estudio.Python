# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1,2,3]
lista2= [1,2,3]

print(lista2+lista)

#Como lo hice yo arriba y abajo como lo hizo el
#La forma en que la hizo el es reutilizar la lista en vez de hacer otra, esta seria la correcta ya que es mas eficiente y 
#usa menos lineas de codigo.

print("\nEjercicio 4:")
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)