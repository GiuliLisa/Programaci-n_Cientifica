#Reinaldo Giulianna
#2025
#Programación Científica

# 1. Realizar un programa que tenga una clase Persona con las siguientes
# características. La clase tendrá como atributos el nombre y la edad de una persona.
# Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e
# indicar si la persona es mayor de edad o no.


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
            
    def mostrar_persona(self):
        print(f"{self.nombre} tiene {self.edad} años")
        
    def mostrar_edad(self):
        if self.edad < 18:
            print(f"{self.nombre} es menor de edad")
        elif self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
            
persona1 = Persona("Pepe", 45)
persona2 = Persona("Giulianna", 18)
persona3 = Persona("Melina", 17)

persona1.mostrar_persona()
persona2.mostrar_persona()
persona3.mostrar_persona()

persona1.mostrar_edad()
persona2.mostrar_edad()
persona3.mostrar_edad()
