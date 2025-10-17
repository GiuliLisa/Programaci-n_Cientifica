#Programación Científica.
#Segundo Parcial.
#Reinaldo Giulianna.
#17/10/2025.

#Actividad Nº 4.

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def nombre_completo(self):
        return f"{self.nombre}, {self.apellido}"
        
class AlumnoInscripto(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        
        try:
            if edad < 17:
                raise ValueError("Edad no válida para inscribirse")
            self.edad = edad
            self.carrera = carrera
        except ValueError as e:
            print(f"Error de Inscripción: {e}")
            self.edad = None
            self.carrera = None
        
    def mostrar_datos_academicos(self):
        print(f"{self.nombre_completo()} - Edad: {self.edad}. Carrera: {self.carrera}")
            
def crear_alumno(nombre, apellido, edad, carrera):
    return AlumnoInscripto(nombre, apellido, edad, carrera)

giulianna = crear_alumno("Giulianna", "Reinaldo", 20, "Analista en Sistemas")
giulianna.mostrar_datos_academicos()

pepe = crear_alumno("Pepe", "Lopez", 15, "Programador")
pepe.mostrar_datos_academicos()