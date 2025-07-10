# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
numero =int(input("seleccione el numero que desea multiplicar: "))
multiplicar=1
for num in range(1,11):
 multiplicar= numero*num
 print(f"{numero}x{num}={multiplicar}")
 
 print("\nEjercicio 6:")
numero = int(input("Introduce un número para la tabla de multiplicar: "))
for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")