import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def cargar_foto():
    ruta_foto = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if ruta_foto:
        entry_foto.delete(0, tk.END)  # Limpiar el campo
        entry_foto.insert(0, ruta_foto)  # Mostrar la ruta de la foto
        # Mostrar la imagen en la interfaz (opcional)
        img = Image.open(ruta_foto)
        img.thumbnail((100, 100))  # Redimensionar la imagen
        img = ImageTk.PhotoImage(img)
        lbl_imagen.config(image=img)
        lbl_imagen.image = img  # Mantener una referencia

def publicar():
    # Obtener los datos del formulario
    nombre = entry_nombre.get()
    foto = entry_foto.get()
    raza = entry_raza.get()
    color = entry_color.get()
    padecimientos = entry_padecimientos.get()
    descripcion = entry_descripcion.get()

    # Validar que todos los campos estén llenos
    if not all([nombre, foto, raza, color, padecimientos, descripcion]):
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return

    # Crear una nueva ventana con los datos introducidos
    ventana_publicacion = tk.Toplevel()
    ventana_publicacion.title("Publicación de Mascota")
    ventana_publicacion.configure(bg='purple')

    # Mostrar los datos
    tk.Label(ventana_publicacion, text="Nombre: " + nombre, bg='purple', fg='white').pack(pady=5)
    tk.Label(ventana_publicacion, text="Foto: ", bg='purple', fg='white').pack(pady=5)

    # Cargar y mostrar la imagen
    img = Image.open(foto)
    img.thumbnail((100, 100))  # Redimensionar la imagen
    img = ImageTk.PhotoImage(img)
    lbl_imagen_publicacion = tk.Label(ventana_publicacion, image=img, bg='purple')
    lbl_imagen_publicacion.image = img  # Mantener referencia a la imagen
    lbl_imagen_publicacion.pack(pady=5)

    tk.Label(ventana_publicacion, text="Raza: " + raza, bg='purple', fg='white').pack(pady=5)
    tk.Label(ventana_publicacion, text="Color: " + color, bg='purple', fg='white').pack(pady=5)
    tk.Label(ventana_publicacion, text="Padecimientos: " + padecimientos, bg='purple', fg='white').pack(pady=5)
    tk.Label(ventana_publicacion, text="Descripción: " + descripcion, bg='purple', fg='white').pack(pady=5)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Crear Publicación")
ventana.geometry("1200x600")
ventana.configure(bg="purple")

# Crear los campos del formulario
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Foto:").pack()
entry_foto = tk.Entry(ventana)
entry_foto.pack()
btn_cargar_foto = tk.Button(ventana, text="Cargar Foto", command=cargar_foto)
btn_cargar_foto.pack()

lbl_imagen = tk.Label(ventana)
lbl_imagen.pack(pady=5)  # Para mostrar la imagen seleccionada

tk.Label(ventana, text="Raza:").pack()
entry_raza = tk.Entry(ventana)
entry_raza.pack()

tk.Label(ventana, text="Color:").pack()
entry_color = tk.Entry(ventana)
entry_color.pack()

tk.Label(ventana, text="Padecimientos Médicos:").pack()
entry_padecimientos = tk.Entry(ventana)
entry_padecimientos.pack()

tk.Label(ventana, text="Descripción:").pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

# Botón de publicar
btn_publicar = tk.Button(ventana, text="Publicar", command=publicar)
btn_publicar.pack(pady=10)

# Iniciar el bucle de la ventana
ventana.mainloop()
