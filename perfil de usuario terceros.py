import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Función para el botón de "Atrás"
def volver_atras():
    print("Volviendo atrás...")

# Crear la ventana principal
root = tk.Tk()
root.title("Perfil de Usuario")
root.geometry("1200x600")
root.configure(bg="#800080")  # Color de fondo morado

# Crear el botón "Atrás" con una flecha
atras_icon = "←"  # Icono de flecha
atras_button = tk.Button(root, text=f"{atras_icon} Atrás", command=volver_atras, bg="#800080", fg="white", bd=0, font=("Arial", 12))
atras_button.place(x=10, y=10)

# Cargar y mostrar la imagen de usuario (sustituir 'persona.png' por la ruta de tu imagen)
image = Image.open(r'persona.png')
image = image.resize((180, 260))
photo = ImageTk.PhotoImage(image)


image_label = tk.Label(root, image=photo, bg="#800080")
image_label.place(x=60, y=70)

# Crear el título "Perfil del usuario"
titulo_label = tk.Label(root, text="Perfil del Usuario", bg="#800080", fg="white", font=("Arial", 60, "bold"))
titulo_label.place(relx=0.35, y=50)

# Crear el marco para los datos del perfil
perfil_frame = tk.Frame(root, bg="#800080")
perfil_frame.place(relx=0.3, rely=0.25)

# Crear los datos del perfil como una lista ordenada
datos_perfil = [
    "Nombre: Juan Reyes",
    "Edad: 25 años",
    "Ubicación: Av. Parque Industrial, Mirasur,Parque Industrial Escobedo, 66050,Cdad. Gral. Escobedo, N.L.",
    "Correo: juanreyes@geemail.com"
]

# Añadir los datos a la ventana
for i, dato in enumerate(datos_perfil, start=1):
    label = tk.Label(perfil_frame, text=f"{i}. {dato}", bg="white", fg="Blue", font=("Arial", 13))
    label.pack(anchor="w")

# Crear el label de "Publicaciones"
publicaciones_label = tk.Label(root, text="Publicaciones:", bg="#800080", fg="white", font=("Arial", 20, "bold"))
publicaciones_label.place(relx=0.50, rely=0.52)

# Crear el marco para las publicaciones (botones)
publicaciones_frame = tk.Frame(root, bg="#800080")
publicaciones_frame.place(relx=0.40, rely=0.6)

# Función para manejar el click en cada botón de publicación
def mostrar_publicacion(nombre):
    print(f"Mostrando la publicación de {nombre}")

# Función auxiliar para crear los botones de mascotas con imagen
def crear_boton_publicacion(nombre, descripcion, imagen_ruta):
    imagen = Image.open(imagen_ruta)
    imagen = imagen.resize((50, 50),)
    imagen_tk = ImageTk.PhotoImage(imagen)
    boton = tk.Button(publicaciones_frame, text=f"{nombre}\n{descripcion}", image=imagen_tk, compound="left",
                      command=lambda: mostrar_publicacion(nombre), bg="white", fg="black", font=("Arial", 16))
    boton.image = imagen_tk  # Para evitar que se pierda la referencia a la imagen
    boton.pack(pady=5, anchor="c")

# Crear los botones con imágenes de mascotas
crear_boton_publicacion("Lolo", "Hamster, 3 meses", r'hamster.png')
crear_boton_publicacion("Sorullo", "Gato, 8 meses", r'gato.png')
crear_boton_publicacion("Alfalfa", "Perrita Terrier Escocés, 2 años", r'perro.png')

# Iniciar el bucle principal de Tkinter
root.mainloop()
