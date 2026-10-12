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

def es_apto(fila):
    if fila["edad"] >= 22:
        return bool(fila["puntos"] >= 40)
    return bool(fila["estudios_superiores"] and fila["puntos"] >= 35)

df["apto"] = df.apply(es_apto, axis = 1)

print(df)

#Ejercicio 6
print()
print("Ejercicio 6")

print(df["apto"].value_counts())

#Ejercicio 7
print()
print("Ejercicio 7")
candidatos_aptos = df[df["apto"]]
print(candidatos_aptos)

#Ejercicio 8
print()
print("Ejercicio 8")
con_estudios = df[df["estudios_superiores"]]
print(con_estudios)

num_con_estudios = len(con_estudios)
num_aptos_con_estudios = con_estudios["apto"].sum()
no_aptos_con_estudios = con_estudios[~con_estudios["apto"]]

print("Personas con estudios superiores:", num_con_estudios)
print("De ellas son aptas:", num_aptos_con_estudios)
if len(no_aptos_con_estudios) > 0:
    print("Sí, hay personas con estudios superiores que no son aptas:", list(no_aptos_con_estudios["nombre"]))
else:
    print("No, todas las personas con estudios superiores son aptas")

#Ejercicio 9
print()
print("Ejercicio 9")
print("De menor a mayor puntuación:")
print(df.sort_values("puntos"))
print("De mayor a menor puntuación:")
print(df.sort_values("puntos", ascending=False))

#Ejercicio 10
print()
print("Ejercicio 10")
print("Edad media:", df["edad"].mean())
print("Puntuación media:", df["puntos"].mean())
print("Puntuación máxima:", df["puntos"].max())
print("Puntuación mínima:", df["puntos"].min())
print("Edad de la persona más joven:", df["edad"].min())
print("Edad de la persona más mayor:", df["edad"].max())

#Ejercicio 11
print()
print("Ejercicio 11")

def calcular_nivel(puntos):
    if puntos >= 40:
        return "alto"
    if puntos >= 35:
        return "medio"
    return "bajo"

df["nivel"] = df["puntos"].apply(calcular_nivel)
print(df)

#Ejercicio 12
print()
print("Ejercicio 12")
por_nivel = df.groupby("nivel").agg(
    personas=("nombre", "count"),
    edad_media=("edad", "mean"),
    puntos_media=("puntos", "mean"),
)
print(por_nivel)

#Ejercicio 13
print()
print("Ejercicio 13")
df_resumen = df[["nombre", "puntos", "apto"]]
print(df_resumen)

#Ejercicio 14
print()
print("Ejercicio 14")
df_renombrado = df.rename(columns={
    "nombre": "Nombre del candidato",
    "edad": "Edad",
    "puntos": "Puntuación",
    "estudios_superiores": "Estudios superiores",
    "apto": "Apto",
    "nivel": "Nivel",
})
print(df_renombrado)
