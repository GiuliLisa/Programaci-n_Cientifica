#Reinaldo Giulianna
#2025
#Programación Científica

# 12. Una enfermera requiere una aplicación para el cálculo del IMC, investigar los 
# datos necesarios y la fórmula que se debe implementar, mostrar un mensaje 
# de salida según el IMC, investigar el orden de correspondencia de los valores 
# de salida. 

import tkinter as tk
from tkinter import ttk

def calcular_imc():
    try:
        p = float(peso.get())
        a = float(altura.get())
        
        resultado = p / (a ** 2)
        
        imc.config(state="normal") 
        imc.delete(0, tk.END)
        imc.insert(0, f"{resultado:.2f}")
        imc.config(state="readonly") 
    except ValueError:
        imc.config(state="normal")
        imc.delete(0, tk.END)
        imc.insert(0, "Error")
        imc.config(state="readonly") 

ventana = tk.Tk()
ventana.title("Calcular IMC")
ventana.geometry("400x300")
ventana.resizable(False, False)

frm = ttk.Frame(ventana, padding=10)
frm.grid()

ttk.Label(frm, text="Peso:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
peso = ttk.Entry(frm)
peso.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Altura:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
altura = ttk.Entry(frm)
altura.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="IMC:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
imc = ttk.Entry(frm)
imc.grid(row=2, column=1, padx=5, pady=5, sticky="w")
imc.config(state="readonly")

btn_convertir = ttk.Button(frm, text="Convertir", command=calcular_imc)
btn_convertir.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
ventana.mainloop()