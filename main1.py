from tkinter import *
from tkinter import messagebox as MessageBox
import sqlite3
from sqlite3 import Error
import modulo1
import modulo2

modulo1.conectar()
modulo1.creartabla()

root = Tk()
root.geometry("500x220")
root.title("CRITICA DE LA PELICULA")
rojo = Frame(root, width=450, height=25, pady=3).grid(row=0, columnspan=3)

datos = Label(rojo, text="Ingrese los datos", foreground="black").grid(row=0, column=1)
# labels de entrada
dni = Label(root, text="DNI").grid(row=1, column=0, sticky=W)
dni = StringVar()
titulo = Label(root, text="Titulo").grid(row=2, column=0, sticky=W)
titulo = StringVar()
descripcion = Label(root, text="Descripcion").grid(row=3, column=0, sticky=W)
descripcion = StringVar()
mostrar = Label(root, text="Datos a mostrar").grid(row=4, column=0, sticky=W)
mostrar = StringVar()
listbox = Listbox(root, height=6, width=25)
listbox.grid(row=4, column=1, rowspan=1, columnspan=1)
lista = []


def error():
    MessageBox.showwarning("ERROR", "El campo titulo solo admite alfanumericos")


def ok():
    MessageBox.showinfo("ALTA", "Se dio de alta correctamente")


def dele():
    MessageBox.showinfo("ALTA", "Se dio de baja correctamente")


def alta():
    entrada = {}
    entrada["dni"] = entrada1.get()
    entrada["titulo"] = entrada2.get()
    entrada["descripcion"] = entrada3.get()

    if modulo2.valida(entrada["titulo"]):
        error()
        entrada["titulo"].delete(0, END)

    else:

        cursorObj = modulo1.con.cursor()
        cursorObj.execute(
            "INSERT INTO clientes VALUES(?,?,?)",
            (entrada1.get(), entrada2.get(), entrada3.get()),
        )

        modulo1.con.commit()
        ok()
        entrada1.delete(0, END)
        entrada2.delete(0, END)
        entrada3.delete(0, END)
        return 0
    return 0


def baja():
    cursorObj = modulo1.con.cursor()

    cursorObj.execute("DELETE from clientes where dni =(?)", (entrada1.get(),))
    dele()
    modulo1.con.commit()
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    return 0


def buscar():
    listbox.delete(0, END)
    cursorObj = modulo1.con.cursor()
    cursorObj.execute("SELECT * FROM clientes where dni = (?)", (entrada1.get(),))
    records = cursorObj.fetchone()
    listbox.insert(
        0, "dni:", records[0], "titulo: ", records[1], "descripcion: ", records[2]
    )
    modulo1.con.commit()
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    return 0


def modificar():
    cursorObj = modulo1.con.cursor()
    cursorObj.execute(
        "UPDATE clientes SET titulo =(?), descripcion =(?) where dni =(?)",
        (entrada2.get(), entrada3.get(), entrada1.get()),
    )
    modulo1.con.commit()
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada3.delete(0, END)
    return 0


def valor(valor, ancho, fila, columna):
    valor = Entry(root, width=ancho)
    valor.grid(row=fila, column=columna)
    return valor


# BOTONES

b = Button(
    root,
    text="Nueva Critica",
    command=alta,
    anchor=CENTER,
    justify=CENTER,
    padx=0,
    height=1,
    width=15,
).grid(row=1, column=2)
m = Button(
    root,
    text="Modificar critica",
    command=modificar,
    anchor=CENTER,
    justify=CENTER,
    padx=0,
    height=1,
    width=15,
).grid(row=2, column=2)
d = Button(
    root,
    text="Dar de baja la critica",
    command=baja,
    anchor=CENTER,
    justify=CENTER,
    padx=0,
    height=1,
    width=15,
).grid(row=3, column=2)
s = Button(
    root,
    text="Buscar critica",
    command=buscar,
    anchor=CENTER,
    justify=CENTER,
    padx=0,
    height=1,
    width=15,
).grid(row=4, column=2)

entrada1 = valor("entrada1", 25, 1, 1)
entrada2 = valor("entrada2", 25, 2, 1)
entrada3 = valor("entrada3", 25, 3, 1)

mainloop()