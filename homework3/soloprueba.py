import time
from datetime import datetime
import flask     # extension  Flask es la clase
from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    current_time = datetime.now()  # Crear una instancia de datetime
    return {
        'status': True,
        'name': 'Messenger',
        'time1': time.asctime(),
        'time2': time.time(),
        'time3': current_time,  # Utilizar la instancia creada
        'time4': str(current_time),  # Utilizar la instancia creada
        'time5': current_time.strftime('%Y/%y/%m/%d time: %H:%M:%S '),  # Utilizar la instancia creada
        'time6': current_time.isoformat()  # Llamar al método en la instancia creada
    }

app.run()