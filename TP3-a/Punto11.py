#Reinaldo Giulianna
#2025
#Programación Científica

# 11. ¿Existe una excepción para el error con módulos?. Plantear un ejemplo del manejo
# de la misma.

try:
    import modulo_inexistente
except ModuleNotFoundError:
    print("Error: El módulo no existe.")