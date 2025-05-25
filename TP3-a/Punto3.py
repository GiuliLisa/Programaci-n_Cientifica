#Reinaldo Giulianna
#2025
#Programación Científica

# 3. Escribir una función que, dado un número de DNI, retorne True si el número es válido
# y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8
# dígitos

def dni_valido(dni):
    return 7 <= len(str(dni)) <=8

dni = int(input("Ingrese su DNI: "))
print(f"¿Es válido su DNI?: {dni_valido(dni)}")