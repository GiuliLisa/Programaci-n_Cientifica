#Reinaldo Giulianna
#2025
#Programación Científica

#2. Abrir el archivo y agregar datos personales por ejemplo DNI, correo, nombre.

with open("datos.txt", "a") as archivo:
    archivo.write("Nombre: Giulianna Reinaldo\n")
    archivo.write("DNI: 254789163\n")
    archivo.write("Correo: correo@gmail.com \n")