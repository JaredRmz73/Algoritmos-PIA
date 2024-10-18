import tkinter as tk
from tkinter import messagebox, Label, Tk
from PIL import Image, ImageTk





# Función para verificar los datos y mostrar el menú principal
def verificar_datos():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Aquí puedes agregar una verificación más compleja (por ejemplo, revisar una base de datos)
    if usuario == "admin" and contrasena == "1234":
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

    



    label_bienvenida = tk.Label(menu_principal, text="Find-a-Pet: Encuentra a tu compañero peludo hoy")
    label_bienvenida.pack(pady=20)

    image = Image.open(r'loginfap.png')
    image = image.resize((180, 260))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(menu_principal, image=photo, bg="#800080")
    image_label.place(x=100, y=200)




    
    boton_salir = tk.Button(menu_principal, text="Salir", command=menu_principal.destroy)
    boton_salir.pack(pady=20)

    

# Crear la ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("1200x600")
ventana_login.configure(bg="purple")

# Etiquetas y campos para usuario y contraseña
label_usuario = tk.Label(ventana_login, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana_login, text="Contraseña:")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="")  # Muestra los caracteres como ""
entry_contrasena.pack(pady=5)

# Botón para iniciar sesión
boton_login = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_datos)
boton_login.pack(pady=20)

# Iniciar el bucle principal

ventana_login.mainloop()