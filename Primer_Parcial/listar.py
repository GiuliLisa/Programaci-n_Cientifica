def listar_productos(productos):
    if not productos:
        print("No hay productos cargados.")
    else:
        print("\n--- Lista de Productos ---")
        for nombre, datos in productos.items():
            print(f"Nombre: {nombre}")
            print(f"  Precio unitario: ${datos['precio']}")
            print(f"  Cantidad disponible: {datos['cantidad']}")
        print(f"\nTotal de productos: {len(productos)}\n")
