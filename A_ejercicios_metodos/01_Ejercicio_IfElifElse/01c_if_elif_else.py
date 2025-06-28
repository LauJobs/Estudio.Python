#Ejercicio 3: Año biciesto 
#pide al usuario que ingrese un año y determina si es bisiesto o no.
#Un año es bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400.
Año = input("Ingrese un año: ")
Año = int(Año)

if Año // 4 == 0 and Año // 100 != 0 or Año // 400 == 0:
    print("El año", Año, "es bisiesto.")
else:
    print("El año", Año, "no es bisiesto.")


#Asi lo hizo el 

print("\nEjercicio 3:")
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
