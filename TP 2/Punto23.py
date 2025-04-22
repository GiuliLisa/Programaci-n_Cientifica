#Reinaldo Giulianna
#2025
#Programación Científica

#23 Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son. 
cantidad = int(input("Ingrese la cantidad total de unidades: "))

gruesas = cantidad // 144
docenas = (cantidad % 144) // 12
unidades = cantidad % 12

print(f"{cantidad} unidades son {gruesas} gruesas, {docenas} docenas y {unidades} unidades.")