#Reinaldo Giulianna
#2025
#Programación Científica

#10  Pide dos números y una operación (+, -, *, /), luego muestra el resultado. 
n1 = float(input("Ingrese un numero, por favor: "))
n2 = float(input("Ingrese un segundo numero, por favor: "))
op = input("Ingrese un operador: ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida.")