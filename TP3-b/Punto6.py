#Reinaldo Giulianna
#2025
#Programación Científica

#6. Abrir un archivo “json” para lectura. 

import json

with open("notas.json", "r", encoding="UTF-8") as archivo:
    datos = json.load(archivo)

print(datos)


#Así puedo acceder a los datos de forma individual:
print("Nota de Biología:", datos["Biología"])