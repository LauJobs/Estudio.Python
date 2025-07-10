### 02 Bucles (for) 
#Permiten ejecutar un bloque de codigo repetidamente mientras itera un iterable o una lista 
##

print("\n bucle For: ")

#Iterar una lista 
frutas =["manzana","Pera","sandia"]
for fruta in frutas:
    print(fruta)

#Iterar sobre cualquier cosa que sea iterable 

cadena= "lautaro"
for caracteres in cadena:
    print(caracteres)

#Recuperar el indice para eso usamos enumerate()
furtas=["Manzana","Pera","Mandarina"]
for idex, fruta in enumerate(frutas):
    print (f"El indice es {idex} y la fruta es {fruta}")

# Bucles anidado son bucles dentro de otro bucle

letra =["a","b","c"]
numeros= [1,2,3]

for letra in letra:
    for numero in numeros:
        print(f"{letra}{numero}")


#break
animales =["perros","gato","raton","loro","pez"]
for indx, animal in enumerate(animales):
    print(animal)
    if animal =="loro":
        print(f"El Loro esta escondido en el: {indx}")
        break


#Compresion de listas (list comprehension)

animales =["oveja","lobo","ciervo","lagarto"]

animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)


    