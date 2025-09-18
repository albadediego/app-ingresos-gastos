from app_ingresos_gastos import app
from flask import render_template


@app.route("/")
def index():
    datos=[
        {'fecha': '01/09/2025', 'concepto': 'Salario', 'monto': '1500'},
        {'fecha': '05/09/2025', 'concepto': 'Ropa', 'monto': '-150'},
        {'fecha': '10/09/2025', 'concepto': 'Supermercado', 'monto': '-200'}
    ]
    return render_template("index.html", data=datos, titulo="Lista")

@app.route("/new")
def new():
        return render_template("new.html", titulo="Nuevo")

@app.route("/delete")
def delete():
        return render_template("delete.html", titulo="Borrar")

@app.route("/update")
def update():
        return render_template("update.html", titulo="Actualizar")