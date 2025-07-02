#Ejercicio 04: Categoría de edades 
#Pide al usuario que ingrese su edad y muestra su categoría:
# - Menor de 13 años: "Niño"
# - Entre 13 y 19 años: "Adolescente"
# - Entre 20 y 64 años: "Adulto"
# - 65 años o más: "Adulto mayor"

edad =input("ingrese su edad:")
edad = int(edad)


if edad >= 65 :
    print("Es un adulto mayor")
elif edad <= 64 and edad >= 20:
    print("Es un adulto")
elif edad <= 19 and edad >= 13:
    print("Es un Adolencente")
elif edad <= 12: 
    print("Es un Niñato")
else:
    print("Dale forro ponen un numero real.") 

#Asi lo hizo el 
print("\nEjercicio 4:")
edad = int(input("Introduce una edad: "))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida.")