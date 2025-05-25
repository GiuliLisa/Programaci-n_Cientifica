#Reinaldo Giulianna
#2025
#Programación Científica

# 12. Crea el siguiente módulo:
# El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una
# suma, una resta, un producto y una división entres dos números. Todas ellas
# devolverán el resultado. En las funciones del módulo deberá de haber tratamiento e
# invocación manual de errores para evitar que se quede bloqueada una funcionalidad,
# esto incluye:
# TypeError: En caso de que se envíen valores a las funciones que no sean
# números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no
# válido.
# ZeroDivisionError: En caso de realizar una división por cero. Además deberá
# aparecer un mensaje que informe Error: No es posible dividir entre cero.
# Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que
# deberás importar el módulo y realizar las operaciones de suma y división con
# argumentos a elección.


def suma(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        
def resta(num1, num2):
    try:
        return num1 - num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        
def multi(num1, num2):
    try:
        return num1 * num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        
def div(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir por 0")
        