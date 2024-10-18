import tkinter as tk
from tkinter import messagebox,Entry,Label, Button, Toplevel,ttk,filedialog
from PIL import Image, ImageTk  # Importa Pillow para cargar imágenes en otros formatos

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
    menu_principal = tk.Toplevel()  # Crea una nueva ventana
    menu_principal.title("Menú Principal")
    menu_principal.geometry("1200x600")
    menu_principal.configure(bg="purple")
    
    # Cargar y mostrar la imagen en el menú principal

    

    
    search_entry = Entry(menu_principal, width=50)
    search_entry.insert(0, "¿Qué buscas hoy?")
    search_entry.place(x=450, y=80)
    
    label_bienvenida = tk.Label(menu_principal, text="Bienvenido al Menú Principal")
    label_bienvenida.pack(pady=10)

    pub_label = Label(menu_principal, text="Publicaciones Nuevas", bg="white", fg="blue", font=("Arial", 16))
    pub_label.place(x=480, y=130)

    def abrir_ventana():
    
        nueva_ventana = tk.Toplevel(menu_principal)
        nueva_ventana.title("Nueva Ventana")
        nueva_ventana.geometry("1200x600")
        nueva_ventana.configure(bg="purple")
        label = tk.Label(nueva_ventana, text="Mi Perfil",bg="white",fg="blue",font=("arial",12))
        label.pack(pady=20)
        cerrar_boton = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
        cerrar_boton.pack(pady=5)
        cerrar_boton.place(x=200,y=550)



        perfil_texto = "Nombre: Jared Ramírez\nCorreo: jaredrmz@geemail.com\nUbicación: Mangos 23, Colonia Prismacolor, Monterrey, Nuevo León\nEdad: 26 Años"
        perfil_label = tk.Label(nueva_ventana, text=perfil_texto, font=("Arial", 12), fg="blue", bg="white")
        perfil_label.pack(pady=10)

    
             
        
           




        def create_pet_button(parent, text, image_path, x, y):
           
            pet_button = Button(parent, text=text, compound="left", width=265, height=70)
            
            pet_button.place(x=400, y=y)
        create_pet_button(nueva_ventana, "Sorullo, Gato negro, 6 meses", r'gato.png', 200, 220)
        create_pet_button(nueva_ventana, "Esteban, Hamster, 2 meses", r'hamster.png', 200, 300) 
        create_pet_button(nueva_ventana, "Roberta, Perro Escocés, 4 años", r'perro.png', 200, 380)  
        perfil_2_texto = "Mis Publicaciones"
        perfil_2_label = tk.Label(nueva_ventana, text=perfil_2_texto, font=("Arial", 10), fg="blue", bg="white")
        perfil_2_label.pack(pady=20)
        perfil_2_label.config(x=400,y=250) 
 
    boton_abrir = ttk.Button(menu_principal, text="Mi Perfil", command=abrir_ventana)  
    boton_abrir.pack(pady=20)  
    boton_abrir.place(x=10,y=200)

    def abrir_ventana_2():
        
        nueva_ventana_2 = tk.Toplevel(menu_principal)
        nueva_ventana_2.title("Nueva Ventana")
        nueva_ventana_2.geometry("1200x600")
        nueva_ventana_2.configure(bg="purple")
        label = tk.Label(nueva_ventana_2, text="Crear Publicación")
        label.pack(pady=10)
        cerrar_boton = tk.Button(nueva_ventana_2, text="Cerrar", command=nueva_ventana_2.destroy)
        cerrar_boton.pack(pady=5)
        cerrar_boton.place(x=200,y=550)
        def cargar_foto():
            ruta_foto = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
            if ruta_foto:
                entry_foto.delete(0, tk.END)  # Limpiar el campo
                entry_foto.insert(0, ruta_foto)  # Mostrar la ruta de la foto
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

            if not all([nombre, foto, raza, color, padecimientos, descripcion]):
                messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")        
                return
            # Crear una nueva ventana con los datos introducidos
            ventana_publicacion = tk.Toplevel()
            ventana_publicacion.title("Publicación de Mascota")
            ventana_publicacion.configure(bg='purple')

            tk.Label(ventana_publicacion, text="Nombre: " + nombre, bg='purple', fg='white').pack(pady=5)
            tk.Label(ventana_publicacion, text="Foto: ", bg='purple', fg='white').pack(pady=5)

            # Cargar y mostrar la imagen

            tk.Label(ventana_publicacion, text="Raza: " + raza, bg='purple', fg='white').pack(pady=5)
            tk.Label(ventana_publicacion, text="Color: " + color, bg='purple', fg='white').pack(pady=5)
            tk.Label(ventana_publicacion, text="Padecimientos: " + padecimientos, bg='purple', fg='white').pack(pady=5)
            tk.Label(ventana_publicacion, text="Descripción: " + descripcion, bg='purple', fg='white').pack(pady=5)
        # Crear la ventana principal
        
        
        
        
        # Crear los campos del formulario
        tk.Label(nueva_ventana_2, text="Nombre:").pack()
        entry_nombre = tk.Entry(nueva_ventana_2)
        entry_nombre.pack()

        tk.Label(nueva_ventana_2, text="Foto:").pack()
        entry_foto = tk.Entry(nueva_ventana_2)
        entry_foto.pack()
        btn_cargar_foto = tk.Button(nueva_ventana_2, text="Cargar Foto", command=cargar_foto)  
        btn_cargar_foto.pack()

        lbl_imagen = tk.Label(nueva_ventana_2)
        lbl_imagen.pack(pady=5)  # Para mostrar la imagen seleccionada

        tk.Label(nueva_ventana_2, text="Raza:").pack()
        entry_raza = tk.Entry(nueva_ventana_2)
        entry_raza.pack()

        tk.Label(nueva_ventana_2, text="Color:").pack()
        entry_color = tk.Entry(nueva_ventana_2)
        entry_color.pack()

        tk.Label(nueva_ventana_2, text="Padecimientos Médicos:").pack()
        entry_padecimientos = tk.Entry(nueva_ventana_2)
        entry_padecimientos.pack()

        tk.Label(nueva_ventana_2, text="Descripción:").pack()
        entry_descripcion = tk.Entry(nueva_ventana_2)
        entry_descripcion.pack()

        btn_publicar = tk.Button(nueva_ventana_2, text="Publicar", command=publicar)
        btn_publicar.pack(pady=10)









    boton_abrir = ttk.Button(menu_principal, text="Crear Publicación", command=abrir_ventana_2)
    boton_abrir.pack(pady=20)  
    boton_abrir.place(x=10,y=250)   
        
    def abrir_ventana_3():
        
        nueva_ventana_3 = tk.Toplevel(menu_principal)
        nueva_ventana_3.title("Nueva Ventana")
        nueva_ventana_3.geometry("1200x600")
        nueva_ventana_3.configure(bg="purple")
        label = tk.Label(nueva_ventana_3, text="Mensajes")
        label.pack(pady=10)

        label2 = tk.Label(nueva_ventana_3, text="No hay mensajes nuevos", font=("arial",14),fg="blue")
        label2.pack(pady=10)



        cerrar_boton = tk.Button(nueva_ventana_3, text="Cerrar", command=nueva_ventana_3.destroy)
        cerrar_boton.pack(pady=5)     

    boton_abrir = ttk.Button(menu_principal, text="Mensajes", command=abrir_ventana_3)
    boton_abrir.pack(pady=20)  
    boton_abrir.place(x=10,y=300)        
       
        
    def abrir_ventana_4():
        
        nueva_ventana_4 = tk.Toplevel(menu_principal)
        nueva_ventana_4.title("Nueva Ventana")
        nueva_ventana_4.geometry("1200x600")
        nueva_ventana_4.configure(bg="purple")
        label = tk.Label(nueva_ventana_4, text="¿Seguro que quieres cerrar sesión?",font=("Arial",16),bg="white",fg="blue")
        label.pack(pady=10)
        cerrar_boton = tk.Button(nueva_ventana_4, text="Cerrar Sesión", command=menu_principal.withdraw,font=("arial",12),bg="white",fg="blue")
        cerrar_boton.pack(pady=5) 
        cancelar_boton = Button(nueva_ventana_4, text="Cancelar", command=nueva_ventana_4.destroy, font=("Arial", 12), bg="white", fg="blue")
        cancelar_boton.place(x=570, y=350)  
        
             

        
                



    boton_abrir = ttk.Button(menu_principal, text="Cerrar Sesión", command=abrir_ventana_4)
    boton_abrir.pack(pady=20)  
    boton_abrir.place(x=10,y=350)     


    

        
       

    
    def create_pet_button(parent, text, image_path, x, y):
        
        pet_button = Button(parent, text=text, compound="left", width=450, height=70)
        
        pet_button.place(x=386, y=y)
    create_pet_button(menu_principal, "Luna, Gatita blanca, 6 meses, publicado por: Elena Lopez", r'luna.png', 200, 200)
    create_pet_button(menu_principal, "Atlas, Tortuga, 5 años, publicado por: Silvio Rodriguez", r'atlas.png', 200, 280)
    create_pet_button(menu_principal, "Paquita, Perro Pekinés, 4 años, publicado por: Francis Wilkerson", r'paquita.png', 200, 360) 
       
        
           



    boton_salir = tk.Button(menu_principal, text="Salir", command=menu_principal.destroy)
    boton_salir.pack(pady=10)
    boton_salir.place(x=1100,y=550)

# Crear la ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("1200x600")
ventana_login.configure(bg="purple")

# Cargar y mostrar una imagen en la ventana de login




# Etiquetas y campos para usuario y contraseña
label_usuario = tk.Label(ventana_login, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="*")  # Muestra los caracteres como ""
entry_contrasena.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_datos)
boton_login.pack(pady=20)

# Iniciar el bucle principal
ventana_login.mainloop()