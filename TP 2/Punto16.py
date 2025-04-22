#Reinaldo Giulianna
#2025
#Programación Científica

#16 Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (IMC), con un decimal.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc:.1f}")