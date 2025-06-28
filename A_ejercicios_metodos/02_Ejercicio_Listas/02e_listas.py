# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]


lista2 =[1,2,3,4,5,6]
mitad= len (lista2) //2
lista_invertida2 = lista2[:mitad][::-1] + lista2[mitad:]

print(lista_invertida2)

#Se hace asi !
print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)