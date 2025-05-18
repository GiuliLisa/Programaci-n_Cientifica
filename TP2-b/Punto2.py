#Reinaldo Giulianna
#2025
#Programación Científica

#2. Escriba un programa que reciba un entero positivo. Sí el número ingresado es múltiplo de 5 deberá imprimir en pantalla El número es múltiplo de 5, en cualquier otro caso deberá imprimir El número no es múltiplo de 5. 
numero = float(input("Ingrese un numero, por favor: "))

if numero > 0:
    if numero %5 == 0:
        print("El número es múltiplo de 5")
    else:
        print("El número no es múltiplo de 5")