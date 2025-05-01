#Reinaldo Giulianna
#2025
#Programación Científica

#2. Hemos asignado la lista x = [1,2,3] y ahora queremos asignar una copia a “y”. Podríamos hacer y = x[:], pero parece que y = x +[] también funciona. ¿Es así? ¿Por qué? 

# Respuesta:
# y = x[:]
# Esta es la forma clásica y segura de copiar una lista.
# x[:] significa “una porción de toda la lista”.

# y = x + []
# x + [] crea una nueva lista al sumar x con una lista vacía.