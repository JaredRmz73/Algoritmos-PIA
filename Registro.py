from tkinter import *

def send_data():
    Usuario_data=Usuario.get()
    Contraseña_data =str(Contraseña.get())
    Nombre_data=Nombre.get()
    Edad_data=str(Edad.get())

    print(Usuario_data,"\t",Contraseña_data,"\t",Nombre_data,"\t",Edad_data)
    
    newfile = open("registration.txt","w")
    newfile.write(Usuario_data)
    newfile.write("\t")
    newfile.write(Contraseña_data)
    newfile.write("\t")
    newfile.write(Nombre_data)
    newfile.write("\t")
    newfile.write(Edad_data)
    newfile.write("\n")
    newfile.close()
    
    print("Nuevo Usuario Registrado. Usuario: {} | Nombre {}  ".format(Usuario_data,Nombre_data))

    Usuario_entry.delete(0,END)
    Contraseña_entry.delete(0,END)
    Nombre_entry.delete(0,END)
    Edad_entry.delete(0,END)


mywindow=Tk()
mywindow.geometry("650x550")
mywindow.title("Find-a-Pet:Encuentra un Compañero Peludo Hoy")
mywindow.resizable(False,False)
mywindow.config(background= "purple")
main_title= Label(text="Find-a-Pet  | Registrate",font=("Cambria",13),bg="#56CD63", fg="white", width="550", height="2")
main_title.pack()

Usuario_label = Label(text="Usuario", bg="#FFEEDD")
Usuario_label.place(x=22,y=70)
Contraseña_label = Label(text="Contraseña", bg="#FFEEDD")
Contraseña_label.place(x=22,y=130)
Nombre_label = Label(text="Nombre", bg="#FFEEDD")
Nombre_label.place(x=22,y=190)
Edad_label = Label(text="Edad", bg="#FFEEDD")
Edad_label.place(x=22,y=250)


Usuario = StringVar()
Contraseña = StringVar()
Nombre = StringVar()
Edad = StringVar()

Usuario_entry = Entry(textvariable=Usuario, width="40")
Contraseña_entry = Entry(textvariable=Contraseña, width="40",show="*")
Nombre_entry = Entry(textvariable=Nombre, width="40")
Edad_entry = Entry(textvariable=Edad, width="40")

Usuario_entry.place(x=22,y=100)
Contraseña_entry.place(x=22,y=160)
Nombre_entry.place(x=22,y=220) 
Edad_entry.place(x=22,y=280) 

submit_btn = Button(mywindow,text="Registrarme",command=send_data, width="30",height="2",bg="#00CD63")
submit_btn.place(x=22,y=320)

mywindow.iconbitmap(r"C:\Users\Usuario\Downloads\faplogo.ico")

mywindow.mainloop()