# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

nuemro =[10,20,30,40,50]

print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50,60,70,80]
suma = 0
for numero in numeros:
  suma += numero
media = suma / len(numeros)
print(f"La media es: {media}")