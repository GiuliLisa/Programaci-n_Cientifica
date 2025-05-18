#Reinaldo Giulianna
#2025
#Programación Científica

# 11. Escriba un programa que, dada una lista o tupla de números, determine 
# cuáles son los valores máximos y mínimos. Evite hacer uso de las funciones 
# min o max nativas de Python. 

lista_o_tupla = [5,40,8,9,57,2,64,10,41,12,13]

minimo = lista_o_tupla[0]
maximo = lista_o_tupla[0]

for numero in lista_o_tupla:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
        
print(maximo)
print(minimo)