#Reinaldo Giulianna
#2025
#Programación Científica

#33. Pide al usuario ingresar una expresión matemática simple (ej: 2 + 3 * 5) y evalúala. 
expresion = input("Ingresa una expresión matemática (ej: 2 + 3 * 5): ")

try:
    res = eval(expresion)
    print(f"El resultado de la expresión es: {res}")
except Exception as e:
    print(f"Hubo un error al evaluar la expresión: {e}")