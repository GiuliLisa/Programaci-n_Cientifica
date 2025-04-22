#Reinaldo Giulianna
#2025
#Programación Científica

#29. Pide al usuario ingresar un valor (número, texto, lista, etc.) y muestra su tipo de dato. 
dato = input("Ingresa un valor (puede ser un número, texto, booleano, lista, etc.): ")

try:
    #Se usa eval para evaluar el valor ingresado y convertirlo al tipo adecuado
    dato_convertido = eval(dato)
except:
    #Si eval falla, lo deja como string
    dato_convertido = dato

#Mostrar el tipo de dato:
print(f"El tipo de dato de lo que ingresaste es: {type(dato_convertido)}")