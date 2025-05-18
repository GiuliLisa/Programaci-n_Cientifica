#Reinaldo Giulianna
#2025
#Programación Científica

#1. Desarrolle un programa que calcule la suma de los enteros del 1 al 100, es decir: 1 + 2 + 3 + … + 99 + 100. 

suma = 0

for numero in range(1, 101):
    suma = suma + numero
    
print(suma)