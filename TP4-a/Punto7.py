#Reinaldo Giulianna
#2025
#Programación Científica

# 7. Desarrollar un programa con tres clases: 
# La primera debe ser Universidad, con atributos nombre (Donde se almacena el 
# nombre de la Universidad). La segunda llamada Carerra, con los atributos 
# especialidad (En donde me guarda la especialidad de un estudiante). Y por último, 
# una llamada Estudiante, que tenga como atributos su nombre y edad. El programa 
# debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con 
# un objeto llamado persona.

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad
        
class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera
        
    def mostrar(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}. Universidad: {self.universidad.nombre} - Especialidad: {self.carrera.especialidad}.")
        
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
especialidad = input("Ingrese su especialidad: ")
uni = input("Ingrese el nombre de su universidad: ")

carrera = Carrera(especialidad)
universidad = Universidad(uni)

persona = Estudiante(nombre, edad, universidad, carrera)
persona.mostrar()