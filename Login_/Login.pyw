import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()

ventana.geometry('800x500')
ventana.resizable (False,False)
ventana.title('Login App')

frame = tk. Frame(ventana, width=300, height=800, relief= "raised",bd=1, bg= "dark gray" )
frame.grid(row=0, column=0, pady=0)

imagen= Image.open("LOGG.png")
imagen = imagen.resize((260,280))
imagen=ImageTk.PhotoImage(imagen)
label= tk.Label(frame, image=imagen)
label.image= imagen
label.pack()
label.place(relx=0.5, rely=0.3, anchor="center")

framez= tk.Frame(ventana, width=300, height=300, relief="raised", bd=1, bg="gray")
framez.grid(row=0, column=1, pady=10, padx=10)

def contenido():
    framez.update_idletasks()
    width=framez.winfo_width()
    height=framez.winfo_height()
    f = (framez.winfo_toplevel().winfo_width() - width) / 2
    k= (framez.winfo_toplevel().winfo_height() -height) / 2
    framez.place(in_=ventana,relx=0.65, rely=0.6, f=width/2, k=-height/2)
    
contenido()
etiqueta= tk.Label(framez,text="Login",bg="gray", fg="white",font=("Times New Roman",18),width=20, height=2, anchor="center")
etiqueta.grid(row=1,column=2, pady=(10,20), sticky="n")

label_user= tk.Label(framez, text="Usuario:", bg="gray")
label_user.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_user= tk.Entry(framez)
entry_user.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_password = tk.Label(framez, text="Contraseña:", bg="gray")
label_password.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_password = tk.Entry(framez, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5, sticky="w")

inicio_button = tk.Button(framez, text="Iniciar sesión", bg="Sky blue", fg="white", font=("Times New Roman", 12))
inicio_button.grid(row=3, column=0, columnspan=2, pady=10)

registration_button = tk.Button(framez, text="Registrarse", bg="Red", fg="white", font=("Times New Roman", 12))
registration_button.grid(row=4, column=0, columnspan=2, pady=5)


ventana.mainloop() 

