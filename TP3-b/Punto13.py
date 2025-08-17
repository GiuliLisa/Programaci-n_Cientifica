#Reinaldo Giulianna
#2025
#Programación Científica

# 13. Se necesita un reloj digital que muestre la hora actual en tiempo real en una 
# pantalla (usar after()). 

import tkinter as tk
from tkinter import ttk
import time

# Función que actualiza la hora
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")  # Formato 24 horas
    etiqueta_reloj.config(text=hora_actual)  # Actualiza el texto del label
    ventana.after(1000, actualizar_reloj)    # Llama a esta función otra vez en 1 segundo

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("250x100")

# Etiqueta para mostrar la hora
etiqueta_reloj = ttk.Label(ventana, text="", font=("Helvetica", 32))
etiqueta_reloj.pack(expand=True)

# Iniciar el reloj
actualizar_reloj()

# Ejecutar la aplicación
ventana.mainloop()
