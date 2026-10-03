#Ejercicio 1. Control de notas
#Crea una lista llamada notas con al menos 10 calificaciones numéricas.
#El programa debe:
#- Mostrar todas las notas.
#- Calcular cuántas notas están aprobadas y cuántas suspendidas.
#- Calcular la nota media.
#- Mostrar la nota más alta y la nota más baja.
#- Indicar si la media final está aprobada o suspendida.
#Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.

notas = [7, 5, 9, 4, 6, 3, 8, 10, 2, 5]
aprobadas = 0
suspendidas = 0
suma_notas = 0

nota_alta = max(notas)
nota_baja = min(notas)

for nota in notas:
    suma_notas += nota
    if nota >= 5:
        aprobadas += 1
    else:
        suspendidas += 1

media = suma_notas / len(notas)

print("Ejercicio 1")
print("Notas:", notas)
print("Aprobadas:", aprobadas)
print("Suspendidas:", suspendidas)
print("Nota media:", media, "Aprobada" if media >= 5 else "Suspendida")
print("Nota más alta:", nota_alta)
print("Nota más baja:", nota_baja)

#Ejercicio 2. Carrito de la compra
#Crea dos listas: una con nombres de productos y otra con sus precios.
#productos = ["pan", "leche", "arroz", "huevos"]
#precios = [1.20, 0.95, 2.10, 2.80]
#El programa debe:
#- Mostrar cada producto con su precio.
#- Calcular el precio total de la compra.
#- Aplicar un descuento del 10% si el total supera 20 euros.
#- Mostrar el total final que debe pagarse.
#Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.

productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]
total = 0

for producto, precio in zip(productos, precios):
    print(f"{producto}: {precio} euros")
    total += precio

if total > 20:
    total *= 0.9

print("")
print("Ejercicio 2")
print("Total final: ",total," euros")

#Ejercicio 3. Registro de alumno
#Crea un diccionario llamado alumno con los siguientes datos:
#nombre
#edad
#curso
#nota_media
#faltas
#El programa debe:
#- Mostrar todos los datos del alumno.
#- Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
#- Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
#- Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
#Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.
#Ejercicios de programación en Python · 2

alumno = {
    "nombre": "Juan Pérez",
    "edad": 16,
    "curso": "4º ESO",
    "nota_media": 6.5,
    "faltas": 12
}

print("")
print("Ejercicio 3")

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

if alumno["nota_media"] >= 5:
    resultado_academico = "aprobado"
else:
    resultado_academico = "suspendido"

if alumno["faltas"] > 10:
    aviso_faltas = "debe recibir un aviso por faltas"
else:
    aviso_faltas = "no debe recibir un aviso por faltas"

print(f"El alumno está {resultado_academico} y {aviso_faltas}.")


#Ejercicio 4. Números pares, impares y múltiplos
#Usando range, recorre los números del 1 al 50.
#El programa debe:
#- Contar cuántos números son pares.
#- Contar cuántos números son impares.
#- Contar cuántos números son múltiplos de 5.
#- Mostrar los tres resultados finales.
#Condición: Debe utilizar for, range, el operador módulo % y contadores.

pares = 0
impares = 0
multiplos_5 = 0

for i in range(1, 51):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

    if i % 5 == 0:
        multiplos_5 += 1

print("")
print("Ejercicio 4")
print("Números pares:", pares)
print("Números impares:", impares)
print("Múltiplos de 5:", multiplos_5)

#Ejercicio 5. Validación de contraseña
#Crea una variable llamada password con una contraseña de prueba.
#El programa debe:
#- Comprobar si la contraseña tiene al menos 8 caracteres.
#- Comprobar si contiene el símbolo @.
#- Comprobar que no sea igual a 12345678.
#- Si cumple todas las condiciones, mostrar Contraseña válida.
#- En caso contrario, mostrar Contraseña no válida.
#Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro
#del texto puede utilizarse "@" in password.

print("")
print("Ejercicio 5")
password = "mi@contraseña"

print("Resultado ejercicio 5:\n")
if len(password) >= 8 and "@" in password and password != "12345678":
    print("Contraseña válida")
else:
    print("Contraseña no válida")

#Ejercicio 6. Inventario de productos
#Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades
#disponibles.
#inventario = {
#"ratón": 12,
#"teclado": 5,
#"monitor": 0,
#"cable": 25
#}
#El programa debe:
#- Mostrar todos los productos y sus unidades.
#- Mostrar qué productos están agotados.
#- Calcular cuántas unidades hay en total.
#- Mostrar cuántos productos tienen menos de 10 unidades.
#Condición: Debe utilizar diccionarios, items(), acumuladores, contadores e if.

print("")
print("Ejercicio 6")
inventario = {
    "ratón": 12,
    "teclado": 5,
    "monitor": 0,
    "cable": 25
}

total_unidades = 0
productos_menos_10 = 0

for producto, unidades in inventario.items():
    print(producto, ":", unidades)
    total_unidades += unidades
    if total_unidades >= 10:
        productos_menos_10 += 1
    

#Ejercicio 7. Búsqueda en una lista
#Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar.
#El programa debe:
#- Recorrer la lista buscando ese nombre.
#- Si encuentra el nombre, mostrar en qué posición está.
#- Cuando lo encuentre, detener la búsqueda.
#- Si no lo encuentra, mostrar Alumno no encontrado.
#Condición: Debe utilizar listas, for, enumerate, if, break y una variable booleana de control.
#Ejercicios de programación en Python · 3

print("")
print("Ejercicio 7")
alumnos = ["Juan","Paco","Raul","Jose","Maria","Sofia"]
nombre_buscar = "Paco"
encontrado = False

for posicion,alumno in enumerate(alumnos):
    if alumno == nombre_buscar:
        print("Nombre",nombre_buscar, "esta en la posicion",posicion)
        encontrado = True
        break

if not encontrado:
    print("Alumno no encontrado")

#Ejercicio 8. Limpieza de datos
#Crea una lista con varios números, incluyendo positivos, negativos y ceros.
#El programa debe:
#- Recorrer la lista completa.
#- Ignorar los números negativos usando continue.
#- Sumar solo los números positivos.
#- Contar cuántos ceros hay.
#- Mostrar la suma final y la cantidad de ceros.
#Condición: Debe utilizar listas, for, continue, un acumulador y un contador.

numeros = [5, -3, 0, 12, -7, 0, 8, 0, -1, 4]
suma_positivos = 0
contador0 = 0

for num in numeros:
    if num < 0:
        continue
    if num > 0:
        suma_positivos += num
    if num == 0:
        contador0 += 1

print("")
print("Ejercicio 8:")
print("Suma de positivos:", suma_positivos)
print("Cantidad de ceros:", contador0)

#Ejercicio 9. Clasificación de usuarios
#Crea una lista de diccionarios. Cada diccionario representa un usuario con los siguientes datos:
#nombre
#edad
#activo
#puntos
#El programa debe:
#- Clasificar como Premium a los usuarios activos con 100 puntos o más.
#- Clasificar como Estándar a los usuarios activos con menos de 100 puntos.
#- Clasificar como Inactivo a los usuarios que no estén activos.
#- Además, si el usuario es menor de 18 años, debe indicarse como usuario menor de edad.
#- Mostrar el nombre de cada usuario y su clasificación.
#Condición: Debe utilizar una lista de diccionarios, bucle for, booleanos, if, elif, else y operadores lógicos.

usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True, "puntos": 150, "clasificacion":""},
    {"nombre": "Luis", "edad": 17, "activo": True, "puntos": 80, "clasificacion":""},
    {"nombre": "Marta", "edad": 30, "activo": False, "puntos": 200, "clasificacion":""},
    {"nombre": "Pablo", "edad": 16, "activo": True, "puntos": 120, "clasificacion":""},
]

print("")
print("Ejercicio 9")

for usuario in usuarios:
    if usuario["activo"] and usuario["puntos"] >= 100:
        usuario["clasificacion"] = "Premium"
    elif usuario["activo"] and usuario["puntos"] < 100:
        usuario["clasificacion"] = "Estandar"
    else:
        usuario["clasificacion"] = "Inactivo"
    
    if usuario["edad"] < 18:
        usuario["clasificacion"] += "(Usuario es menor de edad)"

    print(f"{usuario["nombre"]}: {usuario["clasificacion"]}")

#Ejercicio 10. Sistema de intentos
#Crea una variable codigo_correcto y una lista llamada intentos con varios códigos introducidos.
#El programa debe:
#- Recorrer todos los intentos.
#- Mostrar cada intento realizado.
#- Si un intento está vacío, debe entrar en una condición donde se use pass como marcador.
#- Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle.
#- Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado.
# Condición: Debe utilizar listas, for, if, elif, else, break, pass, una variable booleana y un condicional final.
print("")
print("Ejercicio 10")

codigo_correcto = "4321"
intentos = ["1111", "", "0000", "4321", "9999"]
acceso = False

for intento in intentos:
    print("Intento:",intento)
    if intento == None:
        pass
    elif intento == codigo_correcto:
        acceso = True
        print("Acceso concedido")\
        
        break
    else:
        print("Código incorrecto")

if not acceso:
    print("Acceso denegado")