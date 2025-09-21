#Reinaldo Giulianna
#2025
#Programación Científica

# 2. Realizar un programa que conste de una clase llamada Alumno que tenga como
# atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus
# atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha
# aprobado o no.

class Alumno:
    def __init__(self, nombre, nota=None): #el None hace referencia a que puede estar vacio (no es obligatorio poner un dato)
        self.nombre = nombre
        self.nota = nota


    def __str__(self):
        return(f"Soy {self.nombre}") #define como queremos mostrar el objeto
        
    def mostrar_nota(self):
        if self.nota >= 6:
            print(f"Soy {self.nombre} me saqué {self.nota} y aprobé")
        elif self.nota < 6:
            print(f"Soy {self.nombre} me saqué {self.nota} y desaprobé")


dic_alumnos = {
    "Giuli" : 9,
    "Pepe" : 5,
    "Marta" : 6
}


for nombre, nota in dic_alumnos.items():
    alumn = Alumno(nombre, nota) #crear un objeto mediante los datos en el diccionario, usando los parámetros del dic.
    alumn.mostrar_nota() #se recorre todo el dic y ya se muestra esa funcion por cada alumno.