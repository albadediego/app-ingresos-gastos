# Aplicación web flask

Programa hecho en python con el framework flask, app web

## Instalación
- Crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```

La librería utilizada en flask: https://flask.palletsprojects.com/es/stable/quickstart

# Ejecución del programa
- Inicializar parámetros para el servidor de Flask
- Windows: 
```
set FLASK_APP=main.py
```
- Mac:
```
export FLASK_APP=main.py
```

- Comando para ejecutar el servidor
```
flask --app main run
```

- Comando para ejecutar el servidor en otro puerto diferente del default que es siempre el 5000
```
flask --app main run -p 5002
```

- Comando para ejecutar el servidor en modo debug, para realizar cambios en código en tiempo real
```
flask --app main --debug run
```