#Reinaldo Giulianna
#2025
#Programación Científica

#9. Simular los ejemplos de la documentación tkinter. 

import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi app")
ventana.geometry("300x200")

frm = tk.Frame(ventana, padx=10, pady=10)  # CORRECTO
frm.grid()

tk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.Button(frm, text="Quit", command=ventana.destroy).grid(column=1, row=0)

ventana.mainloop()

#con ttk:
# import tkinter as tk
# from tkinter import ttk

# ventana = tk.Tk()
# ventana.title("Mi app")
# ventana.geometry("300x200")

# frm = ttk.Frame(ventana, padding=10)
# frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=ventana.destroy).grid(column=1, row=0)

# ventana.mainloop()