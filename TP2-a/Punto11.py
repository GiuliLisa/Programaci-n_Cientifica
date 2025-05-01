#Reinaldo Giulianna
#2025
#Programación Científica

#11. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Ingrese su palabra: ")
 
palabra_revez = palabra[::-1]
 
if palabra == palabra_revez:
    print("Esta palabra un palíndromo")
else:
    print("Esta palabra no es un palíndromo")