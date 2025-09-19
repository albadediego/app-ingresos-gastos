from app_ingresos_gastos import app
from flask import render_template, request, redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #Llamada al archivo csv
    fichero = open('data/movimientos.csv', 'r')
    csvReader = csv.reader(fichero, delimiter=',',quotechar='"')
    for items in csvReader:
            datos.append(items)
    fichero.close()
    return render_template("index.html", data=datos, titulo="Lista")

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        comprobarErrores = validarFormulario(request.form)

        if comprobarErrores:
              return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", errors=comprobarErrores)
        else:
            #Acceder al archivo y configurar para la carga del nuevo registro
            mifichero = open('data/movimientos.csv', 'a',newline="")
            #Llamar al método writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            #Registramos los datos recibidos en el archivo csv
            lectura.writerow([request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()

            #Redireccionar a home o lista de registros
            return redirect("/")
    else:
            return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar")

@app.route("/delete")
def delete():
        return render_template("delete.html", titulo="Borrar")

@app.route("/update")
def update():
        return render_template("update.html", titulo="Actualizar", tipoAccion="Actualizacion", tipoBoton="Editar")


def validarFormulario(datosFormulario):
    errores = [] #Se crea la lista para guardar errores
    hoy = str(date.today())
    if datosFormulario['fecha'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concepto'] == "":
        errores.append("El concepto no puede ir vacío")
    if datosFormulario['monto'] == "" or int(datosFormulario['monto']) == 0:
        errores.append("El monto debe ser distinto de 0 y de vacío")
    return errores