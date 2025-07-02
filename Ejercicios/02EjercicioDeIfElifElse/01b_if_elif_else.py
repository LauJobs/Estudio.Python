#Ejercicio 2: calculadora simple
# # Crea un programa que simule una calculadora simple. Debe pedir al usuario dos números y una operación (suma, resta, multiplicación o división) y mostrar el resultado.
#realiza la operacion y muertra el resultado (maneja la division entre zero)

operacion = input("Ingrese la operación (+, -, *,/): ")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if operacion == "+":
    print("La suma del numero 1 y el numero 2 es:", numero1 + numero2)
elif operacion == "-":
    print("La resta del numero 1 y el numero 2 es:", numero1 - numero2)
elif operacion =="*":
    print("La multiplicacion del numero 1 y el numero 2 es: ", numero1 * numero2)
elif operacion == "/":
    print("La division del numero 1 y el numero 2 es:",int(numero1 / numero2))
else:("No a Ingresado un operador valida")



#Asi lo hizo el:
print("\nEjercicio 2:")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
else:
    print("Operación no válida.")

if 'resultado' in locals(): #Comprueba si la variable resultado existe.
    print(f"El resultado es: {resultado}")