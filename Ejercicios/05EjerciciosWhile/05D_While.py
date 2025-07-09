# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

ingrese_contraseña= input("Ponga una contreña(Debe tener 8 Digitos): ")
contraseña_asinada= ""
while len(ingrese_contraseña) <8:
       if len(ingrese_contraseña) >=8:
        print("Su contraseña a sido guardada")
        contraseña_asinada = ingrese_contraseña
       elif len(ingrese_contraseña) < 8:
        print("La contraseña debe tener 8 digitos,intentelo de nuevo.")
        

#Ta dificil los bucles che pero de aca no salgo hasta entenderlo jajaja
#Asi lo hizo el.

print("\nEjercicio de el 4:")

#contrasena = ""
#while len(contrasena) < 8:
 # contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
 # if len(contrasena) < 8:
 #   print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

#print("Contraseña válida")