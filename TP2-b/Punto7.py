#Reinaldo Giulianna
#2025
#Programación Científica

# 7. En una plataforma de aprendizaje en línea, al finalizar cada semana se le 
# envía un mensaje a los usuarios, dependiendo de la cantidad de puntos que 
# han acumulado durante la semana: 
# Más de 10000 puntos — Mensaje: Genial, lo has hecho fenomenal. 
# Entre 6000 y 9999 puntos — Mensaje: Excelente, eres muy dedicado. 
# Entre 3000 y 5999 puntos — Mensaje: Muy bien, sigue así de constante. 
# Entre 1000 y 2999 puntos — Mensaje: Bien, sigue aprendiendo. 
# Menos de 1000 puntos — Mensaje: Es un buen comienzo, no pares. 

puntos = float(input("Ingresá la cantidad de puntos de la semana: "))

if puntos > 10000:
    print("Genial, lo has hecho fenomenal")
elif puntos >=6000 and puntos <=9999:
    print("Excelente, eres muy dedicado")
elif puntos >=3000 and puntos <=5999:
    print("Muy bien, sigue así de constante")
elif puntos >=1000 and puntos <=2999:
    print("Bien, sigue aprendiendo")
elif puntos < 1000:
    print("Es un buen comienzo, no pares")