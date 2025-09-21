#Reinaldo Giulianna
#2025
#Programación Científica

# 9. Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase: 
# a. Un constructor, donde los datos pueden estar vacíos. 
# b. Los setters y getters para cada uno de los atributos. Hay que validar las 
# entradas de datos. 
# c. mostrar(): Muestra los datos de la persona. 
# d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad. 

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        # Se pueden pasar los datos vacíos (None) o completos.
        # Usamos los setters para aprovechar la validación. 
        self._nombre = None #atributo privado
        self._edad = None
        self._dni = None

        # Si se pasa un valor, se asigna usando los setters
        if nombre is not None:
            self.nombre = nombre
        if edad is not None:
            self.edad = edad
        if dni is not None:
            self.dni = dni

    # -----------------------------
    #getter y setter de nombre:
    # -----------------------------
    @property #esto indica que estamos usando un getter, o sea la funcion debajo   
    def nombre(self): #getter
        return self._nombre

    @nombre.setter #Esto define el setter, se pone el nombre del getter.
    def nombre(self, new_nombre): #setter
        #Valida que el nombre no esté vacío y no contenga números.
        if not new_nombre or new_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if any(char.isdigit() for char in new_nombre):
            raise ValueError("El nombre no puede contener números.")
        self._nombre = new_nombre
        # isdigit() es un método de Python que sirve para ver si un carácter es un número.
        
        
    # -----------------------------
    #getter y setter de edad:
    # -----------------------------
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, new_edad):
        #Valida que la edad sea un número entero y mayor o igual a 0.
        if not isinstance(new_edad, int):
            raise ValueError("La edad debe ser un número entero.")
        if new_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = new_edad
        # isinstance() es un método de Python que sirve para ver de qué tipo de dato es un valor.
        #En este caso se esta viendo si es un entero: if not isinstance(new_edad, int):

    # -----------------------------
    #getter y setter de dni:
    # -----------------------------
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, new_dni):
        #Valida que el DNI tenga solo números y longitud correcta (7 u 8 dígitos).
        if not new_dni.isdigit():
            raise ValueError("El DNI debe contener solo números.")
        if len(new_dni) < 7 or len(new_dni) > 8:
            raise ValueError("El DNI debe tener 7 u 8 dígitos.")
        self._dni = new_dni
    
    
#raise ValueError() guarda el error que se debe mostrar cuando usemos el try y el except para manejar errores.
    
    
    
    def mostrar(self):
        print(f"{self.nombre} - Edad: {self.edad}. DNI: {self.dni}")
        
    def EsMayorDeEdad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")
            


persona1 = Persona("Juan Pérez", 20, "12345678")
persona1.mostrar()
persona1.EsMayorDeEdad()
print(persona1.nombre) #persona1.nombre esto seria el getter. Ya que devuelve el nombre.


#usando el setter para modificar:
persona1.nombre = "Juan Lopez"
persona1.mostrar()

#se debe usar try/except porque asi maneja el error y muestra lo que se puso antes en ValueError.
try:
    persona1.edad = -1 #tira error porque no puede ser negativa
except ValueError as e:
    print("Error:", e)

try:
    persona1.edad = 0.2 #tira error porque debe ser numero entero
except ValueError as e:
    print("Error:", e)



persona2 = Persona("Pepita Pérez", 15, "98765432")
persona2.mostrar()
persona2.EsMayorDeEdad()

persona2.dni = "1234567"

try:
    persona2.dni = "5646dwa5" #tira error porque debe contener solo numeros
except ValueError as e:
    print("Error:", e)
    
try:
    persona2.dni = "564674569" #tira error porque debe tener entre 7 y 8 numeros
except ValueError as e:
    print("Error:", e)