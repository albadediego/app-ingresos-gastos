from app_ingresos_gastos import MOVIMIENTOS_FILE, LAST_ID_FILE
import csv

def select_all():
    datos=[]
    #Llamada al archivo csv
    fichero = open(MOVIMIENTOS_FILE, 'r')
    csvReader = csv.reader(fichero, delimiter=',',quotechar='"')
    for items in csvReader:
            datos.append(items)
    fichero.close()

    return datos

def select_by(id,condicion):
        miFicheroBuscado = open(MOVIMIENTOS_FILE, 'r')
        lecturaFichero = csv.reader(miFicheroBuscado, delimiter=',',quotechar='"')
        registroBuscado = []
        for item in lecturaFichero:
            if condicion == "==":
                if item[0] == str(id):
                    #encuentro el id buscado de mi registro
                    registroBuscado = item
            elif condicion == "!=":
                if item[0] != str(id):
                  registroBuscado.append(item)
            elif condicion == "dic":
                if item[0] == str(id):
                    registroBuscado = dict()
                    registroBuscado['id']=item[0]
                    registroBuscado['fecha']=item[1]
                    registroBuscado['concepto']=item[2]
                    registroBuscado['monto']=item[3]

        miFicheroBuscado.close()
        
        return registroBuscado

def delete_by(id, registros):
    fichero_guardar= open(MOVIMIENTOS_FILE,'w',newline='')
    #llamar al metodo writer de escritura y configuramos el formato
    csvWriter = csv.writer(fichero_guardar,delimiter=',',quotechar='"')
    #registramos los datos recibidos en el archivo csv
    for datos in registros:
        csvWriter.writerow(datos)
    
    fichero_guardar.close()

def insert(requestForm):
    #######################Generar el nuevo id para registro###################################
    listaId = []
    lastId = ""
    newId = 0
    ficheroId = open(LAST_ID_FILE, 'r')
    csvReaderId = csv.reader(ficheroId, delimiter=',', quotechar='"')
    for items in csvReaderId:
        listaId.append(items[0])
    if listaId == []:
        newId = 1
    else:    
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
    lectura.writerow([newId,requestForm['fecha'],requestForm['concepto'],requestForm['monto']])
    mifichero.close()

def update_by(id, registros, requestForm):
    nuevosDatos = []
    for item in registros:
        if item[0] == str(id):
            nuevosDatos.append([id, requestForm['fecha'], requestForm['concepto'], requestForm['monto'] ])
        else:
            nuevosDatos.append(item)

    fichero_update= open(MOVIMIENTOS_FILE,'w',newline='')
    #llamar al metodo writer de escritura y configuramos el formato
    csvWriter = csv.writer(fichero_update,delimiter=',',quotechar='"')
    #registramos los datos recibidos en el archivo csv
    csvWriter.writerows(nuevosDatos)
    
    fichero_update.close()