#Reinaldo Giulianna
#2025
#Programación Científica

# 4. Desarrolle un programa que reciba una lista de números enteros y calcule cuánto es el porcentaje de números pares que contiene, redondee el porcentaje calculado. 

ingresar = input("Ingrese numeros enteros separados por una coma (Ejemplo: 1,2,3): ")

numeros = [int(num.strip()) for num in ingresar.split(",")]

pares = 0

for numero in numeros:
    if numero %2 == 0:
        pares = pares + 1


total = len(numeros)
porcentaje = round((pares / total)*100)

print(f"El porcentaje de numeros pares es de un: {porcentaje}%")