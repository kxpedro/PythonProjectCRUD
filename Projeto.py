from CarroUI import Application
from CarroUI import CarroUI


app = CarroUI()
dao = Application()

app.btnViewAll.configure(command=dao.view_command)
app.btnInserir.configure(command=dao.insert_command)
app.btnUpdate.configure(command=dao.update_command)
app.btnDel.configure(command=dao.del_command)
app.btnClose.configure(command=app.window.destroy)

app.window.minsize(width=1120, height=400)
app.window.mainloop()
