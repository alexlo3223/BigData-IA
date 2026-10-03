#Ejercicios 

#Ejercicio 1. Listas: control de notas 
#- Crea una lista llamada notas con cinco calificaciones: 6, 8, 5, 9 y 7. 
#- Guarda en una variable primera_nota el primer elemento de la lista. 
#- Guarda en una variable ultima_nota el último elemento de la lista. 
#- Cambia la segunda nota de la lista por un 10. 
#- Añade una nueva nota, 8, al final de la lista. 
#- Guarda en una variable total_notas la cantidad de notas que hay en la lista. 
#- Muestra por consola la lista final, la primera nota, la última nota y el total de notas. 
#Condición: 
#Debe utilizar: lista, índices, modificación de un elemento, append y len. 

notas = [6,8,5,9,7]

nota_1 = notas[1]
nota_last = notas[-1]
notas[1]=10
notas.append(8)
total_notas = len(notas)

print("Ejercicio 1")
print("Lista final:", notas)
print("Primera nota:", nota_1)
print("Última nota:", nota_last)
print("Total de notas:", total_notas)
print()

#Ejercicio 2. Tuplas: datos fijos de un producto 
#- Crea una tupla llamada producto con tres datos: nombre del producto, precio y unidades disponibles. 
#- Por ejemplo: ("teclado", 25.50, 12). 
#- Guarda cada dato de la tupla en una variable diferente: nombre, precio y unidades. 
#- Calcula el valor total del stock multiplicando precio por unidades. 
#- Muestra por consola el nombre del producto, el precio, las unidades y el valor total del stock. 
#Condición: 
#Debe utilizar: tupla, acceso por índice y operaciones aritméticas sencillas. 

producto = ("raton",25.50,32)

nombre = producto[0]
precio = producto[1]
unidades_disponibles = producto[2]
valor_total_stock = precio*unidades_disponibles

print("Ejercicio 2")
print("Nombre del producto:", nombre)
print("Precio:", precio)
print("Unidades:", unidades_disponibles)
print("Valor total del stock:", valor_total_stock)
print()

#Ejercicio 3. Diccionarios: ficha de alumno 
#- Crea un diccionario llamado alumno. 
#- El diccionario debe tener estas claves: nombre, edad, curso y nota. 
#- Usa valores concretos, por ejemplo: "Ana", 16, "IA" y 7.5. 
#- Muestra por consola el nombre del alumno usando la clave nombre. 
#- Muestra por consola la nota del alumno usando la clave nota. 
#- Cambia la nota del alumno por otro valor.
#- Añade una nueva clave llamada aprobado. Su valor debe ser el resultado de comprobar si la nota es mayor o igual que 5. 
#- Muestra por consola el diccionario completo al final. 
#Condición: 
#Debe utilizar: diccionario, claves de texto, consulta de valores, modificación y creación de una nueva clave. 

alumno = {
    "nombre": "Alex",
    "edad": 19,
    "curso": "BigData",
    "nota": 8.5
}

print("Ejercicio 3")
print("Nombre del alumno:", alumno["nombre"])
print("Nota del alumno:", alumno["nota"])

alumno["nota"] = 9.2
alumno["aprobado"] = alumno["nota"] >= 5

print("Diccionario completo:", alumno)

#Ejercicio 4. Conjuntos: usuarios registrados 
#- Crea un conjunto llamado usuarios con estos nombres: Ana, Luis, Marta, Ana y Pedro. 
#- Crea una variable nuevo_usuario con el valor "Luis". 
#- Crea una variable usuario_existe que compruebe si nuevo_usuario está dentro del conjunto. 
#- Añade el usuario "Clara" al conjunto. 
#- Crea una variable total_usuarios con el número de usuarios únicos. 
#- Muestra por consola el conjunto final, usuario_existe y total_usuarios. 
#Condición: 
#Debe utilizar: conjunto, eliminación automática de duplicados, pertenencia con in y len. 

usuarios = {"Ana","Luis","Matrta","Ana","Pedro"}

nuevo_usuario = "Luis"
usuario_existe = nuevo_usuario in usuarios
usuarios.add("Clara")
total_usuarios = len(usuarios)

print("Ejercicio 4")
print("Conjunto final:", usuarios)
print("¿Usuario existe?:", usuario_existe)
print("Total de usuarios:", total_usuarios)
print()

#Ejercicio 5. Condiciones con and, or y not 
#- Crea las variables edad, tiene_permiso, es_socio y sancionado. 
#- Asigna valores concretos a esas variables. 
#- Crea una variable acceso_por_edad que sea True si la persona tiene al menos 16 años y tiene permiso. 
#- Crea una variable acceso_por_socio que sea True si la persona es socio y no está sancionada. 
#- Crea una variable puede_acceder que sea True si se cumple acceso_por_edad o acceso_por_socio. 
#- Muestra por consola las tres variables: acceso_por_edad, acceso_por_socio y puede_acceder. 
#Condición: 
#La condición final debe utilizar and, or y not. 


edad = 15
tiene_permiso = False
es_socio = False
sancionado = True

acceso_por_edad = edad >= 16 and tiene_permiso == True
acceso_por_socio = es_socio == True and sancionado == False
puede_acceder = acceso_por_edad and acceso_por_socio

print("Ejercicio 5")
print("Acceso por edad:", acceso_por_edad)
print("Acceso por socio:", acceso_por_socio)
print("Puede acceder:", puede_acceder)


# Ejercicio 6. if, elif y else: clasificación de matrícula 
# - Crea las variables nota_media, renta_baja y familia_numerosa. 
# - Asigna valores concretos a esas variables. 
# - Crea una variable mensaje. 
# - Si la nota_media es menor que 5, mensaje debe ser No admitido. 
# - Si la nota_media es mayor o igual que 9, mensaje debe ser Beca completa. 
# - Si la nota_media es mayor o igual que 7 y además renta_baja o familia_numerosa es True, mensaje debe ser Beca parcial. 
# - Si la nota_media es mayor o igual que 5, mensaje debe ser Admitido sin beca. 
# - En cualquier otro caso, mensaje debe ser Revisar solicitud. 
# - Muestra por consola el valor final de mensaje. 
# Condición: 
# Debe resolverse con una estructura que combine if, varios elif y else. 

nota_media = 8
renta_baja = True
familia_numerosa = False

if nota_media < 5:
    mensaje = "No admitido"
elif nota_media >= 9:
    mensaje = "Beca completa"
elif nota_media >= 7 and (renta_baja or familia_numerosa):
    mensaje = "Beca parcial"
elif nota_media >= 5:
    mensaje = "Admitido sin beca"
else:
    mensaje = "Revisar solicitud"

print("Ejercicio 6")
print("Mensaje final:", mensaje)

# Ejercicio 7. Ternaria: mensaje de resultado 
# - Crea una variable nota con un valor numérico. 
# - Usa un condicional ternario para guardar en resultado el texto Aprobado si la nota es mayor o igual que 5, o Suspenso en caso contrario. 
# - Usa otro condicional ternario para guardar en tipo_nota el texto Alta si la nota es mayor o igual que 8, o Normal en caso contrario. 
# - Muestra por consola la nota, el resultado y el tipo de nota. 
# Condición: 
# El ejercicio debe usar al menos dos expresiones ternarias. 

nota = 7
resultado = "Aprobado" if nota >= 5 else "Suspenso"
tipo_nota = "Alta" if nota >= 8 else "Normal"

print("Ejercicio 7")
print("Nota:", nota)
print("Resultado:", resultado)
print("Tipo de nota:", tipo_nota)

# Ejercicio 8. match-case: menú de aplicación 
# - Crea una variable opcion con un texto: crear, editar, borrar, listar u otra opción. 
# - Crea una variable mensaje. 
# - Usa match-case para asignar un mensaje distinto según la opción elegida. 
# - Si opcion es "crear", mensaje debe ser Creando registro. 
# - Si opcion es "editar", mensaje debe ser Editando registro. 
# - Si opcion es "borrar", mensaje debe ser Borrando registro. 
# - Si opcion es "listar", mensaje debe ser Mostrando registros. 
# - Para cualquier otro valor, mensaje debe ser Opción no reconocida. 
# - Muestra por consola el valor de mensaje. 
# Condición: 
# Debe incluirse un case _ como opción por defecto. 

opcion = "editar"

match opcion:
    case "crear":
        mensaje = "Creando registro"
    case "editar":
        mensaje = "Editando registro"
    case "borrar":
        mensaje = "Borrando registro"
    case "listar":
        mensaje = "Mostrando registros"
    case _:
        mensaje = "Opción no reconocida"

print("Ejercicio 8")
print("Mensaje:", mensaje)

# Ejercicio 9. Caso completo: pedido online 
# - Crea una lista llamada productos con tres productos. 
# - Crea una lista llamada precios con tres precios, en el mismo orden que los productos. 
# - Crea un diccionario llamado cliente con las claves nombre, es_socio y saldo. 
# - Crea un conjunto llamado cupones_validos con tres códigos de cupón. 
# - Crea una variable cupon_usado con uno de esos códigos o con un código inventado. 
# - Calcula el total del pedido sumando los tres precios. 
# - Crea una variable tiene_descuento que sea True si el cliente es socio o si el cupón usado está en cupones_validos. 
# - Si tiene_descuento es True, calcula total_final aplicando un descuento del 10%. Si no, total_final será igual al total. 
# - Si el saldo del cliente es mayor o igual que total_final, el mensaje será Pedido aceptado. En caso contrario, será Saldo insuficiente. 
# - Muestra por consola el nombre del cliente, productos, total_final y mensaje. 
# Condición: 
# Debe mezclar listas, diccionarios, conjuntos, operadores aritméticos, operadores lógicos y condicionales. 

productos = ["camiseta", "pantalón", "zapatillas"]
precios = [20, 35, 50]
cliente = {
    "nombre": "Carlos",
    "es_socio": True,
    "saldo": 100
}
cupones_validos = {"DESCUENTO10", "OFERTA20", "PROMO30"}
cupon_usado = "DESCUENTO10"

total = sum(precios)
tiene_descuento = cliente["es_socio"] or cupon_usado in cupones_validos
total_final = total * 0.9 if tiene_descuento else total

if cliente["saldo"] >= total_final:
    mensaje = "Pedido aceptado"
else:
    mensaje = "Saldo insuficiente"

print("Ejercicio 9")
print("Nombre del cliente:", cliente["nombre"])
print("Productos:", productos)
print("Total final:", total_final)
print("Mensaje:", mensaje)

# Ejercicio 10. Caso completo: evaluación de acceso 
# - Crea una tupla llamada requisitos con tres valores: edad mínima, nota mínima y si se requiere permiso. 
# - Ejemplo: requisitos = (18, 6, True). 
# - Crea un diccionario llamado candidato con las claves nombre, edad, nota y permiso. 
# - Crea un conjunto llamado cursos_disponibles con tres cursos. 
# - Crea una variable curso_elegido. 
# - Crea una variable curso_existe que compruebe si curso_elegido está en cursos_disponibles. 
# - Crea una variable cumple_edad comparando la edad del candidato con la edad mínima. 
# - Crea una variable cumple_nota comparando la nota del candidato con la nota mínima. 
# - Crea una variable cumple_permiso. Si el requisito de permiso es True, debe comprobarse el permiso del candidato. Si no se requiere permiso, debe valer True. 
# - Usa if, elif y else para crear un mensaje final: Acceso concedido, Curso no disponible, No cumple requisitos o Solicitud incompleta. 
# - Usa una ternaria para crear un estado breve: Apto si el mensaje final es Acceso concedido, o No apto en caso contrario. 
# - Muestra por consola el nombre del candidato, el curso elegido, el estado breve y el mensaje final. 
# Condición: 
# Debe combinar tuplas, diccionarios, conjuntos, condiciones múltiples, if/elif/else y ternaria.

requisitos = (18, 6, True)
candidato = {
    "nombre": "Lucía",
    "edad": 19,
    "nota": 7,
    "permiso": True
}

cursos_disponibles = {"Python", "BigData", "IA"}
curso_elegido = "Python"
curso_existe = curso_elegido in cursos_disponibles
cumple_edad = candidato["edad"] >= requisitos[0]
cumple_nota = candidato["nota"] >= requisitos[1]
cumple_permiso = candidato["permiso"] if requisitos[2] else True

if not curso_existe:
    mensaje_final = "Curso no disponible"
elif not cumple_edad:
    mensaje_final = "No cumple requisitos"
elif not cumple_nota:
    mensaje_final = "No cumple requisitos"
elif not cumple_permiso:
    mensaje_final = "No cumple requisitos"
else:
    mensaje_final = "Acceso concedido"

estado_breve = "Apto" if mensaje_final == "Acceso concedido" else "No apto"

print("Ejercicio 10")
print("Nombre del candidato:", candidato["nombre"])
print("Curso elegido:", curso_elegido)
print("Estado breve:", estado_breve)
print("Mensaje final:", mensaje_final)

# Ejercicio 11.
#- Diferencias/Similitudes entre:
# "i=i+1", "i++", "++i", "i+=1"

# i = i + 1: suma 1 a i y reasigna el resultado.
i = 0
i = i + 1
print("i=i+1:", i)

# i++: no existe en Python, da SyntaxError.
# i++
# print("i++:", i)

# ++i: es válido pero no hace nada (dos "+" unarios).
++i
print("++i:", i)

# i += 1: equivale a i = i + 1, es la forma habitual de incrementar.
i += 1
print("i+=1:", i)

# Ejercicio 12.
#- "Zip" y "enumerate" en iterables

frutas = ["manzana", "banana", "cereza"]

# Recorre la lista elemento a elemento.
for fruta in frutas:
    print(fruta)

# enumerate: da el índice junto con cada elemento.
for index, fruta in enumerate(frutas):
    print(index, fruta)

# zip: recorre dos iterables a la vez, emparejando sus elementos.
for fruta1, fruta2 in zip(frutas, frutas):
    print(fruta1, fruta2)