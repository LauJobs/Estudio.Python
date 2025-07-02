#Ejercicio 1: determinar el mayor de dos números
#pide al usuario que ingrese dos números y muestra el mayor de los dos.
#indicando cual es el mayor o si son iguales.
numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")



if numero1 < numero2 :
    print("el numero mayor es numero2")
elif numero1 > numero2: 
    print("numero1 es el mayor")
else:
    print("Los numeros son iguales")


#Asi es como lo hizo

print("\nEjercicio 1:")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Los números son iguales")



