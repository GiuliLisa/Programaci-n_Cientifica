#Reinaldo Giulianna
#2025
#Programación Científica

# 11. Agregar al conversor de unidades las siguientes opciones: 
# a. Centímetros a Metros 
# b. Hectáreas a Metros Cuadrados 
# c. °C a °F 
# d. Kilómetros a Hectáreas 

import tkinter as tk
from tkinter import ttk

def convertir_valor():
    try:
        valor = float(entrada.get())
        seleccion = convertir.get()

        if seleccion == "C2M":
            unidad.config(text="Centímetros:")
            resultado = valor / 100
            resultado2.config(text=f"{resultado:.2f} m")

        elif seleccion == "H2M":
            unidad.config(text="Hectáreas:")
            resultado = valor * 10000
            resultado2.config(text=f"{resultado:.2f} m²")

        elif seleccion == "C2F":
            unidad.config(text="Celsius:")
            resultado = (valor * 9/5) + 32
            resultado2.config(text=f"{resultado:.2f} °F")

        elif seleccion == "K2H":
            unidad.config(text="Kilómetros:")
            resultado = valor * 100
            resultado2.config(text=f"{resultado:.2f} ha")

        elif seleccion == "M2K":
            unidad.config(text="Metros:")
            resultado = valor / 1000
            resultado2.config(text=f"{resultado:.2f} km")

    except ValueError:
        resultado2.config(text="Error")

ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry('300x250')

convertir = tk.StringVar()

unidad = tk.Label(ventana, text="Unidad:")
unidad.pack()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Convertir", command=convertir_valor).pack()

resultado2 = tk.Label(ventana, text="")
resultado2.pack()

ttk.Radiobutton(ventana, text="Metros a Kilómetros", variable=convertir, value="M2K").pack()
ttk.Radiobutton(ventana, text="Centímetros a Metros", variable=convertir, value="C2M").pack()
ttk.Radiobutton(ventana, text="Hectáreas a Metros Cuadrados", variable=convertir, value="H2M").pack()
ttk.Radiobutton(ventana, text="Cº a Fº", variable=convertir, value="C2F").pack()
ttk.Radiobutton(ventana, text="Kilómetros a Hectáreas", variable=convertir, value="K2H").pack()

ventana.mainloop()