#Reinaldo Giulianna
#2025
#Programación Científica

#24. Piensa que quieres usar un diccionario para organizarte. Diseña una agenda donde 
# quieres anotar las tareas. Para ello, pedirás al usuario lo siguiente: 'Dime el día de la 
# semana...' Usuario: lunes. 'Tienes 0 tareas pendientes. ¿Qué anotamos?'. Si hubiera 
# alguna tarea, se mostraría cada elemento. Como ves, la clave será el día y el valor 
# de una lista. 

agenda = {}

dia = input("Dime el día de la semana: ").capitalize()

if dia in agenda:
    print(f"Tienes {len(agenda[dia])} tareas pendientes.")
    for i, tarea in enumerate(agenda[dia], 1):
        print(f"{i}. {tarea}")
else:
    print("Tienes 0 tareas pendientes.")
    agenda[dia] = []

nueva_tarea = input("¿Qué anotamos?: ")
agenda[dia].append(nueva_tarea)

print("\nAgenda actualizada:")
for d, tareas in agenda.items():
    print(f"{d}: {tareas}")
