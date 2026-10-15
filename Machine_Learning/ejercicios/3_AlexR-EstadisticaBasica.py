# =============================================================================
# EJERCICIOS DE ESTADÍSTICA BÁSICA CON CSV
# =============================================================================
#
# -----------------------------------------------------------------------------
# 1. ARCHIVO DE DATOS
# -----------------------------------------------------------------------------
# Trabajarás con el archivo datos_estadistica_alumnos.csv. El archivo contiene
# datos de 10 alumnos sobre horas de estudio, puntos obtenidos en una prueba,
# ejercicios entregados y minutos de uso de una plataforma.
#
# La columna principal para los cálculos será puntos_prueba, porque tiene
# valores repetidos, un mínimo claro, un máximo claro y una distribución fácil
# de comprobar.
#
#   id | nombre  | horas_estudio | puntos_prueba | ejercicios_entregados | minutos_plataforma
#   ---+---------+---------------+---------------+-----------------------+-------------------
#    1 | Ana     |       2       |      50       |           4           |        30
#    2 | Bruno   |       3       |      60       |           5           |        35
#    3 | Carla   |       4       |      60       |           6           |        40
#    4 | Diego   |       5       |      70       |           7           |        45
#    5 | Elena   |       5       |      70       |           7           |        50
#    6 | Fátima  |       6       |      80       |           8           |        55
#    7 | Gonzalo |       6       |      80       |           8           |        60
#    8 | Hugo    |       7       |      80       |           9           |        65
#    9 | Irene   |       8       |      90       |          10           |        70
#   10 | Lucía   |       9       |     100       |          10           |        80
#
# -----------------------------------------------------------------------------
# 2. FORMA DE TRABAJO
# -----------------------------------------------------------------------------
# Cada cálculo estadístico debe resolverse tres veces. El objetivo es comprobar
# que los tres métodos dan el mismo resultado y entender qué se está
# calculando, no solo llamar a una función de pandas.
#
#   - Método 1: Python elemental, usando listas, variables, for, condicionales,
#     acumuladores e iteraciones.
#   - Método 2: Python funcional, usando en cada caso la herramienta más
#     adecuada: map(), filter(), lambda, sorted(), sum(), min(), max(), set()
#     o count(). No siempre será necesario usar todas.
#   - Método 3: pandas, usando métodos propios de Series y DataFrames.
#   - Después de cada cálculo, muestra los tres resultados por consola y
#     comprueba si coinciden.
#
# IMPORTANTE: en estos ejercicios usa la varianza poblacional, dividiendo
# entre n. En pandas deberás usar ddof=0 para que coincida con el cálculo
# manual.
#
# Ejemplo inicial: cargar el CSV y recorrer una columna
#
import pandas as pd
#
#   df = pd.read_csv("datos_estadistica_alumnos.csv")
#   puntos = list(df["puntos_prueba"])
#
#   # Método 1: bucle
#   suma = 0
#   for valor in puntos:
#       suma += valor
#
#   media_bucle = suma / len(puntos)
#
#   # Método 2: funciones
#   media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)
#
#   # Método 3: pandas
#   media_pandas = df["puntos_prueba"].mean()
#
#   print(media_bucle)
#   print(media_funciones)
#   print(media_pandas)
#
# -----------------------------------------------------------------------------
# 3. EJERCICIOS
# -----------------------------------------------------------------------------
#
# Ejercicio 1. Carga y exploración de datos
#   - Carga el archivo CSV en un DataFrame llamado df.
#   - Muestra las primeras filas.
#   - Guarda la columna puntos_prueba en una variable llamada puntos.
#   - Muestra cuántos datos hay en la columna.
#   - Explica con tus palabras qué representa cada fila del CSV.
#   Pandas que puedes usar: read_csv(), head(), len().
import os

#Metodo 1
ruta_csv = os.path.join(os.path.dirname(__file__), "datos_estadistica_alumnos.csv")
df = pd.read_csv(ruta_csv)

print(df.head())

puntos = list(df["puntos_prueba"])
contador = 0
for valor in puntos:
    contador += 1
print(contador)

# Ejercicio 2. Media
#   - Calcula la media de puntos_prueba con el Método 1: bucle for,
#     acumulador y len().
#   - Calcula la misma media con el Método 2: sum(), len() y, si quieres
#     practicarlo, map() con lambda.
#   - Calcula la misma media con el Método 3: pandas usando .mean().
#   - Muestra los tres resultados con nombres claros: media_bucle,
#     media_funciones y media_pandas.
#   - Comprueba que los tres resultados coinciden.
#   - Explica qué significa esa media en el contexto de la prueba.
#   Pandas que puedes usar: df["puntos_prueba"].mean().
#
# Ejercicio 3. Mediana
#   - Calcula la mediana de puntos_prueba con el Método 1: ordenar la lista,
#     comprobar si la cantidad de datos es par o impar y acceder por índice.
#   - Calcula la misma mediana con el Método 2: sorted(), len() y acceso por
#     índice. En este caso map() no es necesario.
#   - Calcula la misma mediana con el Método 3: pandas usando .median().
#   - Muestra los tres resultados con nombres claros: mediana_bucle,
#     mediana_funciones y mediana_pandas.
#   - Comprueba que los tres resultados coinciden.
#   - Explica por qué la mediana representa el centro de los datos.
#   Pandas que puedes usar: df["puntos_prueba"].median().
#
# Ejercicio 4. Moda
#   - Calcula la moda de puntos_prueba con el Método 1: recorre la lista con
#     un bucle y crea un diccionario de frecuencias.
#   - Calcula la misma moda con el Método 2: usa set(), count(), max() y una
#     lambda para encontrar el valor más repetido.
#   - Calcula la misma moda con el Método 3: pandas usando .mode().
#   - Muestra los tres resultados con nombres claros: moda_bucle,
#     moda_funciones y moda_pandas.
#   - Comprueba que los tres resultados coinciden.
#   - Explica qué significa que ese valor sea la moda.
#   Pandas que puedes usar: df["puntos_prueba"].mode().
#
# Ejercicio 5. Desviación de cada dato respecto a la media
#   - Calcula primero la media de puntos_prueba.
#   - Calcula una lista de desviaciones con el Método 1: bucle for y
#     append(). Cada valor debe ser punto - media.
#   - Calcula la misma lista con el Método 2: map() y lambda.
#   - Calcula las mismas desviaciones con el Método 3: pandas, restando la
#     media directamente a la columna y creando una columna llamada
#     desviacion.
#   - Muestra las tres versiones y comprueba que contienen los mismos valores.
#   - Explica qué significa que una desviación sea positiva, negativa o cero.
#   Pandas que puedes usar: df["desviacion"] = df["puntos_prueba"] - media.
#
# Ejercicio 6. Varianza
#   - Calcula la varianza de puntos_prueba con el Método 1: bucle for,
#     desviaciones, cuadrados y promedio final.
#   - Recuerda: primero se calcula cada desviación, después se eleva al
#     cuadrado y finalmente se hace la media de esos cuadrados.
#   - Calcula la misma varianza con el Método 2: map(), lambda, sum() y len().
#   - Calcula la misma varianza con el Método 3: pandas usando ddof=0.
#   - Muestra los tres resultados con nombres claros: varianza_bucle,
#     varianza_funciones y varianza_pandas.
#   - Comprueba que los tres resultados coinciden.
#   - Explica qué nos dice la varianza sobre el grupo.
#   Pandas que puedes usar: df["puntos_prueba"].var(ddof=0).
#
# Ejercicio 7. Desviación estándar
#   - Calcula la desviación estándar con el Método 1: parte de la varianza
#     calculada con bucles y aplica la raíz cuadrada.
#   - Calcula la misma desviación estándar con el Método 2: usa map(),
#     lambda, sum(), len() y raíz cuadrada.
#   - Calcula la misma desviación estándar con el Método 3: pandas usando
#     .std(ddof=0).
#   - Muestra los tres resultados con nombres claros:
#     desviacion_estandar_bucle, desviacion_estandar_funciones y
#     desviacion_estandar_pandas.
#   - Comprueba que los tres resultados coinciden o que solo cambian por
#     pequeños decimales.
#   - Explica por qué la desviación estándar es más fácil de interpretar que
#     la varianza.
#   Pandas que puedes usar: df["puntos_prueba"].std(ddof=0).
#
# Ejercicio 8. Normalización min-max
#   - Calcula el mínimo y el máximo de puntos_prueba.
#   - Normaliza cada valor con el Método 1: bucle for y append(), usando la
#     fórmula (valor - mínimo) / (máximo - mínimo).
#   - Normaliza los mismos valores con el Método 2: min(), max(), map() y
#     lambda.
#   - Normaliza los mismos valores con el Método 3: pandas usando .min(),
#     .max() y operaciones sobre columnas. Crea una columna llamada
#     puntos_normalizados.
#   - Muestra las tres versiones y comprueba que contienen los mismos valores.
#   - Explica qué significa que un valor normalizado sea 0, 0.5 o 1.
#   Pandas que puedes usar: min(), max() y operaciones directas sobre
#   columnas.
#
# Ejercicio 9. Estandarización z-score
#   - Calcula la media y la desviación estándar de puntos_prueba.
#   - Estandariza cada valor con el Método 1: bucle for y append(), usando la
#     fórmula z = (valor - media) / desviación estándar.
#   - Estandariza los mismos valores con el Método 2: map(), lambda y las
#     variables media y desviación estándar ya calculadas.
#   - Estandariza los mismos valores con el Método 3: pandas usando .mean(),
#     .std(ddof=0) y operaciones sobre columnas. Crea una columna llamada
#     puntos_estandarizados.
#   - Muestra las tres versiones y comprueba que contienen los mismos valores.
#   - Explica qué significa que un valor z sea positivo, negativo o cercano
#     a 0.
#   Pandas que puedes usar: mean(), std(ddof=0) y operaciones directas sobre
#   columnas.
#
# Ejercicio 10. Interpretación final
#   - Indica qué alumnos están por encima de la media usando el Método 1:
#     bucle for y condicional.
#   - Indica los mismos alumnos usando el Método 2: filter() y lambda.
#   - Indica los mismos alumnos usando el Método 3: filtrado de pandas con
#     condiciones sobre columnas.
#   - Indica qué alumnos están por debajo de la media usando también los tres
#     métodos.
#   - Indica qué alumno o alumnos tienen el valor normalizado más alto.
#   - Indica qué alumno o alumnos tienen el valor normalizado más bajo.
#   - Indica si hay algún valor que parezca especialmente alejado del resto.
#   - Escribe una conclusión breve sobre el rendimiento general del grupo.
#
# -----------------------------------------------------------------------------
# 4. ENTREGA
# -----------------------------------------------------------------------------
#   - Entrega un único archivo .py con todos los ejercicios resueltos.
#   - Antes de cada ejercicio, escribe por consola: Solución del ejercicio X.
#   - Incluye comentarios breves explicando qué estás calculando.
# =============================================================================