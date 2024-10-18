import tkinter as tk
from PIL import Image, ImageTk  # Necesario para manejar imágenes con Tkinter

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Perfil")
ventana.configure(bg='purple')  # Color de fondo morado

# Crear el label del título "Mi Perfil"
titulo_label = tk.Label(ventana, text="Mi Perfil", font=("Arial", 24), fg="white", bg="purple")
titulo_label.pack(pady=20)  # Padding en el eje Y

# Crear el label para los datos del perfil
perfil_texto = "Nombre: Jared Ramírez\nCorreo: jaredrmz@geemail.com\nUbicación: Mangos 23, Colonia Prismacolor, Monterrey, Nuevo León\nEdad: 26 Años"
perfil_label = tk.Label(ventana, text=perfil_texto, font=("Arial", 14), fg="white", bg="purple")
perfil_label.pack(pady=10)

# Cargar la imagen del usuario
imagen = Image.open(r'perfil.png')  # Asegúrate de que la ruta a la imagen sea correcta
imagen = imagen.resize((150, 250))  # Redimensionar la imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un label para mostrar la imagen
imagen_label = tk.Label(ventana, image=imagen_tk, bg="purple")
imagen_label.pack(pady=20)

# Crear el botón para actualizar la información
actualizar_boton = tk.Button(ventana, text="Actualizar información", font=("Arial", 14), bg="white", fg="purple")
actualizar_boton.pack(pady=20)

# Ejecutar el loop de la ventana
ventana.mainloop()
