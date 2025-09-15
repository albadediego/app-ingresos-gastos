from app_ingresos_gastos import app

@app.route("/")
def hello_world():
    return "Hola, esto es la kata de flask"