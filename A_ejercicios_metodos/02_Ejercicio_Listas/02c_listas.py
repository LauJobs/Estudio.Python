# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan1=["pan arriba"]
pan2=["pan abajo"]
ingredientes= ["jamon","queso","tomate"]

sandwich = pan1,ingredientes,pan2

print(sandwich)
#Arriba como lo hice (deberia a ver puesto mas) el mas con parentisis salta erro pero de esa manera no y de esta manera concatena las palabras y no hace una lista dentro de otra lista. 
#Asi es lo corrrecto.

print("\nEjercicio 3:")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print(sandwich)