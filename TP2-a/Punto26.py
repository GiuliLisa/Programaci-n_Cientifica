#Reinaldo Giulianna
#2025
#Programación Científica

#26. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
# lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es 
# <teléfono>. 

nombre = input("Ingrese su nombre, por favor: ")
edad = int(input("Ingrese su edad, por favor: "))
direccion = input("Ingrese su dirección, por favor: ")
telefono = int(input("ingrese su telefono, por favor: "))

usuario = {
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono
}

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")