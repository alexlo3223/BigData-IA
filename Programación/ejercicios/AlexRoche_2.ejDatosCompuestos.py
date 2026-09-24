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