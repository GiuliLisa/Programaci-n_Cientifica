#Reinaldo Giulianna
#2025
#Programación Científica

#21 Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.
total_segundos = int(input("Ingrese la cantidad de segundos: "))

minutos = total_segundos // 60
segundos = total_segundos % 60

print(f"El resultado en minutos y segundos es de: {minutos}:{segundos}")