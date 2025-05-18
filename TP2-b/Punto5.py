#Reinaldo Giulianna
#2025
#Programación Científica

# 5. ¿Cuál es el error en el siguiente código? Descríbalo. 
# numeros = [10,20,30] 
# for x,y in numeros: 
#     print(x)

#Respuesta: el error del codigo se encuentra en "x,y", ya que la lista numeros 
# contiene solo enteros (10, 20, 30) y no pares de valores.
# Al escribir x, y, el programa espera que cada elemento de la lista sea un conjunto
# de dos valores (como una tupla), pero no lo es. Por eso da error.

# La variable debería ser solo x o solo y, porque al poner solo una letra o la variable
# que sea (por ejemplo: numero) esta variable lo que hace es representar a cada elemento
# de la lista en cada vuelta del recorrido (primero será 10, luego 20 y luego 30).