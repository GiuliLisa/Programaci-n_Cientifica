#Reinaldo Giulianna
#2025
#Programación Científica

# 2. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la
# suma de sus dígitos (utilizando una función que realice dicha suma).

def suma_digitos(numero):
    return sum(int(num) for num in str(numero))

while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    print(f"Suma de dígitos: {suma_digitos(num)}")
