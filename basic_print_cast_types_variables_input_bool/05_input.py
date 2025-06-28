####
# 05 - Entrada de usuario (input()) - Version simplificada
# La función `input()` permite recibir datos del usuario a través de la consola.
###

nombre =input("Hola, ¿como te llmas? ")

print(f"Hola {nombre}, encantado de conocerte")

age = int(input("¿Cuántos años tienes? "))

print(f"dentro de 20 años tendras {age+20} años")

age= int(age)

print  (f"tienes {age} años")

##print ("obtener multiple valores a la vez")
country, city = input("¿En qué país y ciudad vives? (Separados por un coma,) :").split(",")
      
print(f"{nombre} Vives en {city}, {country}")

