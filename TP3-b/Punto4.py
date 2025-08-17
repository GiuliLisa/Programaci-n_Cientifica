#Reinaldo Giulianna
#2025
#Programación Científica

#4. Crear un archivo con formato “json”, que contenga nombre de materias y notas. 

import json

materias = {
    "Matemática": 9,
    "Lengua": 8,
    "Historia": 10,
    "Biología": 7
}

# Guardar como archivo JSON
with open("notas.json", "w", encoding="UTF-8") as archivo:
    json.dump(materias, archivo, ensure_ascii=False) #si quiero que se vea una materia debajo de la otra puedo poner: indent=4 (por cada indent)
