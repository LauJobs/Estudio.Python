# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

lista = [10, 20, 30, 40, 50]
print(lista[4])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[0])

#Arriba es como lo hice abajo es como se hace

print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.
print(numeros)
