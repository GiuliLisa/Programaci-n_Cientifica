#Reinaldo Giulianna
#2025
#Programación Científica

#3. Cambiar de directorio y crear otro módulo que tenga una función para modificar DNI en archivos. 

def modificar_dni(ruta_archivo, nuevo_dni):
    with open(ruta_archivo, "r") as archivo:
        lineas = archivo.readlines()

    with open(ruta_archivo, "w") as archivo:
        for linea in lineas:
            if linea.startswith("DNI:"):
                archivo.write(f"DNI: {nuevo_dni}\n")
            else:
                archivo.write(linea)


modificar_dni("datos.txt", "87654321")
