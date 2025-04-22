#Reinaldo Giulianna
#2025
#Programación Científica

#17 Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros. 
pies = float(input("Ingrese la distancia en pies: "))
pulgadas = float(input("Ingrese la distancia en pulgadas: "))

centimetros = (pies * 30.48) + (pulgadas * 2.54)

print(f"La distancia total en centímetros es: {centimetros:.2f} cm")