# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero1 =0

while numero1 <20:
 numero1 +=1 
 if numero1 % 2==0:
  continue

 print(numero1)              
 
#Como lo hizo el, lo hice mal por no leer bien la consigna. tengo que prestar mas atencion a la consiganas porque si no
#lo hago puede pasar un error asi de tonto.
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero = 1
suma_pares = 0
while numero <= 20:
  if numero % 2 == 0:
    suma_pares += numero
  numero += 1
  print(suma_pares)
