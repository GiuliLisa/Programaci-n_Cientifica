#Reinaldo Giulianna
#2025
#Programación Científica

#5. Abrir un archivo “json” para escritura. 

import json

# Reemplaza el contenido o crea uno nuevo
nuevas_materias = {
    "Física": 6,
    "Química": 7
}

with open("notas.json", "w") as archivo:
    json.dump(nuevas_materias, archivo)