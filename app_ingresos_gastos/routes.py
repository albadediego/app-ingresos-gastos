from app_ingresos_gastos import app
from flask import render_template
import csv

@app.route("/")
def index():
    datos = []
    #Llamada al archivo csv
    fichero = open('data/movimientos.csv', 'r')
    csvReader = csv.reader(fichero, delimiter=',', quotechar='"')
    for items in csvReader:
        datos.append(items)
        
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar")
'''
@app.route("/delete")
def new():
    return render_template("delete.html",titulo="Borrar")

@app.route("/update")
def new():
    return render_template("update.html", titulo="Actualizar",tipoAccion="Actualización", tipoBoton="Editar")
'''