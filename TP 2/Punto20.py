#Reinaldo Giulianna
#2025
#Programación Científica

#20 Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")