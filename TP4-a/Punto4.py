#Reinaldo Giulianna
#2025
#Programación Científica

# 4. Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase
# con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño
# mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_lados(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es un triángulo equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triángulo isóceles")
        else:
            print("Es un triángulo escaleno")
            
    def mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"El lado {self.lado1} es el mayor")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f"El lado {self.lado2} es el mayor")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print(f"El lado {self.lado3} es el mayor")

            
triangulo = Triangulo(10, 5, 7)
triangulo.calcular_lados()
triangulo.mayor()