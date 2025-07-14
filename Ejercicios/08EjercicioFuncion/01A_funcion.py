#Ejercicio 1: determinar el mayor de dos números
#pide al usuario que ingrese dos números y muestra el mayor de los dos.
#usando Funcion, range ,for
#indicando cual es el mayor o si son iguales.

print("\n Funcion sumar")
def suma():
    num1=int(input("Numero 1: "))
    num2=int(input("Numero 1: "))
    print(f"la suma es {num1+num2}")

#suma()

print("\n Sacar promedio")

def SacarPromedio(num1,num2,num3):
   resultado=num1+num2+num3
   resultado=resultado/3
   print(f"El promedio es: {resultado}")

#SacarPromedio(5,5,5)
print("\nHacer una tabla de multiplicar usando funcion")

def tabla(num1):
    num2=0
    while num2<=10:
        resultado=num1*num2
        print(f"{num1}x{num2}={resultado}")
        num2+=1    
#tabla(5)

print("\n Elije solo numeros impares: ")

def impar(num1):
    contador=1
    while contador<=num1:
     print(F"los numeros impares son {contador}")
     contador+=2


#impar(30)


def pares(num1):
     par=2
     while par<=num1:
        if par&2==0 and par/2==int:
         print(f"Es par el numero: {par}")
        par+=1


pares(20)
   