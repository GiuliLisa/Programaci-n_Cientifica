#Reinaldo Giulianna
#2025
#Programación Científica

#32. Convierte un carácter a su código ASCII (ord) y viceversa (chr). 
caracter = input("Ingresa un carácter: ")
codigo_ascii = ord(caracter)
print(f"El código ASCII de '{caracter}' es: {codigo_ascii}")

#Convierte un código ASCII a su carácter
codigo = int(input("Ingresa un código ASCII: "))
caracter_convertido = chr(codigo)
print(f"El carácter correspondiente al código ASCII {codigo} es: '{caracter_convertido}'")