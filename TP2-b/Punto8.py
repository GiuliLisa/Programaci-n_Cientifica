#Reinaldo Giulianna
#2025
#Programación Científica

# 8. Desarrolle un programa que, dados los tres lados de un triángulo rectángulo 
# en centímetros, calcule y muestre tanto su área como su perímetro. A 
# continuación, podemos observar un ejemplo de lo que se espera que el 
# programa muestre en el caso de que el usuario ingrese valores de 3, 4 y 5 
# para cada uno de los lados (tener en cuenta que valores pueden adoptar una 
# unidad de medida). 
# Ingresa a: 3 
# Ingresa b: 4 
# Ingresa c: 5 
# El área del triángulo es 6.0 
# El perímetro del triángulo es 12.0 

print("Ingrese los lados de un triángulo rectángulo en centímetros: ")
a = float(input("Ingrese el Lado 1: "))
b = float(input("Ingrese el Lado 2: "))
c = float(input("Ingrese el Lado 3: "))

if a > b and a > c:
    hipotenusa = a
    cateto1 = b
    cateto2 = c
elif b > a and b > c:
    hipotenusa = b
    cateto1 = a
    cateto2 = c
else:
    hipotenusa = c
    cateto1 = a
    cateto2 = b


if round(cateto1**2 + cateto2**2, 5) == round(hipotenusa**2, 5): #Esto verifica si es un triángulo rectángulo usando el teorema de Pitágoras
    perimetro = a + b + c
    area = (cateto1 * cateto2) / 2
    
    print(f"El área del triángulo rectángulo es de: {area} cm2, y el perímetro es de: {perimetro} cm")
else:
    print("\nLos lados ingresados no forman un triángulo rectángulo.")