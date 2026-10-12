"""
Ejercicios de estadística básica con CSV
Cada cálculo se resuelve de tres formas:
  - Método 1: Python elemental (bucles, acumuladores, condicionales)
  - Método 2: Python funcional (map, filter, lambda, sorted, sum, min, max, set, count)
  - Método 3: pandas
Se usa la varianza POBLACIONAL (dividir entre n) -> en pandas, ddof=0.
"""

import math
import pandas as pd


def coinciden(a, b, c):
    """Compara tres números con tolerancia para pequeños decimales."""
    return math.isclose(a, b) and math.isclose(b, c)


def listas_coinciden(a, b, c):
    """Compara tres listas valor a valor con tolerancia."""
    if not (len(a) == len(b) == len(c)):
        return False
    for x, y, z in zip(a, b, c):
        if not coinciden(x, y, z):
            return False
    return True


def redondear(lista, decimales=4):
    return [round(x, decimales) for x in lista]


# =================================================================
print("\nSolución del ejercicio 1")
# =================================================================
# Cargamos el CSV en un DataFrame y exploramos los datos.
df = pd.read_csv("datos_estadistica_alumnos.csv")
print(df.head())

# Guardamos la columna principal como lista de Python
puntos = list(df["puntos_prueba"])
nombres = list(df["nombre"])
print("Cantidad de datos en puntos_prueba:", len(puntos))

# Cada fila del CSV representa a UN alumno: su identificador, su nombre,
# las horas que ha estudiado, los puntos que ha sacado en la prueba,
# cuántos ejercicios ha entregado y cuántos minutos ha usado la plataforma.

# =================================================================
print("\nSolución del ejercicio 2")
# =================================================================
# Media: suma de todos los valores dividida entre la cantidad de valores.

# Método 1: bucle + acumulador
suma = 0
for valor in puntos:
    suma += valor
media_bucle = suma / len(puntos)

# Método 2: funciones
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)

# Método 3: pandas
media_pandas = df["puntos_prueba"].mean()

print("media_bucle:     ", media_bucle)
print("media_funciones: ", media_funciones)
print("media_pandas:    ", media_pandas)
print("¿Coinciden?", coinciden(media_bucle, media_funciones, media_pandas))

# Interpretación: de media, cada alumno ha sacado 74 puntos en la prueba.
# Si repartiéramos todos los puntos a partes iguales, cada uno tendría 74.

# =================================================================
print("\nSolución del ejercicio 3")
# =================================================================
# Mediana: el valor central de los datos ordenados.
# Si n es par, es la media de los dos valores centrales.

# Método 1: ordenamos a mano (ordenación por selección) y miramos par/impar
ordenados = puntos.copy()
for i in range(len(ordenados)):
    pos_min = i
    for j in range(i + 1, len(ordenados)):
        if ordenados[j] < ordenados[pos_min]:
            pos_min = j
    ordenados[i], ordenados[pos_min] = ordenados[pos_min], ordenados[i]

n = len(ordenados)
if n % 2 == 0:
    mediana_bucle = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
else:
    mediana_bucle = ordenados[n // 2]

# Método 2: sorted() + índices
ordenados_f = sorted(puntos)
mitad = len(ordenados_f) // 2
mediana_funciones = (
    (ordenados_f[mitad - 1] + ordenados_f[mitad]) / 2
    if len(ordenados_f) % 2 == 0
    else ordenados_f[mitad]
)

# Método 3: pandas
mediana_pandas = df["puntos_prueba"].median()

print("mediana_bucle:     ", mediana_bucle)
print("mediana_funciones: ", mediana_funciones)
print("mediana_pandas:    ", mediana_pandas)
print("¿Coinciden?", coinciden(mediana_bucle, mediana_funciones, mediana_pandas))

# Interpretación: la mediana deja la mitad de los alumnos por debajo y la
# otra mitad por encima. Con 10 datos, el centro cae entre el 5.º (70) y el
# 6.º (80), así que la mediana es 75. A diferencia de la media, no le afectan
# los valores extremos.

# =================================================================
print("\nSolución del ejercicio 4")
# =================================================================
# Moda: el valor que más se repite.

# Método 1: diccionario de frecuencias con un bucle
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1

moda_bucle = None
max_repeticiones = 0
for valor, veces in frecuencias.items():
    if veces > max_repeticiones:
        max_repeticiones = veces
        moda_bucle = valor

# Método 2: set() + count() + max() con lambda
moda_funciones = max(set(puntos), key=lambda x: puntos.count(x))

# Método 3: pandas (.mode() devuelve una Serie; cogemos el primero)
moda_pandas = df["puntos_prueba"].mode()[0]

print("Frecuencias:", frecuencias)
print("moda_bucle:     ", moda_bucle)
print("moda_funciones: ", moda_funciones)
print("moda_pandas:    ", moda_pandas)
print("¿Coinciden?", coinciden(moda_bucle, moda_funciones, moda_pandas))

# Interpretación: 80 es la puntuación más frecuente; la han sacado 3 alumnos
# (Fátima, Gonzalo y Hugo). Es el resultado "más típico" del grupo.

# =================================================================
print("\nSolución del ejercicio 5")
# =================================================================
# Desviación de cada dato: cuánto se aleja de la media (punto - media).
media = media_bucle

# Método 1: bucle + append()
desviaciones_bucle = []
for valor in puntos:
    desviaciones_bucle.append(valor - media)

# Método 2: map() + lambda
desviaciones_funciones = list(map(lambda x: x - media, puntos))

# Método 3: pandas, nueva columna
df["desviacion"] = df["puntos_prueba"] - df["puntos_prueba"].mean()
desviaciones_pandas = list(df["desviacion"])

print("desviaciones_bucle:     ", desviaciones_bucle)
print("desviaciones_funciones: ", desviaciones_funciones)
print("desviaciones_pandas:    ", desviaciones_pandas)
print("¿Coinciden?", listas_coinciden(desviaciones_bucle,
                                      desviaciones_funciones,
                                      desviaciones_pandas))

# Interpretación:
#  - Positiva: el alumno ha sacado más puntos que la media.
#  - Negativa: ha sacado menos que la media.
#  - Cero: ha sacado exactamente la media.
# (Si sumamos todas las desviaciones, siempre da 0.)

# =================================================================
print("\nSolución del ejercicio 6")
# =================================================================
# Varianza poblacional: media de los cuadrados de las desviaciones.

# Método 1: bucle -> desviación -> cuadrado -> acumulamos -> dividimos entre n
suma_cuadrados = 0
for valor in puntos:
    desviacion = valor - media_bucle
    suma_cuadrados += desviacion ** 2
varianza_bucle = suma_cuadrados / len(puntos)

# Método 2: map() + lambda + sum() + len()
varianza_funciones = sum(map(lambda x: (x - media_funciones) ** 2, puntos)) / len(puntos)

# Método 3: pandas con ddof=0 (divide entre n, no entre n-1)
varianza_pandas = df["puntos_prueba"].var(ddof=0)

print("varianza_bucle:     ", varianza_bucle)
print("varianza_funciones: ", varianza_funciones)
print("varianza_pandas:    ", varianza_pandas)
print("¿Coinciden?", coinciden(varianza_bucle, varianza_funciones, varianza_pandas))

# Interpretación: la varianza mide lo dispersos que están los datos respecto
# a la media. Cuanto mayor, más diferentes son las notas entre sí. Su
# inconveniente es que está en "puntos al cuadrado", lo que cuesta de leer.

# =================================================================
print("\nSolución del ejercicio 7")
# =================================================================
# Desviación estándar: raíz cuadrada de la varianza.

# Método 1: partimos de la varianza calculada con bucles
desviacion_estandar_bucle = math.sqrt(varianza_bucle)

# Método 2: todo en una expresión funcional
desviacion_estandar_funciones = math.sqrt(
    sum(map(lambda x: (x - media_funciones) ** 2, puntos)) / len(puntos)
)

# Método 3: pandas
desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

print("desviacion_estandar_bucle:     ", desviacion_estandar_bucle)
print("desviacion_estandar_funciones: ", desviacion_estandar_funciones)
print("desviacion_estandar_pandas:    ", desviacion_estandar_pandas)
print("¿Coinciden?", coinciden(desviacion_estandar_bucle,
                              desviacion_estandar_funciones,
                              desviacion_estandar_pandas))

# Interpretación: está en las mismas unidades que los datos (puntos), así que
# se entiende directamente: las notas se alejan de la media unos 14 puntos
# de forma típica. La varianza (204) está en puntos², que no es intuitivo.

# =================================================================
print("\nSolución del ejercicio 8")
# =================================================================
# Normalización min-max: (valor - mínimo) / (máximo - mínimo) -> rango [0, 1]

# Método 1: buscamos mínimo y máximo con un bucle y normalizamos con append()
minimo = puntos[0]
maximo = puntos[0]
for valor in puntos:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor

normalizados_bucle = []
for valor in puntos:
    normalizados_bucle.append((valor - minimo) / (maximo - minimo))

# Método 2: min(), max(), map() y lambda
minimo_f, maximo_f = min(puntos), max(puntos)
normalizados_funciones = list(
    map(lambda x: (x - minimo_f) / (maximo_f - minimo_f), puntos)
)

# Método 3: pandas
col = df["puntos_prueba"]
df["puntos_normalizados"] = (col - col.min()) / (col.max() - col.min())
normalizados_pandas = list(df["puntos_normalizados"])

print("Mínimo:", minimo, "| Máximo:", maximo)
print("normalizados_bucle:     ", redondear(normalizados_bucle))
print("normalizados_funciones: ", redondear(normalizados_funciones))
print("normalizados_pandas:    ", redondear(normalizados_pandas))
print("¿Coinciden?", listas_coinciden(normalizados_bucle,
                                      normalizados_funciones,
                                      normalizados_pandas))

# Interpretación:
#  - 0   -> es la nota más baja del grupo (el mínimo).
#  - 0.5 -> está justo a mitad de camino entre el mínimo y el máximo.
#  - 1   -> es la nota más alta del grupo (el máximo).

# =================================================================
print("\nSolución del ejercicio 9")
# =================================================================
# Estandarización z-score: z = (valor - media) / desviación estándar

media_z = media_bucle
desv_z = desviacion_estandar_bucle

# Método 1: bucle + append()
z_bucle = []
for valor in puntos:
    z_bucle.append((valor - media_z) / desv_z)

# Método 2: map() + lambda con las variables ya calculadas
z_funciones = list(map(lambda x: (x - media_z) / desv_z, puntos))

# Método 3: pandas
df["puntos_estandarizados"] = (col - col.mean()) / col.std(ddof=0)
z_pandas = list(df["puntos_estandarizados"])

print("z_bucle:     ", redondear(z_bucle))
print("z_funciones: ", redondear(z_funciones))
print("z_pandas:    ", redondear(z_pandas))
print("¿Coinciden?", listas_coinciden(z_bucle, z_funciones, z_pandas))

# Interpretación:
#  - z positivo: la nota está por encima de la media.
#  - z negativo: la nota está por debajo de la media.
#  - z cercano a 0: la nota está muy cerca de la media.
# El número indica a cuántas desviaciones estándar está de la media.

# =================================================================
print("\nSolución del ejercicio 10")
# =================================================================
# Alumnos por encima y por debajo de la media.

# Método 1: bucle + condicional
encima_bucle = []
debajo_bucle = []
for i in range(len(puntos)):
    if puntos[i] > media_bucle:
        encima_bucle.append(nombres[i])
    elif puntos[i] < media_bucle:
        debajo_bucle.append(nombres[i])

# Método 2: filter() + lambda sobre pares (nombre, puntos)
alumnos = list(zip(nombres, puntos))
encima_funciones = list(map(lambda a: a[0],
                            filter(lambda a: a[1] > media_funciones, alumnos)))
debajo_funciones = list(map(lambda a: a[0],
                            filter(lambda a: a[1] < media_funciones, alumnos)))

# Método 3: filtrado de pandas
encima_pandas = list(df[df["puntos_prueba"] > col.mean()]["nombre"])
debajo_pandas = list(df[df["puntos_prueba"] < col.mean()]["nombre"])

print("Por encima de la media (", media_bucle, "):")
print("  bucle:     ", encima_bucle)
print("  funciones: ", encima_funciones)
print("  pandas:    ", encima_pandas)
print("  ¿Coinciden?", encima_bucle == encima_funciones == encima_pandas)

print("Por debajo de la media:")
print("  bucle:     ", debajo_bucle)
print("  funciones: ", debajo_funciones)
print("  pandas:    ", debajo_pandas)
print("  ¿Coinciden?", debajo_bucle == debajo_funciones == debajo_pandas)

# Valores normalizados más alto y más bajo (puede haber empates)
max_norm = df["puntos_normalizados"].max()
min_norm = df["puntos_normalizados"].min()
print("Normalizado más alto:",
      list(df[df["puntos_normalizados"] == max_norm]["nombre"]))
print("Normalizado más bajo:",
      list(df[df["puntos_normalizados"] == min_norm]["nombre"]))

# ¿Algún valor especialmente alejado? Criterio habitual: |z| > 2
alejados = df[df["puntos_estandarizados"].abs() > 2]
if len(alejados) > 0:
    print("Valores alejados (|z| > 2):", list(alejados["nombre"]))
else:
    print("No hay valores especialmente alejados: ningún |z| supera 2.")
    print("Los más extremos son Lucía (z ≈ %.2f) y Ana (z ≈ %.2f)."
          % (df["puntos_estandarizados"].max(), df["puntos_estandarizados"].min()))

# Tabla final con todas las columnas calculadas
print()
print(df[["nombre", "puntos_prueba", "desviacion",
          "puntos_normalizados", "puntos_estandarizados"]].round(3))

# Conclusión
print("\nConclusión:")
print("El grupo tiene un rendimiento medio de 74 puntos y una mediana de 75,")
print("muy parecidas, así que la distribución es bastante equilibrada.")
print("La nota más repetida es 80. La desviación estándar (~14 puntos) indica")
print("una dispersión moderada. La mitad de la clase está por encima de la media")
print("y la otra mitad por debajo, y no hay valores atípicos claros: Lucía (100)")
print("y Ana (50) son los extremos, pero dentro de lo esperable.")