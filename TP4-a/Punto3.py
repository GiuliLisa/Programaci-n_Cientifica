#Reinaldo Giulianna
#2025
#Programación Científica

# 3. Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un
# método “cumpleaños”, que aumente en 1 la edad de la persona cuando se invoque
# sobre un objeto creado con “Persona”.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumpleaños(self):
        self.edad += 1
        print(f"¡{self.nombre} cumplió años! Ahora tiene {self.edad}")
        
        
pepe = Persona("Pepe", 56)
pepe.cumpleaños()