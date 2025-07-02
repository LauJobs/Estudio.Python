# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista=[10,20,30,40,50,60,70]
print(lista[2::3])

#Como lo hice yo arriba como lo hice abajo
#Como lo hizo el es la manera correcta ya que en mi caso como lo hice afecataria solo un lugar en especifico en 
#En cambio la forma de el siempre toma el dato del medio.
print("\nEjercicio 5:")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])