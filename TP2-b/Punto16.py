#Reinaldo Giulianna
#2025
#Programación Científica

# 16. Escriba un programa que permita obtener la sucesión de Fibonacci hasta un número X ingresado por el usuario.

limite = int(input("Ingrese un numero límite: "))

a = 0
b = 1

while a <= limite:
    print(a)
    suma = a + b
    a = b
    b = suma