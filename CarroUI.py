from tkinter import *
import datetime
from CarroDAO import CarroDAO
from CarroBAL import CarroBAL


class CarroUI():
    window = Tk()
    window.wm_title("Python PROJECT CRUD - Carro")

    txtMarca = StringVar()
    txtAno = StringVar()
    txtValor = StringVar()
    txtFoto = StringVar()

    lblMarca = Label(window, text="Marca")
    lblAno = Label(window, text="Ano")
    lblValor = Label(window, text="Valor")
    lblFoto = Label(window, text="Foto")

    space1 = Label(window, text="")
    space2 = Label(window, text="")

    entMarca = Entry(window, textvariable=txtMarca)
    entAno = Entry(window, textvariable=txtAno)
    entValor = Entry(window, textvariable=txtValor)
    entFoto = Entry(window, textvariable=txtFoto)

    btnViewAll = Button(window, text="Listar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Editar")
    btnDel = Button(window, text="Deletar")
    btnClose = Button(window, text="Fechar")

    lblMarca.grid(row=1, column=0)
    lblAno.grid(row=2, column=0)
    lblValor.grid(row=3, column=0)
    lblFoto.grid(row=4, column=0)

    space1.grid(row=0, column=2)
    space2.grid(row=0, column=10)

    entMarca.grid(row=1, column=1, padx=50, pady=50)
    entAno.grid(row=2, column=1)
    entValor.grid(row=3, column=1)
    entFoto.grid(row=4, column=1)

    btnViewAll.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    listClientes = Listbox(window,font=("Helvetica", 20))

    scrollClientes = Scrollbar(window)

    listClientes.grid(row=1, column=3, rowspan=10, ipadx=255)

    scrollClientes.grid(row=1, column=7, rowspan=10)

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    x_pad = 15
    y_pad = 5
    width_entry = 30

    for child in window.winfo_children():
        widget_class = child.__class__.__name__

        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)

        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')

        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')

        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')


f = CarroDAO()
app = CarroUI()


class Application():
    def view_command(self):
        rows = f.listar()

        app.listClientes.delete(0, END)

        for r in rows:
            app.listClientes.insert(END, r)

    def insert_command(self):
        f.inserir(app.txtMarca.get(), app.txtAno.get(), app.txtValor.get(), app.txtFoto.get())
        self.view_command()

    def update_command(self):
        id = selected[0]
        f.editar(id, app.txtMarca.get(), app.txtAno.get(), app.txtValor.get(), app.txtFoto.get())
        self.view_command()

    def del_command(self):
        id = selected[0]
        f.excluir(id)
        self.view_command()

    def getSelectedRow(self):
        global selected

        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)

        app.entMarca.delete(0, END)
        app.entMarca.insert(END, selected[1])

        app.entAno.delete(0, END)
        app.entAno.insert(END, selected[2])

        app.entValor.delete(0, END)
        app.entValor.insert(END, selected[3])

        app.entFoto.delete(0, END)
        app.entFoto.insert(END, selected[4])

    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)


