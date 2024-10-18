import tkinter as tk
from tkinter import ttk

# Función que abre una nueva ventana
def abrir_ventana():
    nueva_ventana = tk.Toplevel(ventana_principal)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("300x200")

    # Ejemplo de agregar más cosas: Etiqueta y botón dentro de la nueva ventana
    label = tk.Label(nueva_ventana, text="¡Esta es una nueva ventana!")
    label.pack(pady=10)

    cerrar_boton = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    cerrar_boton.pack(pady=5)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("400x300")

# Crear un botón que abre una nueva ventana
boton_abrir = ttk.Button(ventana_principal, text="Abrir Nueva Ventana", command=abrir_ventana)
boton_abrir.pack(pady=20)

# Iniciar el bucle principal de tkinter
ventana_principal.mainloop()
