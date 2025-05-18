#Reinaldo Giulianna
#2025
#Programación Científica

# 9. Desarrolle un programa que calcule y muestre la suma de los primeros n 
# términos de la serie: 1/1 + 1/2 + 1/3 + 1/n

n = int(input("Ingrese la cantidad de términos (n): "))

suma = 0

for i in range(1, n + 1):
    suma += 1 / i

print("La suma de los primeros", n, "términos de la serie es:", suma)
