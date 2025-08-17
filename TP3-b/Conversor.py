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
        valor = float(valor_entrante.get())
        seleccion = convertir.get()
        
        if seleccion == "C2M":
            resultado = valor / 100
        elif seleccion == "H2M":  # ha a m²
            resultado = valor * 10000
        elif seleccion == "C2F":  # °C a °F
            resultado = (valor * 9/5) + 32
        elif seleccion == "K2H":  # km a ha
            resultado = valor * 100
        
        conversion.config(state="normal") 
        conversion.delete(0, tk.END)
        conversion.insert(0, f"{resultado:.2f}")
        conversion.config(state="readonly") 
    except ValueError:
        conversion.config(state="normal")
        conversion.delete(0, tk.END)
        conversion.insert(0, "Error")
        conversion.config(state="readonly") 

ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x300")
ventana.resizable(False, False)

frm = ttk.Frame(ventana, padding=10)
frm.grid()

convertir = tk.StringVar()

ttk.Label(frm, text="Seleccione la conversión:").grid(row=0, column=0, padx=5, pady=5, sticky="w")

ttk.Radiobutton(frm, text="Centímetros a Metros", variable=convertir, value="C2M").grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frm, text="Hectáreas a Metros Cuadrados", variable=convertir, value="H2M").grid(row=2, column=0, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frm, text="Cº a Fº", variable=convertir, value="C2F").grid(row=3, column=0, padx=5, pady=5, sticky="w")
ttk.Radiobutton(frm, text="Kilómetros a Hectáreas", variable=convertir, value="K2H").grid(row=4, column=0, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Valor:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
valor_entrante = ttk.Entry(frm)
valor_entrante.grid(row=5, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Conversión:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
conversion = ttk.Entry(frm)
conversion.grid(row=6, column=1, padx=5, pady=5, sticky="w")
conversion.config(state="readonly")

btn_convertir = ttk.Button(frm, text="Convertir", command=convertir_valor)
btn_convertir.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        
ventana.mainloop()
