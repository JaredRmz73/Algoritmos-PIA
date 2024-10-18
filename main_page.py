import tkinter as tk
from tkinter import Label, Entry, Button, Toplevel, messagebox
from PIL import Image, ImageTk
# Crear la ventana principal
root = tk.Tk()
root.title("Main Page")
root.geometry("1200x600")
root.configure(bg="purple")

# Agregar logo en forma de patita
def load_image(path, size):
    img = Image.open(path)
    img = img.resize((130,130))
    return ImageTk.PhotoImage(img)

paw_logo = load_image(r'patita.png', (80, 80)) 
logo_label = tk.Label(root, image=paw_logo, bg="purple")
logo_label.place(x=30, y=30)

# Etiqueta con el texto del logo
logo_text = Label(root, text="Find-a-Pet: Encuentra a tu compañero peludo hoy", bg="white", fg="blue", font=("Arial", 14, "bold"))
logo_text.place(x=370, y=15)

# Barra buscadora
search_entry = Entry(root, width=50)
search_entry.insert(0, "¿Qué buscas hoy?")
search_entry.place(x=450, y=80)

# Publicaciones Nuevas
pub_label = Label(root, text="Publicaciones Nuevas", bg="white", fg="blue", font=("Arial", 16))
pub_label.place(x=480, y=130)

# Función para abrir nuevas ventanas
def open_new_window(title):
    new_window = Toplevel(root)
    new_window.title(title)
    new_window.geometry("1200x600")
    new_window.configure(bg="purple")
    label = Label(new_window, text=title, font=("Arial", 18),bg="purple")
    label.pack(pady=20)

# Menú de botones a la izquierda
menu_frame = tk.Frame(root, bg="purple")
menu_frame.place(x=20, y=250)

menu_buttons = [("Mi perfil", "Mi perfil"), ("Crear publicación", "Crear publicación"), 
                ("Mensajes", "Mensajes"), ("Cerrar sesión", "Cerrar sesión")]

for text, title in menu_buttons:
    btn = Button(menu_frame, text=text, width=20, command=lambda t=title: open_new_window(t))
    btn.pack(pady=5)

# Crear botón para cada mascota con imagen y detalles
def create_pet_button(parent, text, image_path, x, y):
    pet_img = load_image(image_path, (50, 50))  # Ajustar tamaño de la imagen
    pet_button = Button(parent, text=text, image=pet_img, compound="left", width=450, height=70)
    pet_button.image = pet_img  # Para evitar que la imagen se borre
    pet_button.place(x=386, y=y)

# Botones de las mascotas
create_pet_button(root, "Luna, Gatita blanca, 6 meses, publicado por: Elena Lopez", r'luna.png', 200, 200)
create_pet_button(root, "Atlas, Tortuga, 5 años, publicado por: Silvio Rodriguez", r'atlas.png', 200, 280)
create_pet_button(root, "Paquita, Perro Pekinés, 4 años, publicado por: Francis Wilkerson", r'paquita.png', 200, 360)

# Iniciar la ventana principal
root.mainloop()
