#Reinaldo Giulianna
#2025
#Programación Científica

# 6. En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El 
# banco requiere también al final del día calcular la cantidad de dinero que se ha 
# depositado. 
# Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá 
# los atributos nombre y cantidad y los métodos __init__, depositar, extraer, 
# mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los 
# métodos __init__, operar y deposito_total.

class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad
        
    def depositar(self, monto):
        self.cantidad += monto
        print(f"¡Operación exitosa! Se han depositado ${monto}")
    
    def extraer(self, monto):
        if self.cantidad >= monto:
            self.cantidad -= monto
            print(f"¡Operación exitosa! Se han extraido ${monto}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para extraer {monto}")
    
    def mostrar_total(self):
        print(f"Cliente: {self.nombre} - Saldo: ${self.cantidad}")
    
class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Ana")
        self.cliente2 = Cliente("Pepe")
        self.cliente3 = Cliente("Juan")
        
    def operar(self):
        self.cliente1.depositar(100000)
        self.cliente2.depositar(50000)
        self.cliente3.extraer(12000)
        self.cliente1.extraer(50000)
        self.cliente2.extraer(56000)
    
    def deposito_total(self):
        total = (self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad)
        print(f"El total de dinero en el banco es de ${total}")
        
        
banco = Banco()
banco.operar()
banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()
banco.deposito_total()