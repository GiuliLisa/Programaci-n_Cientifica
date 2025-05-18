#Reinaldo Giulianna
#2025
#Programación Científica

# 10. Desarrolle un programa que cuente y muestre cuántos números múltiplos de 3 y mayores que 15 hay en una lista de números. 

cantidad_multiplos = 0
mayores_de_quince = 0

lista =  [3,90,5,7,18,6,24,68,87,30,46,1,10,12]

for numero in lista:
    if numero % 3 == 0:
        cantidad_multiplos = cantidad_multiplos + 1
    if numero > 15:
        mayores_de_quince = mayores_de_quince + 1
        
print(f"Cantidad de múltiplos de 3: {cantidad_multiplos}")
print(f"Números mayores a 15: {mayores_de_quince}")