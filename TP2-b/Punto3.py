#Reinaldo Giulianna
#2025
#Programación Científica

#3. Escriba un programa que reciba como entrada una frase (un string) y 
# determine cuántas veces aparece cada una de las vocales en esa frase. El 
# valor de salida a mostrar debe ser un diccionario, se muestra enseguida un 
# ejemplo: 
# # entrada 
# frase = "hola mundo" 
# # salida 
# {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1} 

cantidad_a = 0
cantidad_e = 0
cantidad_i = 0
cantidad_o = 0
cantidad_u = 0

frase = input("Escriba una frase: ")

frase = frase.lower()

for letra in frase:
    if letra == "a":
        cantidad_a = cantidad_a + 1
    elif letra == "e":
        cantidad_e = cantidad_e + 1
    elif letra == "i":
        cantidad_i = cantidad_i + 1
    elif letra == "o":
        cantidad_o = cantidad_o + 1
    elif letra == "u":
        cantidad_u = cantidad_u + 1
        
print(f"Cantidad de 'a' en la frase: {cantidad_a}")
print(f"Cantidad de 'e' en la frase: {cantidad_e}")
print(f"Cantidad de 'i' en la frase: {cantidad_i}")
print(f"Cantidad de 'o' en la frase: {cantidad_o}")
print(f"Cantidad de 'u' en la frase: {cantidad_u}")