#Reinaldo Giulianna
#2025
#Programación Científica

#25. Imagina partir de una super lista de notas en formato texto, algo parecido a esto: 
# ‘7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;‘. ¿Serías capaz de extraer el patrón para 
# construir un diccionario donde la clave son los nombres y el valor de la puntuación 
# promedio? 

notas = '7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;'

diccionario_promedios = {}

alumnos = notas.split(';;')

for alumno in alumnos:
    if alumno:  
        calificaciones, nombre = alumno.split('#')
        
        lista_calificaciones = [float(x) for x in calificaciones.split(',')]
        
        promedio = sum(lista_calificaciones) / len(lista_calificaciones)
        
        diccionario_promedios[nombre] = promedio


print(diccionario_promedios)
