#Reinaldo Giulianna
#2025
#Programación Científica

# 10. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es 
# una persona) y cantidad (puede tener decimales). El titular será obligatorio y la 
# cantidad es opcional. Construye los siguientes métodos para la clase: 
# a. Un constructor, donde los datos pueden estar vacíos. 
# b. Los setters y getters para cada uno de los atributos. El atributo no se puede 
# modificar directamente, sólo ingresando o retirando dinero. 
# c. mostrar(): Muestra los datos de la cuenta. 
# d. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad 
# introducida es negativa, no se hará nada. 
# e. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en 
# números rojos.

# -----------------------------
# Clase Cuenta
# -----------------------------
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        """
        Constructor de la clase Cuenta.
        titular: obligatorio.
        cantidad: opcional, por defecto 0.0
        """
        self._titular = titular  # Atributo "privado"
        self._cantidad = float(cantidad)  # Asegura que sea decimal


    # Getter del titular
    @property
    def titular(self):
        return self._titular


    # Getter de cantidad
    @property
    def cantidad(self):
        return self._cantidad


    # -----------------------------
    # No se define setter para titular ni cantidad
    # porque solo se modifican con ingresar() o retirar()
    # -----------------------------


    # Método mostrar
    def mostrar(self):
        """Muestra los datos de la cuenta"""
        print(f"Titular: {self.titular}, Saldo: ${self.cantidad:.2f}")


    # Método ingresar
    def ingresar(self, monto):
        """
        Ingresa dinero a la cuenta.
        Si la cantidad es negativa, no se hace nada.
        """
        if monto > 0:
            self._cantidad += monto


    # Método retirar
    def retirar(self, monto):
        """
        Retira dinero de la cuenta.
        La cuenta puede quedar en números rojos (saldo negativo)
        """
        self._cantidad -= monto



# Prueba
# Crear cuenta con titular y saldo inicial opcional
cuenta1 = Cuenta("Giulianna", 1000.0)

# Mostrar datos de la cuenta
cuenta1.mostrar()   # Titular: Giulianna, Saldo: $1000.00

# Ingresar dinero
cuenta1.ingresar(500)
cuenta1.mostrar()   # Saldo: $1500.00

# Intentar ingresar cantidad negativa
cuenta1.ingresar(-200)
cuenta1.mostrar()   # Saldo sigue $1500.00 (no cambia)

# Retirar dinero
cuenta1.retirar(2000)
cuenta1.mostrar()   # Saldo: -$500.00 (puede quedar negativo)