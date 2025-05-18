#Reinaldo Giulianna
#2025
#Programación Científica

# 18. Localiza los errores en los siguientes bloques de código. Crea una excepción 
# para evitar que el programa se bloquee y además explica en un mensaje al 
# usuario la causa y/o solución:  
# a. resultado = 10/0 
# b. lista = [1, 2, 3, 4, 5] 
# lista[10] 
# c. colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  
# colores['blanco'] 
# d. resultado = 15 + "20" 

try:
    resultado = 10/0 #no se puede dividir por 0
except ZeroDivisionError:
    print("Error: División por cero")

try:
    lista = [1, 2, 3, 4, 5] 
    lista[10] #la lista no llega a indice 10 y para mostrar un elemento se necesita print()
except IndexError:
    print("Error: La lista no llega al indice 10")

try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  
    colores['blanco'] #el diccionario no posee la clave "blanco"
except KeyError:
    print("Error: No se encuentra la clave 'blanco' en el diccionario")

try:
    resultado = 15 + "20" #no se puede sumar un numero a una cadena y viceversa.
except TypeError:
    print("Error: No se puede sumar un entero a una cadena")