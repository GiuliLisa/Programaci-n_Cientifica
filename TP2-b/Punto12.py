#Reinaldo Giulianna
#2025
#Programación Científica

# 12. Desarrolle un programa que cuente y muestre cuántos números impares mayores que 10 hay en una lista de números.
lista = [5,2,10,8,64,7,21,32,18,20,75,44,33,60,1,3]
cantidad = 0
print("Numeros impares mayores a 10:")

for numero in lista:
    if numero > 10 and numero % 2 != 0:
        cantidad = cantidad + 1
        print(numero)
        
print(f"\nCantidad de numeros impares mayores a 10: {cantidad}")