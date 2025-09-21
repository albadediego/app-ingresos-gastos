from app_ingresos_gastos import app, MOVIMIENTOS_FILE, LAST_ID_FILE
from flask import render_template, request, redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    #Llamada al archivo csv
    fichero = open(MOVIMIENTOS_FILE, 'r')
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
            ficheroId = open(LAST_ID_FILE, 'r')
            csvReaderId = csv.reader(ficheroId, delimiter=',', quotechar='"')
            for items in csvReaderId:
                listaId.append(items[0])
            lastId = listaId[-1] #obtenemos el ultimo id registrado
            newId = int(lastId) + 1
            ficheroId.close()
            ######################Guardar el anterior id en last_id.csv#######################################
            fichero_new_id=open(LAST_ID_FILE, 'w')
            fichero_new_id.write(str(newId))
            fichero_new_id.close()

            #######################################################################
            #Acceder al archivo y configurar para la carga del nuevo registro
            mifichero = open(MOVIMIENTOS_FILE, 'a',newline="")
            #Llamar al método writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
            #Registramos los datos recibidos en el archivo csv
            lectura.writerow([newId,request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()

            #Redireccionar a home o lista de registros
            return redirect("/")
    else: #Esto es el GET 
            return render_template("new.html", titulo="Nuevo", tipoAccion="Registro", tipoBoton="Guardar", dataForm={}, urlForm="/new")

@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == 'GET':
        miFicheroDelete = open(MOVIMIENTOS_FILE, 'r')
        lecturaDelete = csv.reader(miFicheroDelete, delimiter=',',quotechar='"')
        registroBuscado = []
        for item in lecturaDelete:
            if item[0] == str(id):
                #encuentro el id buscado de mi registro
                registroBuscado = item
        return render_template("delete.html",titulo="Borrar",data=registroBuscado)
    else: #POST 
         ############Lectura de archivo csv para quitar todos los datos excepto el id#########
        fichero_lectura = open(MOVIMIENTOS_FILE,'r')
        csvReader = csv.reader(fichero_lectura,delimiter=',',quotechar='"')
        registros=[]

        for item in csvReader:
             if item[0] != str(id):
                  registros.append(item)
        fichero_lectura.close()

        ###################Guardar el registro de datos obtenido#############################
        fichero_guardar= open(MOVIMIENTOS_FILE,'w',newline='')
        #llamar al metodo writer de escritura y configuramos el formato
        csvWriter = csv.writer(fichero_guardar,delimiter=',',quotechar='"')
        #registramos los datos recibidos en el archivo csv
        for datos in registros:
             csvWriter.writerow(datos)
        
        fichero_guardar.close()


        return redirect('/')

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if request.method == "POST":
        return f"Se debe actualizar estos datos {request.form}"
    else:
        miFicheroUpdate = open(MOVIMIENTOS_FILE, 'r')
        lecturaUpdate = csv.reader(miFicheroUpdate, delimiter=',', quotechar='"')
        registro_buscado = dict()
        for item in lecturaUpdate:
            if item[0] == str(id):
                registro_buscado['id']=item[0]
                registro_buscado['fecha']=item[1]
                registro_buscado['concepto']=item[2]
                registro_buscado['monto']=item[3]

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