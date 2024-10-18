import tkinter as tk
from tkinter import messagebox, Toplevel, Entry, Button, Label
from PIL import Image, ImageTk

# Función para cerrar la ventana principal
def close_window(window):
    window.destroy()

# Función para abrir la ventana de adopción
def open_adoption_window():
    adoption_window = Toplevel(root)
    adoption_window.title("Adopción de Sorullo")
    adoption_window.geometry("1200x600")
    adoption_window.config(bg="purple")

    label_info = Label(adoption_window, text="Manda un mensaje a JaredRmz para adoptar esta mascota")
    label_info.pack(pady=10)

    # Campo de entrada de mensaje
    message_field = Entry(adoption_window, width=100)
    message_field.pack(pady=5)
   

    # Botón para enviar mensaje
    def send_message():
        # Muestra el pop-up y cierra la ventana de adopción
        messagebox.showinfo("Mensaje Enviado", "¡Tu mensaje ha sido enviado! JaredRmz se pondrá en contacto contigo pronto c:")
        adoption_window.destroy()

    send_button = Button(adoption_window, text="Enviar", command=send_message)
    send_button.pack(pady=10)

    # Botón para volver
    def return_to_main():
        adoption_window.destroy()

    return_button = Button(adoption_window, text="Volver", command=return_to_main)
    return_button.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Sorullo")
root.geometry("1200x600")
root.config(bg="purple")

# Botón "Back" en la esquina superior izquierda para cerrar la ventana
back_button = Button(root, text="Back", command=lambda: close_window(root))
back_button.place(x=10, y=10)

# Cargar y redimensionar la imagen de la mascota usando PIL
mascota_image = Image.open("gato.png")  # Ruta correcta de la imagen de la mascota
mascota_image_resized = mascota_image.resize((250, 150))  # Redimensionar
mascota_photo = ImageTk.PhotoImage(mascota_image_resized)

mascota_label = Label(root, image=mascota_photo)
mascota_label.place(x=10, y=50)

# Cargar y redimensionar la imagen del perfil usando PIL
perfil_image = Image.open("perfil.png")  # Ruta correcta de la imagen del perfil
perfil_image_resized = perfil_image.resize((65, 100))  # Redimensionar
perfil_photo = ImageTk.PhotoImage(perfil_image_resized)

sorullo_label=Label(root,text="Sorullo",font=("arial",20))
sorullo_label.place(x=400,y=80)

perfil_label = Label(root, image=perfil_photo)
perfil_label.place(x=10, y=290)

# Información del autor
publicado_por_label = Label(root, text="Publicado por\nJaredRmz", width=20, height=2, bg="lightgray", anchor="w")
publicado_por_label.place(x=10, y=260)


# Información central del gato
info_label = Label(root, text="Raza: Gato\nEdad: 6 meses\nColor: Negro\nPadecimientos Médicos: Es sordo de una de sus orejitas", font=("arial",12), justify="left")
info_label.place(x=400, y=150)

# Descripción del gato
descripcion_label = Label(root, text="Sorullo es un gatito muy divertido, le gusta explorar, dormir, y jugar con las bolsas.", font=("arial",11) , width=80, height=8, bg="lightgray")
descripcion_label.place(x=400, y=350)

# Botón "Adoptame" que abre la ventana de adopción
adopt_button = Button(root, text="Adoptame", font=("arial",14), command=open_adoption_window)
adopt_button.place(x=700, y=510)

# Iniciar la ventana principal
root.mainloop()
