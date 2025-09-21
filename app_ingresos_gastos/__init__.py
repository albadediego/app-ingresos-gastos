from flask import Flask

app = Flask(__name__)

MOVIMIENTOS_FILE = 'data/movimientos.csv'
LAST_ID_FILE = 'data/last_id.csv'

from app_ingresos_gastos.routes import *

#set FLASK_APP=main.py
#flask --app main --debug run
