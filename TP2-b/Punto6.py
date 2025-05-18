#Reinaldo Giulianna
#2025
#Programación Científica

# 6. Modifique el siguiente código para que se muestre en pantalla lo siguiente: 
# x 
# xx 
# xxx 
# xxxx 
# xxxxx 
# for x in range(1,3): 
# print(x * "o")

#Respuesta:
#Encontré dos formas de hacerlo:

#Forma 1
for x in range(1,6): 
    print(x * "x") 
    
#Forma 2
letra = "x"

print(letra)

for x in range(1,5):
    letra = letra + "x"
    print(letra)