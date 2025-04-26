#Reinaldo Giulianna
#2025
#Programación Científica

#14  Pide la hora actual (formato 24h) e imprime: 
#"Buenos días" si es antes de las 12. 
#"Buenas tardes" si es entre las 12 y 18. 
#"Buenas noches" si es después de las 18.

hora_str = input("Ingrese la hora actual (formato 24h, ejemplo: 17:30): ")

hora_partes = hora_str.split(":")
hora = int(hora_partes[0])

if hora < 12:
    print("Buendos días")
elif hora >= 12 and hora <= 18:
    print("Buenas tardes")
elif hora > 18 and hora <=23:
    print("Buenas noches")
else:
    print("Ingrese una hora valida (entre 0 y 23)")