from app_ingresos_gastos import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar")

@app.route("/delete")
def new():
    return render_template("delete.html",titulo="Borrar")

@app.route("/update")
def new():
    return render_template("update.html", titulo="Actualizar",tipoAccion="Actualización", tipoBoton="Editar")