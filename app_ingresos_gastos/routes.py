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
    if request.method == "POST": #Esto es el POST 
        comprobarErrores = validarFormulario(request.form)

        if comprobarErrores:
              return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", errors=comprobarErrores, dataForm=request.form)
        else:
            #######################Generar el nuevo id para registro###################################
            listaId = []
            lastId = ""
            newId = 0
            ficheroId = open('data/last_id.csv', 'r')
            csvReaderId = csv.reader(ficheroId, delimiter=',', quotechar='"')
            for items in csvReaderId:
                listaId.append(items[0])
            lastId = listaId[-1] #obtenemos el ultimo id registrado
            newId = int(lastId) + 1
            ficheroId.close()
            ######################Guardar el anterior id en last_id.csv#######################################
            fichero_new_id=open('data/last_id.csv', 'w')
            fichero_new_id.write(str(newId))
            fichero_new_id.close()

            #######################################################################
            #Acceder al archivo y configurar para la carga del nuevo registro
            mifichero = open('data/movimientos.csv', 'a',newline="")
            #Llamar al método writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            #Registramos los datos recibidos en el archivo csv
            lectura.writerow([newId,request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()

            #Redireccionar a home o lista de registros
            return redirect("/")
    else: #Esto es el GET 
            return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", dataForm={})

@app.route("/delete/<int:id>")
def delete(id):
     return f"El registro para eliminar es el id: {id}"
    #return render_template("delete.html", titulo="Borrar")

@app.route("/update/<int:id>")
def update(id):
    return f"El registro para actualizar es el id: {id}"
    #return render_template("update.html", titulo="Actualizar", tipoAccion="Actualizacion", tipoBoton="Editar", dataForm={})


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