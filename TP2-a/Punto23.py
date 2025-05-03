#Reinaldo Giulianna
#2025
#Programación Científica

#23. Pide al usuario que impute una lista de alumnos, separados con “;”. Después, pregunta por las notas de ellos. Realizar diccionario para después poder preguntar a alguien y observar su nota. 

entrada = input("Ingrese los nombres de los alumnos separados por ';': ")
alumnos = entrada.split(";")

notas = {}

for alumno in alumnos:
    alumno = alumno.strip()
    nota = input(f"Ingrese la nota de {alumno}: ")
    notas[alumno] = nota

consulta = input("Ingrese el nombre del alumno para ver su nota: ")
if consulta in notas:
    print(f"La nota de {consulta} es: {notas[consulta]}")
else:
    print("El alumno no está en la lista.")