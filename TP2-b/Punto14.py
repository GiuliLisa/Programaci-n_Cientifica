#Reinaldo Giulianna
#2025
#Programación Científica

# 14. En un almacén se descuenta 20% del precio al cliente si el valor a pagar es 
# mayor a $200. Dado un valor de precio, muestre lo que debe pagar el cliente

precio = float(input("Ingrese el precio a pagar: "))

if precio > 200:
    pagar = (precio * 20) / 100
    print(f"El precio a pagar con descuento es de: ${pagar}")
else:
    print(f"El precio a pagar es de: ${precio}")