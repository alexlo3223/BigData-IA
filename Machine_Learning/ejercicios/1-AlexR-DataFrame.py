#Ejercicio 1
datos = {
    "nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "estudios_superiores": [True, False, True, False, True, True, False, False, True, False],
}

#Ejercicio 2
import pandas as pd

df = pd.DataFrame(datos)
print("Ejercicio 2")
print(df)

#Ejercicio 3
print()
print("Ejercicio 3")
print(df.head())
print("Tamaño (filas, columnas):",df.shape)
print("Columnas:",df.columns)
print("Tipos de datos:\n",df.dtypes)
print(df.info())
print(df.describe())

#Ejercicio 4

# - Con 22 años o más: apto si tiene al menos 40 puntos.
# - Con menos de 22 años: apto solo si tiene estudios superiores Y al menos 35 puntos.
# - En cualquier otro caso: no apto.

#Ejercicio 5
print()
print("Ejercicio 5")
