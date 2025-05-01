#Reinaldo Giulianna
#2025
#Programación Científica

#28. Construye un sistema escolar entero para el IPET 1308 de 25 de Mayo. Para ello, el 
# diccionario principal contendrá las carreras con la información de precio y nombre. 
# Dentro de estas, existirán nuevos diccionarios para almacenar la siguiente 
# información: ‘profesor, contacto, lista de alumnos totales, evaluación promedio‘. 


carreras = {
    "Analista de Sistemas": {
        "nombre": "Analista de Sistemas de Computación",
        "precio": 40000,
        "profesor": {
            "nombre": "Carlos Gómez",
            "contacto": "carlos.gomez@ipet1308.edu.ar"
        },
        "alumnos": {
            "Ana Pérez": 8.5,
            "Lucas Torres": 7.9,
            "María López": 9.2
        }
    },
    "Secretariado": {
        "nombre": "Secretariado Administrativo",
        "precio": 40000,
        "profesor": {
            "nombre": "Sandra Ruiz",
            "contacto": "sandra.ruiz@ipet1308.edu.ar"
        },
        "alumnos": {
            "Pedro Martínez": 7.0,
            "Valentina Fernández": 8.1
        }
    },
    "Administración": {
        "nombre": "Técnico Superior en Administración de Empresas",
        "precio": 40000,
        "profesor": {
            "nombre": "Martín Herrera",
            "contacto": "martin.herrera@ipet1308.edu.ar"
        },
        "alumnos": {
            "Julieta Gómez": 8.3,
            "Tomás Vidal": 7.5,
            "Brenda Salas": 9.0
        }
    },
    "Profesor/a de Informática": {
        "nombre": "Profesorado de Educación Secundaria en Informática",
        "precio": 40000,
        "profesor": {
            "nombre": "Leonardo Martiteli",
            "contacto": "martin.herrera@ipet1308.edu.ar"
        },
        "alumnos": {
            "Marina Gómez": 8.3,
            "Jorge Lopez": 7.5,
            "Marianela Salasi": 9.0
        }
    },
    "Traductor de Portugués": {
        "nombre": "Traductor de Portugués",
        "precio": 40000,
        "profesor": {
            "nombre": "Julian Herrera",
            "contacto": "julian.herrera@ipet1308.edu.ar"
        },
        "alumnos": {
            "Pepe Ramirez": 8.3,
            "Teo Vivid": 7.5,
            "George Lucas": 9.0
        }
    }
}


for carrera, datos in carreras.items():
    print(f"\nCarrera: {carrera}")
    print(f"Nombre completo: {datos['nombre']}")
    print(f"Precio: ${datos['precio']}")
    print(f"Profesor/a: {datos['profesor']['nombre']}")
    print(f"Contacto: {datos['profesor']['contacto']}")
    print("Alumnos y sus promedios:")
    for alumno, promedio in datos["alumnos"].items():
        print(f" - {alumno}: {promedio}")
