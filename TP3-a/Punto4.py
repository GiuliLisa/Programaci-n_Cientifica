#Reinaldo Giulianna
#2025
#Programación Científica

# 4. Escribir un programa que permita al usuario obtener un identificador para cada uno
# de los socios de un club. Para eso ingresará nombre completo y número de DNI de
# cada socio, indicando que finalizará el procesamiento mediante el ingreso de un
# nombre vacío.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría
# ingresar más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un
# socio tuviera más de un apellido, el usuario sólo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el
# programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el
# primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI.
# Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258

def validar_dni(dni):
    return 7 <= len(str(dni)) <=8

while True:
    nombre = input("Ingrese nombre completo (nombre-apellido) (o vacío para salir): ")
    if nombre == "":
        break
    
    while True:
        dni = input("Ingrese DNI: ")
        if validar_dni(dni):
            break
        print("DNI inválido. Intente de nuevo.")
    
    partes = nombre.strip().split()
    primer_nombre = partes[0]
    apellido = partes[-1]
    identificador = f"{primer_nombre}{len(apellido)}{dni[:3]}"
    print("Identificador:", identificador)
