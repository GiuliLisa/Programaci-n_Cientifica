#Reinaldo Giulianna
#2025
#Programación Científica

#8. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
 
numeros = []

print("Ingresá los 6 números ganadores de la lotería (uno por uno):")

for i in range(6):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

numeros.sort()

print("Números ganadores ordenados de menor a mayor:")
print(numeros)
