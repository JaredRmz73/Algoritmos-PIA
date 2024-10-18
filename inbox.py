import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para cargar imágenes (debes instalar pillow)

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mensajes")
        self.root.geometry("600x400")
        self.root.configure(bg="purple")
        
        # Crear el marco para la lista de contactos y los botones
        self.frame_contacts = tk.Frame(self.root, bg="lightgray")
        self.frame_contacts.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Botón "Regresar"
        self.back_button = tk.Button(self.frame_contacts, text="⬅ Regresar", command=self.back_to_inbox)
        self.back_button.pack(pady=5)

        # Lista de contactos
        self.contacts = ["Contacto 1", "Contacto 2", "Contacto 3"]
        self.contact_buttons = []
        for contact in self.contacts:
            button = tk.Button(self.frame_contacts, text=contact, width=20, command=lambda c=contact: self.open_chat(c))
            button.pack(pady=5)
            self.contact_buttons.append(button)

        # Crear el marco para el chat
        self.frame_chat = None

    def back_to_inbox(self):
        if self.frame_chat:
            self.frame_chat.destroy()
        self.frame_contacts.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    def open_chat(self, contact_name):
        # Ocultar la bandeja de entrada
        self.frame_contacts.pack_forget()

        # Crear el marco del chat
        self.frame_chat = tk.Frame(self.root, bg="white")
        self.frame_chat.pack(fill=tk.BOTH, expand=True)

        # Nombre del contacto
        label_name = tk.Label(self.frame_chat, text=contact_name, font=("Arial", 14), bg="white")
        label_name.pack(anchor="nw", padx=10, pady=5)

        # Imagen del contacto (simulación)
        img = Image.open(r'usuario.png')  # Usa tu propia imagen
        img = img.resize((50, 50))
        profile_image = ImageTk.PhotoImage(img)
        label_image = tk.Label(self.frame_chat, image=profile_image, bg="white")
        label_image.image = profile_image  # Necesario para evitar que Python elimine la referencia
        label_image.pack(anchor="nw", padx=10, pady=5)

        # Campo de mensajes
        text_chat = tk.Text(self.frame_chat, height=10, state=tk.DISABLED)
        text_chat.pack(pady=10, padx=10)

        # Campo para escribir mensaje
        entry_message = tk.Entry(self.frame_chat, width=50)
        entry_message.pack(pady=5, padx=10, side=tk.LEFT)

        # Botón para enviar mensaje
        send_button = tk.Button(self.frame_chat, text="Enviar", command=lambda: self.send_message(entry_message, text_chat))
        send_button.pack(pady=5, padx=10, side=tk.LEFT)

        # Botones de opciones
        frame_options = tk.Frame(self.frame_chat, bg="white")
        frame_options.pack(pady=10, padx=10)

        profile_button = tk.Button(frame_options, text="Ver perfil", command=lambda: self.view_profile(contact_name))
        profile_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(frame_options, text="Eliminar chat", command=lambda: self.delete_chat(contact_name))
        delete_button.pack(side=tk.LEFT, padx=5)

        block_button = tk.Button(frame_options, text="Bloquear contacto", command=lambda: self.block_contact(contact_name))
        block_button.pack(side=tk.LEFT, padx=5)

    def send_message(self, entry, text_chat):
        message = entry.get()
        if message:
            text_chat.config(state=tk.NORMAL)
            text_chat.insert(tk.END, "Yo: " + message + "\n")
            text_chat.config(state=tk.DISABLED)
            entry.delete(0, tk.END)

    def view_profile(self, contact_name):
        messagebox.showinfo("Perfil", f"Viendo perfil de {contact_name}")

    def delete_chat(self, contact_name):
        answer = messagebox.askyesno("Eliminar chat", f"¿Estás seguro de eliminar el chat con {contact_name}?")
        if answer:
            messagebox.showinfo("Chat eliminado", f"El chat con {contact_name} ha sido eliminado")

    def block_contact(self, contact_name):
        answer = messagebox.askyesno("Bloquear contacto", f"¿Estás seguro de bloquear a {contact_name}?")
        if answer:
            messagebox.showinfo("Contacto bloqueado", f"Has bloqueado a {contact_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
