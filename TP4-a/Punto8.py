#Reinaldo Giulianna
#2025
#Programación Científica

# 8. Desarrollar un programa que conste de una clase padre Cuenta y dos subclases 
# PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para 
# imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para 
# heredar los datos y uno para mostrar la información. 
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método 
# para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar 
# la información, datos del titular plazo, interés y total de interés. 
# Crear al menos un objeto de cada subclase. 

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def mostrar_datos(self):
        print(f"Titular: {self.titular} - Saldo: {self.cantidad}")

        
        
class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def importe(self):
        return (self.cantidad*self.interes)/100
        
    def mostrar_info(self):
        print("=== Plazo Fijo ===")
        self.mostrar_datos()
        print(f"Plazo: {self.plazo} meses")
        print(f"Interés: {self.interes}%")
        print(f"Importe de Interés: ${self.importe()}")
            
            
class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
        
    def mostrar_info(self):
        print("=== Caja de Ahorro ===")
        self.mostrar_datos()        
        

ahorro = CajaAhorro("Giulianna", 600000)
plazo = PlazoFijo("Pepe", 1000000, 12, 5)

ahorro.mostrar_info()

plazo.mostrar_info()
