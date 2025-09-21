from app_ingresos_gastos import app, MOVIMIENTOS_FILE, LAST_ID_FILE
from flask import render_template, request, redirect
import csv
from datetime import date
from app_ingresos_gastos.models import *

@app.route("/")
def index():
    datos = select_all()
    totales = total_view()
    return render_template("index.html", data=datos, titulo="Lista", total=totales)

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST": #Esto es el POST 
        comprobarErrores = validarFormulario(request.form)

        if comprobarErrores:
              return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", errors=comprobarErrores, dataForm=request.form)
        else:
            insert(request.form)

            #Redireccionar a home o lista de registros
            return redirect("/")
    else: #Esto es el GET 
            return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", dataForm={}, urlForm="/new")

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == 'GET':
        registroBuscado = select_by(id,"==")
     
        return render_template("delete.html",titulo="Borrar",data=registroBuscado)
    else: #POST 
         ############Lectura de archivo csv para quitar todos los datos excepto el id#########
        registros=select_by(id,"!=")

        ###################Guardar el registro de datos obtenido#############################
        delete_by(id,registros)
        return redirect('/')

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if request.method == "POST":
        comprobarErrores = validarFormulario(request.form)

        if comprobarErrores:
            return render_template("update.html", titulo="Actualizar", tipoAccion="Actualizacion", tipoBoton="Editar", dataForm=request.form, errors=comprobarErrores)
        
        update_by(id, select_all(), request.form)
        return redirect("/")
    else:
        registro_buscado=select_by(id,"dic")

        return render_template("update.html", titulo="Actualizar", tipoAccion="Actualizacion", tipoBoton="Editar", dataForm=registro_buscado)


def validarFormulario(datosFormulario):
    errores = [] #Se crea la lista para guardar errores
    hoy = str(date.today())
    if datosFormulario['fecha'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concepto'] == "":
        errores.append("El concepto no puede ir vacío")
    if datosFormulario['monto'] == "" or float(datosFormulario['monto']) == 0.0:
        errores.append("El monto debe ser distinto de 0 y de vacío")
    return errores