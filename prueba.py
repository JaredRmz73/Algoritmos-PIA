import tkinter as tk
from tkinter import messagebox, Entry, Label, Button, Toplevel, ttk, filedialog
from PIL import Image, ImageTk

# Función para cerrar una ventana
def close_window(window):
    window.destroy()

# Función para cargar una imagen con Pillow y redimensionarla
def load_image(path, size):
    try:
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error de imagen", f"No se pudo cargar la imagen {path}: {e}")
        return None

# Función para crear un botón con imagen de mascota
def create_pet_button(parent, text, image_path, x, y, width=265, height=70):
    pet_img = load_image(image_path, (50, 50))  # Ajustar tamaño de la imagen
    if pet_img is None:
        return
    pet_button = Button(parent, text=text, image=pet_img, compound="left", width=width, height=height, bg="lightgray", fg="black", font=("Arial", 10))
    pet_button.image = pet_img  # Para evitar que la imagen se borre
    pet_button.place(x=x, y=y)

# Función para abrir la ventana de adopción
def open_adoption_window(parent):
    adoption_window = Toplevel(parent)
    adoption_window.title("Adopción de Sorullo")
    adoption_window.geometry("1200x600")
    adoption_window.config(bg="purple")

    label_info = Label(adoption_window, text="Manda un mensaje a JaredRmz para adoptar esta mascota", bg="purple", fg="white", font=("Arial", 14))
    label_info.pack(pady=10)

    # Campo de entrada de mensaje
    message_field = Entry(adoption_window, width=100)
    message_field.pack(pady=5)

    # Botón para enviar mensaje
    def send_message():
        # Obtener el mensaje
        message = message_field.get()
        if message.strip() == "":
            messagebox.showwarning("Mensaje vacío", "Por favor, escribe un mensaje antes de enviar.")
            return
        # Aquí puedes agregar la lógica para enviar el mensaje
        messagebox.showinfo("Mensaje Enviado", "¡Tu mensaje ha sido enviado! JaredRmz se pondrá en contacto contigo pronto 😊")
        adoption_window.destroy()

    send_button = Button(adoption_window, text="Enviar", command=send_message)
    send_button.pack(pady=10)

    # Botón para volver
    return_button = Button(adoption_window, text="Volver", command=adoption_window.destroy)
    return_button.pack(pady=10)

# Función para verificar los datos y mostrar el menú principal
def verificar_datos():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "JaredRmz" and contrasena == "1234":
        messagebox.showinfo("Login exitoso", "Bienvenido, " + usuario)
        ventana_login.withdraw()  # Oculta la ventana de login
        mostrar_menu_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar el menú principal
def mostrar_menu_principal():
    menu_principal = Toplevel()
    menu_principal.title("Menú Principal")
    menu_principal.geometry("1200x600")
    menu_principal.configure(bg="purple")

    # Cargar y mostrar la imagen en el menú principal
    imagen_menu = load_image("patita.png", (150, 150))
    if imagen_menu:
        label_imagen_menu = Label(menu_principal, image=imagen_menu, bg="purple")
        label_imagen_menu.image = imagen_menu
        label_imagen_menu.place(x=10, y=20)

    # Campo de búsqueda
    search_entry = Entry(menu_principal, width=50)
    search_entry.insert(0, "¿Qué buscas hoy?")
    search_entry.place(x=450, y=80)

    # Etiqueta de bienvenida
    label_bienvenida = Label(menu_principal, text="Bienvenido al Menú Principal", bg="purple", fg="white", font=("Arial", 16))
    label_bienvenida.place(x=450, y=50)

    # Etiqueta de publicaciones nuevas
    pub_label = Label(menu_principal, text="Publicaciones Nuevas", bg="white", fg="blue", font=("Arial", 16))
    pub_label.place(x=480, y=130)

    # Función para abrir la ventana de perfil
    def abrir_ventana_perfil():
        nueva_ventana = Toplevel(menu_principal)
        nueva_ventana.title("Mi Perfil")
        nueva_ventana.geometry("1200x600")
        nueva_ventana.configure(bg="purple")
        label = Label(nueva_ventana, text="Mi Perfil", bg="white", fg="blue", font=("Arial", 16))
        label.pack(pady=20)

        # Cargar imagen del perfil
        imagen_ventana = load_image("perfil.png", (150, 250))
        if imagen_ventana:
            label_imagen_ventana = Label(nueva_ventana, image=imagen_ventana, bg="white")
            label_imagen_ventana.image = imagen_ventana
            label_imagen_ventana.place(x=20, y=30)

        # Texto de perfil
        perfil_texto = "Nombre: Jared Ramírez\nCorreo: jaredrmz@geemail.com\nUbicación: Mangos 23, Colonia Prismacolor, Monterrey, Nuevo León\nEdad: 26 Años"
        perfil_label = Label(nueva_ventana, text=perfil_texto, font=("Arial", 12), fg="blue", bg="white", justify="left")
        perfil_label.place(x=200, y=30)

        # Crear botones de mascotas
        create_pet_button(nueva_ventana, "Sorullo, Gato negro, 6 meses", "gato.png", 200, 220)
        create_pet_button(nueva_ventana, "Esteban, Hamster, 2 meses", "hamster.png", 200, 300)
        create_pet_button(nueva_ventana, "Roberta, Perro Escocés, 4 años", "perro.png", 200, 380)

        # Etiqueta de "Mis Publicaciones"
        perfil_2_texto = "Mis Publicaciones"
        perfil_2_label = Label(nueva_ventana, text=perfil_2_texto, font=("Arial", 14), fg="blue", bg="white")
        perfil_2_label.place(x=400, y=250)

        # Botón cerrar ventana perfil
        cerrar_boton = Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
        cerrar_boton.place(x=1100, y=550)

    # Función para abrir la ventana de crear publicación
    def abrir_ventana_crear_publicacion():
        nueva_ventana_2 = Toplevel(menu_principal)
        nueva_ventana_2.title("Crear Publicación")
        nueva_ventana_2.geometry("1200x600")
        nueva_ventana_2.configure(bg="purple")
        label = Label(nueva_ventana_2, text="Crear Publicación", bg="purple", fg="white", font=("Arial", 16))
        label.pack(pady=10)

        # Función para cargar una foto
        def cargar_foto():
            ruta_foto = filedialog.askopenfilename(filetypes=[("Archivos de imagen", ".jpg;.jpeg;.png;.gif")])
            if ruta_foto:
                entry_foto.delete(0, tk.END)  # Limpiar el campo
                entry_foto.insert(0, ruta_foto)  # Mostrar la ruta de la foto
                img = load_image(ruta_foto, (100, 100))
                if img:
                    lbl_imagen.config(image=img)
                    lbl_imagen.image = img  # Mantener una referencia

        # Función para publicar
        def publicar():
            # Obtener los datos del formulario
            nombre = entry_nombre.get()
            foto = entry_foto.get()
            raza = entry_raza.get()
            color = entry_color.get()
            padecimientos = entry_padecimientos.get()
            descripcion = entry_descripcion.get()

            if not all([nombre, foto, raza, color, padecimientos, descripcion]):
                messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
                return
            # Crear una nueva ventana con los datos introducidos
            ventana_publicacion = Toplevel(nueva_ventana_2)
            ventana_publicacion.title("Publicación de Mascota")
            ventana_publicacion.configure(bg='purple')
            ventana_publicacion.geometry("600x400")

            # Mostrar los datos
            tk.Label(ventana_publicacion, text="Nombre: " + nombre, bg='purple', fg='white', font=("Arial", 12)).pack(pady=5)
            tk.Label(ventana_publicacion, text="Foto:", bg='purple', fg='white', font=("Arial", 12)).pack(pady=5)

            # Cargar y mostrar la imagen
            img_publicacion = load_image(foto, (100, 100))
            if img_publicacion:
                lbl_imagen_publicacion = tk.Label(ventana_publicacion, image=img_publicacion, bg='purple')
                lbl_imagen_publicacion.image = img_publicacion
                lbl_imagen_publicacion.pack(pady=5)

            tk.Label(ventana_publicacion, text="Raza: " + raza, bg='purple', fg='white', font=("Arial", 12)).pack(pady=5)
            tk.Label(ventana_publicacion, text="Color: " + color, bg='purple', fg='white', font=("Arial", 12)).pack(pady=5)
            tk.Label(ventana_publicacion, text="Padecimientos: " + padecimientos, bg='purple', fg='white', font=("Arial", 12)).pack(pady=5)
            tk.Label(ventana_publicacion, text="Descripción: " + descripcion, bg='purple', fg='white', font=("Arial", 12), wraplength=500, justify="left").pack(pady=5)

        # Crear los campos del formulario
        tk.Label(nueva_ventana_2, text="Nombre:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_nombre = tk.Entry(nueva_ventana_2, width=50)
        entry_nombre.pack(pady=5)

        tk.Label(nueva_ventana_2, text="Foto:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_foto = tk.Entry(nueva_ventana_2, width=50)
        entry_foto.pack(pady=5)
        btn_cargar_foto = tk.Button(nueva_ventana_2, text="Cargar Foto", command=cargar_foto)
        btn_cargar_foto.pack(pady=5)

        lbl_imagen = tk.Label(nueva_ventana_2, bg="purple")
        lbl_imagen.pack(pady=5)  # Para mostrar la imagen seleccionada

        tk.Label(nueva_ventana_2, text="Raza:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_raza = tk.Entry(nueva_ventana_2, width=50)
        entry_raza.pack(pady=5)

        tk.Label(nueva_ventana_2, text="Color:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_color = tk.Entry(nueva_ventana_2, width=50)
        entry_color.pack(pady=5)

        tk.Label(nueva_ventana_2, text="Padecimientos Médicos:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_padecimientos = tk.Entry(nueva_ventana_2, width=50)
        entry_padecimientos.pack(pady=5)

        tk.Label(nueva_ventana_2, text="Descripción:", bg="purple", fg="white", font=("Arial", 12)).pack(pady=5)
        entry_descripcion = tk.Entry(nueva_ventana_2, width=50)
        entry_descripcion.pack(pady=5)

        btn_publicar = tk.Button(nueva_ventana_2, text="Publicar", command=publicar)
        btn_publicar.pack(pady=10)

        # Botón cerrar ventana crear publicación
        cerrar_boton = Button(nueva_ventana_2, text="Cerrar", command=nueva_ventana_2.destroy)
        cerrar_boton.place(x=1100, y=550)

    # Función para abrir la ventana de mensajes
    def abrir_ventana_mensajes():
        nueva_ventana_3 = Toplevel(menu_principal)
        nueva_ventana_3.title("Mensajes")
        nueva_ventana_3.geometry("1200x600")
        nueva_ventana_3.configure(bg="purple")
        label = Label(nueva_ventana_3, text="Mensajes", bg="purple", fg="white", font=("Arial", 16))
        label.pack(pady=10)

        # Aquí puedes agregar la funcionalidad de mensajes

        # Botón cerrar ventana mensajes
        cerrar_boton = Button(nueva_ventana_3, text="Cerrar", command=nueva_ventana_3.destroy)
        cerrar_boton.place(x=1100, y=550)

    # Función para abrir la ventana de cerrar sesión
    def abrir_ventana_cerrar_sesion():
        nueva_ventana_4 = Toplevel(menu_principal)
        nueva_ventana_4.title("Cerrar Sesión")
        nueva_ventana_4.geometry("1200x600")
        nueva_ventana_4.configure(bg="purple")
        label = Label(nueva_ventana_4, text="¿Seguro que quieres cerrar sesión?", font=("Arial", 16), bg="white", fg="blue")
        label.pack(pady=10)

        # Botón para cerrar sesión
        cerrar_sesion_boton = Button(nueva_ventana_4, text="Cerrar Sesión", command=lambda: [nueva_ventana_4.destroy(), menu_principal.destroy(), ventana_login.deiconify()], font=("Arial", 12), bg="white", fg="blue")
        cerrar_sesion_boton.place(x=550, y=300)

        # Botón para cancelar
        cancelar_boton = Button(nueva_ventana_4, text="Cancelar", command=nueva_ventana_4.destroy, font=("Arial", 12), bg="white", fg="blue")
        cancelar_boton.place(x=550, y=350)

    # Botón para abrir la ventana de perfil
    boton_perfil = ttk.Button(menu_principal, text="Mi Perfil", command=abrir_ventana_perfil)
    boton_perfil.place(x=10, y=200)

    # Botón para crear publicación
    boton_crear_publicacion = ttk.Button(menu_principal, text="Crear Publicación", command=abrir_ventana_crear_publicacion)
    boton_crear_publicacion.place(x=10, y=250)

    # Botón para mensajes
    boton_mensajes = ttk.Button(menu_principal, text="Mensajes", command=abrir_ventana_mensajes)
    boton_mensajes.place(x=10, y=300)

    # Botón para cerrar sesión
    boton_cerrar_sesion = ttk.Button(menu_principal, text="Cerrar Sesión", command=abrir_ventana_cerrar_sesion)
    boton_cerrar_sesion.place(x=10, y=350)

    # Crear los botones de publicaciones nuevas
    create_pet_button(menu_principal, "Luna, Gatita blanca, 6 meses, publicado por: Elena Lopez", "luna.png", 400, 200)
    create_pet_button(menu_principal, "Atlas, Tortuga, 5 años, publicado por: Silvio Rodriguez", "atlas.png", 400, 280)
    create_pet_button(menu_principal, "Paquita, Perro Pekinés, 4 años, publicado por: Francis Wilkerson", "paquita.png", 400, 360)

    # Botón "Salir"
    boton_salir = tk.Button(menu_principal, text="Salir", command=menu_principal.destroy, bg="red", fg="white", font=("Arial", 12))
    boton_salir.place(x=1100, y=550)

    # Botón "Adoptame" que abre la ventana de adopción
    adopt_button = Button(menu_principal, text="Adoptame", font=("Arial", 14), command=lambda: open_adoption_window(menu_principal), bg="green", fg="white")
    adopt_button.place(x=700, y=510)

# Crear la ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("1200x600")
ventana_login.configure(bg="purple")

# Cargar y mostrar una imagen en la ventana de login
imagen_login = load_image("loginfap.png", (250, 100))
if imagen_login:
    label_imagen_login = tk.Label(ventana_login, image=imagen_login)
    label_imagen_login.image = imagen_login  # Evita que la imagen sea eliminada por el recolector de basura
    label_imagen_login.pack(pady=10)

# Etiquetas y campos para usuario y contraseña
label_usuario = tk.Label(ventana_login, text="Usuario:", bg="purple", fg="white", font=("Arial", 12))
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana_login, width=30)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana_login, text="Contraseña:", bg="purple", fg="white", font=("Arial", 12))
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="*", width=30)
entry_contrasena.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_datos, bg="blue", fg="white", font=("Arial", 12))
boton_login.pack(pady=20)

# Iniciar el bucle principal
ventana_login.mainloop()