import sqlite3
from sqlite3 import Error


def conectar():
    try:
        con = sqlite3.connect("labase.db")
        return con
    except Error:

        print(Error)
    return 0


def creartabla():

    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists clientes(dni integer PRIMARY KEY, titulo, descripcion)"
    )
    con.commit()
    return 0


con = conectar()
