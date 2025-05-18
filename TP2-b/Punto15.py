#Reinaldo Giulianna
#2025
#Programación Científica

# 15. Aplicar descuentos en compras al por mayor: Una frutería ofrece las 
# manzanas con descuento según la siguiente tabla: 
# kilos comprados: 0 - 2 descuento: 0%
# kilos comprados: 2.01 - 5 descuento: 10%
# kilos comprados: 5.01 - 10 descuento: 15%
# kilos comprados: 10.01 descuento: 20%

manzana = float(input("Ingrese el precio del kilo de manzana: "))

kilos = float(input("Ingrese los kilos a comprar: "))

if kilos >= 0 and kilos <=2:
    precio = (manzana * kilos)
elif kilos >=2.01 and kilos <=5:
    precio = (manzana * kilos) * 10 / 100
elif kilos >=5.01 and kilos <=10:
    precio = (manzana * kilos) * 15 / 100
elif kilos >=10.01:
    precio = (manzana * kilos) * 20 / 100
    
print(f"El precio a pagar es de: {round(precio, 2)}")