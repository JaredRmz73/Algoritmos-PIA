from tkinter import *
from PIL import ImageTk, Image
def send_data():
    Usuario_data=Usuario.get()
    Contraseña_data =str(Contraseña.get())
   

    print(Usuario_data,"\t",Contraseña_data,"\t")
    
    newfile = open("Login.txt","w")
    newfile.write(Usuario_data)
    newfile.write("\t")
    newfile.write(Contraseña_data)
    newfile.write("\t")

    
    print("Credenciales correctas. Usuario: {} | Contraseña {}  ".format(Usuario_data,Contraseña_data))

    Usuario_entry.delete(0,END)
    Contraseña_entry.delete(0,END)
    


mywindow=Tk()
mywindow.geometry("650x550")
mywindow.title("Find-a-Pet:Encuentra un Compañero Peludo Hoy")
mywindow.resizable(False,False)
mywindow.config(background= "#213141")
main_title= Label(text="Find-a-Pet  | Inicio de Sesión",font=("Cambria",13),bg="#56CD63", fg="white", width="550", height="2")
main_title.pack()

Usuario_label = Label(text="Usuario", bg="#FFEEDD")
Usuario_label.place(x=300,y=70)
Contraseña_label = Label(text="Contraseña", bg="#FFEEDD")
Contraseña_label.place(x=292,y=130)


Usuario = StringVar()
Contraseña = StringVar()


Usuario_entry = Entry(textvariable=Usuario, width="40")
Contraseña_entry = Entry(textvariable=Contraseña, width="40",show="*")


Usuario_entry.place(x=200,y=100)
Contraseña_entry.place(x=200,y=160)


submit_btn = Button(mywindow,text="Iniciar Sesión",command=send_data, width="30",height="2",bg="#00CD63")
submit_btn.place(x=210,y=210)

texto1 =Label(text="¿No tienes una cuenta? Regístrate hoy",font=("Cambria",8), fg="blue")
texto1.pack()

texto1.place(x=232,y=255)

texto2 =Label(text="¿No recuerdas tu contraseña?",font=("Cambria",8), fg="blue")
texto2.pack()

texto2.place(x=248,y=185)
mywindow.iconbitmap(r"C:\Users\Usuario\Downloads\faplogo.ico")


mascotas = ImageTk.PhotoImage(Image.open(r'loginfap.png').resize((650,299)))
label2 = Label(image=mascotas)
label2.pack()
label2.place(x=-5,y=280)

new_window= Toplevel()

mywindow.mainloop()