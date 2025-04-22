#Reinaldo Giulianna
#2025
#Programación Científica

#22 Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas, minutos y segundos son.
total_segundos = int(input("Ingrese la cantidad de segundos: "))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"El resultado en minutos y segundos es de: {horas}:{minutos}:{segundos}")