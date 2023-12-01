from datetime import date
from tkinter import ttk
import tkinter as tkinter
from tkinter import messagebox
import tkinter

def OpcionAgregar():
    descripcion = Entrada.get()
    treeview.insert(
    "",
    tkinter.END, text=descripcion, values=(date.today().strftime("%d-%m-%y"), False))

def OpcionCompletar():
    try:
        item = treeview.selection()[0]
    except IndexError:
        messagebox.showwarning(
            message="Debe seleccionar un elemento.",
            title="No hay selección"
        )
    else:
        text = treeview.item(item, option="text")
        treeview.item(item,values=(date.today().strftime("%d-%m-%y"),True))
        messagebox.showinfo(message=text, title="Se completo la tarea:")        
       
def OpcionBorrar():
    try:
        item = treeview.selection()[0]
    except IndexError:
        messagebox.showwarning(
            message="Debe seleccionar un elemento.",
            title="No hay selección"
        )
    else:
        aviso = messagebox.askyesno(message="¿Queres borrar?")
        if aviso==True:
            treeview.delete(item)
        else: None

def salir():
    aviso = messagebox.askyesno(message="¿Queres salir?")
    if aviso==True:
        root.destroy()
    else: None

root = tkinter.Tk()
root.title("Lista de Tareas")
root.geometry("720x600")

treeview = ttk.Treeview(columns= ("Fecha", "Estado", ))
treeview.heading("#0", text="Descripcion")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Estado", text="Estado")

Entrada = tkinter.Entry(root)

boton_agregar = tkinter.Button(root, text="Agregar tarea", bg="cyan", width=15, command=OpcionAgregar)
boton_borrar = tkinter.Button(root, text="Eliminar tarea", bg="red", width=15, command=OpcionBorrar)
boton_completar = tkinter.Button(root, text="Completar tarea", bg="green", width=15,command=OpcionCompletar)
boton_salir = tkinter.Button(root, text="Salir", bg="blue", width=15,command=salir)

treeview.pack()
Entrada.pack()
boton_agregar.pack(pady=8)
boton_completar.pack(pady=8)
boton_borrar.pack(pady=8)
boton_salir.pack(pady=8)

root.mainloop()
