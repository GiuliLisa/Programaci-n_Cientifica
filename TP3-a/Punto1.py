#Reinaldo Giulianna
#2025
#Programación Científica

# 1. Solicitar al usuario que ingrese su dirección de email. Imprimir un mensaje indicando
# si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección
# se considerará válida si contiene el símbolo "@".


def validar_email(email):
    return "@" in email

email = input("Ingrese su dirección de email: ")
if validar_email(email):
    print("La dirección es válida.")
else:
    print("La dirección NO es válida.")
