#Reinaldo Giulianna
#2025
#Programación Científica

# 10. Tomando como referencia el código de la calculadora, cambiar los colores de 
# los números, cambiar el nombre de la calculadora y el tamaño de la ventana. 

import tkinter as tk
from tkinter import ttk

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x200")
ventana.resizable(False, False)

# Frame principal con padding
frm = ttk.Frame(ventana, padding=10)
frm.grid()

# Entradas
ttk.Label(frm, text="Número 1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada1 = ttk.Entry(frm)
entrada1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frm, text="Número 2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entrada2 = ttk.Entry(frm)
entrada2.grid(row=1, column=1, padx=5, pady=5)

# Resultado
ttk.Label(frm, text="Resultado:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
resultado = ttk.Entry(frm)
resultado.grid(row=2, column=1, padx=5, pady=5)
resultado.config(state="readonly")  # Solo lectura

# Función para operar
def calcular(op):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        if op == "+":
            res = n1 + n2
        elif op == "-":
            res = n1 - n2
        elif op == "*":
            res = n1 * n2
        elif op == "/":
            if n2 == 0:
                res = "Error"
            else:
                res = n1 / n2

        # Mostrar resultado
        resultado.config(state="normal")         # Activar campo
        resultado.delete(0, tk.END)              # Borrar lo anterior
        resultado.insert(0, str(res))            # Poner nuevo resultado
        resultado.config(state="readonly")       # Volver a solo lectura

    except ValueError:
        resultado.config(state="normal")
        resultado.delete(0, tk.END)
        resultado.insert(0, "Entrada inválida")
        resultado.config(state="readonly")

# Botones
ttk.Button(frm, text="+", command=lambda: calcular("+")).grid(row=3, column=0, padx=5, pady=5)
ttk.Button(frm, text="-", command=lambda: calcular("-")).grid(row=3, column=1, padx=5, pady=5)
ttk.Button(frm, text="×", command=lambda: calcular("*")).grid(row=4, column=0, padx=5, pady=5)
ttk.Button(frm, text="÷", command=lambda: calcular("/")).grid(row=4, column=1, padx=5, pady=5)

# Ejecutar ventana
ventana.mainloop()
