#Condicionales
# if, elif, else
#edad = int(input("¿Cuántos años tienes? "))
###
#if edad <= 18:
#    print("Eres menor de edad")
#else:
#    print("Eres mayor de edad")
###
nota = 6
if nota >= 9:
    print("Excelente")
elif nota >=6:
    print("Bien")
elif nota <=5:
    print("Desaprobaste")
elif nota  <= 0:
    print("Sos un burro")    

##El if es una condición y el elif se utiliza para agregar multiples condiciones adicionales
# y el else se utiliza para manejar el caso en que ninguna de las condiciones anteriores se cumple.

print("Condiciones multiples")
edad2= 10
tienes_carnet = False

if edad2 >=18 and tienes_carnet:
    print("Puedes conducir")
else:
    print("Policiaa")

#En JavaScript y lo operadores serian
#(java)  (Python)
# &&  ---> and
# ||  ---> or
# !   ---> not

#Isla Margarita = "Venezuela"
edad2= 16
if edad2 >= 18 or tienes_carnet:
    print("Puedes conducir")
else: 
   print("Paga al policia")
#Otro ejemplo de condicionales


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

#Otras cositas

numero = 5
if numero: #true de otra manera si es 0 es false
    print("El número no es cero")
else: 
    print("El número es cero")

nombre= "Lautaro"
if nombre: #true porque no esta vacio en caso contrario si lo esta seria false.
    print("El nombre no está vacío")