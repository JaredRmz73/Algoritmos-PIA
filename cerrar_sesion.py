import tkinter as tk
from tkinter import messagebox

# Función que será llamada al presionar el botón "Cerrar Sesión"
def cerrar_sesion(ventana):
    # Aquí podrías redirigir a otro módulo o llamar alguna función que maneje el cierre de sesión
    ventana.destroy()  # Cierra la ventana actual
    # Aquí puedes llamar a la función o módulo que deseas para redirigir
    # por ejemplo: modulo_existente.iniciar_sesion()

# Función principal del módulo
def ventana_cerrar_sesion():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Cerrar Sesión")
    ventana.geometry("300x150")
    
    # Crear etiqueta con el mensaje
    etiqueta = tk.Label(ventana, text="¿Seguro que quieres cerrar sesión?", font=("Arial", 12))
    etiqueta.pack(pady=20)
    
    # Crear botón para cerrar sesión
    boton_cerrar_sesion = tk.Button(ventana, text="Cerrar Sesión", font=("Arial", 12), command=lambda: cerrar_sesion(ventana))
    boton_cerrar_sesion.pack(pady=10)
    
    # Ejecutar la ventana
    ventana.mainloop()

# Ejecutar el módulo si se llama directamente
if __name__ == "__main__":
    ventana_cerrar_sesion()
