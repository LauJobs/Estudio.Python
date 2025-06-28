#print("conversion de tipos")
print(2 + int("100"))
print ("100" + str(2))

print(int(3.13)) # Convierte el float a int, truncando la parte decimal

print(bool(1))  # Convierte el entero 1 a booleano, resultando en True
print(bool(0))  # Convierte el entero 0 a booleano, resultando en False
print(bool(-1)) # Convierte el entero -1 a booleano, resultando en True

print(bool(""))  # Convierte una cadena vacía a booleano, resultando en False
print(bool("hola mundo")) # Convierte una cadena no vacía a booleano, resultando en True
print(bool("false")) # Convierte una cadena no vacía a booleano, resultando en True

# print(int("hola mundo"))  # Esto generará un ValueError porque "hola mundo" no es un número válido
