from listar import listar_productos

productos = {}

def mostrar_menu():
    print("----- MENÚ DE OPCIONES -----")
    print("1. Cargar producto")
    print("2. Ver lista de productos")
    print("3. Buscar producto por nombre")
    print("4. Calcular valor total del inventario")
    print("5. Salir")

def cargar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    if nombre in productos:
        print("Ese producto ya está cargado.")
        return
    try:
        precio = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        productos[nombre] = {"precio": precio, "cantidad": cantidad}
        print("Producto cargado con éxito.\n")
    except ValueError:
        print("Error: debe ingresar números válidos para precio y cantidad.\n")


def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip().capitalize()
    if nombre in productos:
        datos = productos[nombre]
        print(f"\nProducto encontrado:")
        print(f"  Precio unitario: ${datos['precio']}")
        print(f"  Cantidad disponible: {datos['cantidad']}\n")
    else:
        print("Producto no encontrado.\n")


def calcular_valor_total():
    total = sum(d["precio"] * d["cantidad"] for d in productos.values())
    print(f"\nValor total del inventario: ${total:.2f}\n")


while True:
    mostrar_menu()
    opcion = int(input("Ingrese la opción a elegir: "))
    
    if opcion == 1:
        cargar_producto()
    elif opcion == 2:
        listar_productos(productos)
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        calcular_valor_total()
    elif opcion == 5:
        print("Gracias por usar el programa")
        break
    else:
        print("Ingrese un número válido")