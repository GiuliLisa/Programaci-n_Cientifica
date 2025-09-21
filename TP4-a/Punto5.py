#Reinaldo Giulianna
#2025
#Programación Científica

# 5. Realizar un programa en el cual se declaren dos valores enteros por teclado 
# utilizando el método __init__. Calcular después la suma, resta, multiplicación y 
# división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar 
# a la clase Calculadora. 


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def sumar(self):
        res = self.num1 + self.num2
        print(f"El resultado de la suma es: {res}")
        
    def restar(self):
        res = self.num1 - self.num2
        print(f"El resultado de la resta es: {res}")
        
    def multiplicar(self):
        res = self.num1 * self.num2
        print(f"El resultado de la multiplicación es: {res}")
        
    def dividir(self):
        if self.num2 != 0:
            res = self.num1 / self.num2
            print(f"El resultado de la división es: {res}")
        else:
            print(f"No se puede realizar una división por 0")
            
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

calculo = Calculadora(numero1, numero2)

ope = input("Ingrese el símbolo de la operación que desea realizar (+, -, *, /): ")

if ope == "+":
    operacion = calculo.sumar()
elif ope == "-":
    operacion = calculo.restar()
elif ope == "*":
    operacion = calculo.multiplicar()
elif ope == "/":
    operacion = calculo.dividir()