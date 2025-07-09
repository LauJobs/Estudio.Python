# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20]

maximo = numeros[0]  # Inicializamos con el primer elemento
for numero in numeros:
  if numero > maximo:
    maximo = numero
print(f"El número máximo es: {maximo}")
