import tkinter as tk
from tkinter import messagebox

def registrar():
    
    mensaje = f"Nombre: {xnombre.get()}\nApellido: {xapellido.get()}\nEdad: {xedad.get()}\nDirección: {xdireccion.get()}\nSexo: {seleccione_genero.get()}\nTeléfono: {xtelefono.get()}\nCiudad: {seleccionar_ciudad.get()}"
    messagebox.showinfo("Informacion Registrada", mensaje)
    
ventana = tk.Tk()
    
ventana.title("Fabian APP")
    
ventana.geometry("800x600")
    
ventana.resizable(True,True)
    
lnombre=tk.Label(ventana,text="Nombre:")
lnombre.grid(row=0,column=0, pady= 4)
xnombre=tk.Entry(ventana,width=30)
xnombre.grid(row= 0, column=1, pady=4)
    
lapellido=tk.Label(ventana,text="Apellido:" )
lapellido.grid(row = 1, column = 0, pady = 4)
xapellido=tk.Entry(ventana, width=30)
xapellido.grid(row = 1, column = 1, pady = 4)

ledad=tk.Label(ventana,text="Edad:" )
ledad.grid(row = 2, column = 0, pady = 4)
xedad=tk.Entry(ventana, width=30)
xedad.grid(row = 2, column = 1, pady = 4)

ldireccion=tk.Label(ventana,text="Direccion:")
ldireccion.grid(row = 3, column= 0, pady= 4)
xdireccion=tk.Entry(ventana, width=30)
xdireccion.grid(row = 3, column = 1, pady = 4)

ltelefono=tk.Label(ventana,text="Telefono:")
ltelefono.grid(row=4, column=0, pady=4)
xtelefono=tk.Entry(ventana, width=30)
xtelefono.grid(row=4, column=1, pady=4) 

seleccione_genero=tk.Label(ventana,text="Sexo:")
seleccione_genero.grid(row = 5, column= 0, pady= 4)
seleccione_genero = tk.StringVar()

tk.Radiobutton(ventana, text="Masculino", variable=seleccione_genero, value="Masculino").grid(row=5, column=1, pady=4)
tk.Radiobutton(ventana, text="Femenino", variable=seleccione_genero, value="Femenino").grid(row=5, column=2, pady=4)

xciudad=tk.Label(ventana,text="Ciudad:")
xciudad.grid(row=6, column=0, pady=4)

seleccionar_ciudad = tk.StringVar()
ciudades = ["Barranquilla", "Medellin","Cucuta", "Cartagena","Monteria"]


ciudad_list= tk.Listbox(ventana,height=5)
ciudad_list.grid(row=6, column=1, pady=4)
for ciudad in ciudades:
    ciudad_list.insert(tk.END, ciudad)
    
def on_select(event):
    seleccionar_ciudad.set(event.widget.get(event.widget.curselection()))

ciudad_list.bind('<<ListboxSelect>>', on_select)    
    
Registrar = tk.Button(ventana, text="Registrar", command=registrar,bg="light blue")
Registrar.grid(row = 8, column=2, pady=4)


ventana.mainloop()
    

