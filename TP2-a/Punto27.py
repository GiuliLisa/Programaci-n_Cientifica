#Reinaldo Giulianna
#2025
#Programación Científica

#27. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
fruta = input("¿Que fruta desea comprar?: ").lower()
kilos = float(input("¿Cuantos kilos?: "))

precios = {
    "manzana" : 500,
    "naranja" : 400,
    "pera" : 650,
    "mandarina": 855,
    "banana" : 786,
    "ananá" : 1000,
    "sandía" : 1500,
    "durazno" : 900,
    "ciruela" : 950
}

if fruta in precios:
    try:
        precio = precios[fruta] * kilos
        print(f"El precio total es de: {precio}")
    except ValueError:
        print("Por favor, ingresa un número válido de kilos.")
else:
    print("Lo siento, no tenemos esa fruta.")