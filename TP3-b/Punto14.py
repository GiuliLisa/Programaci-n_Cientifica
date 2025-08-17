#Reinaldo Giulianna
#2025
#Programación Científica

# 14. Una empresa necesita crear contraseñas seguras para los PCs de sus 
# oficinas. Crear una aplicación que permite generar contraseñas seguras de 
# manera aleatoria. Se deben definir los criterios y documentar los mismos.

# Criterios:
# Longitud de 12 caracteres
# Letras en mayúscula y en minúscula
# Números
# Símbolos

import tkinter as tk
from tkinter import ttk
import random
import string

# Criterios de contraseña segura
longitud = 12
caracteres = string.ascii_letters + string.digits + string.punctuation
# ascii_letters = a-z + A-Z
# digits = 0-9
# punctuation = !@#$%...

def generar_contraseña():
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    entrada_contraseña.config(state="normal")
    entrada_contraseña.delete(0, tk.END)
    entrada_contraseña.insert(0, contraseña)
    entrada_contraseña.config(state="readonly")

# Ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x150")
ventana.resizable(False, False)

# Frame
frame = ttk.Frame(ventana, padding=10)
frame.pack(expand=True)

# Label y botón
ttk.Label(frame, text="Contraseña segura generada:").pack(pady=5)
entrada_contraseña = ttk.Entry(frame, width=40, font=("Consolas", 12))
entrada_contraseña.pack()
entrada_contraseña.config(state="readonly")

ttk.Button(frame, text="Generar contraseña", command=generar_contraseña).pack(pady=10)

ventana.mainloop()
