# save this as app.py
import time
from pydantic import BaseModel, ValidationError

import flask
from flask import Flask, abort

app = Flask(__name__)
db = []
for i in range(3):
    db.append({
        'name': f'user{i}',
        'time': 10000*i,
        'text': f'text {i}'
    })
class Message(BaseModel):

    name: str
    text: str

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/send", methods= ['POST'])
def send_message():

    data = flask.request.json

    try:
        message = Message.parse_obj(data)
    except ValidationError as e:
        return abort(400, str(e))

    text = data['text']
    name = data['name']
    message_data = {
        'text': text,
        'name': name,
        'time': time.time()
    }

    db.append(message_data)
    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        abort(400)
    db_after = []
    for message in db:
        if message['time'] > after:
            db_after.append(message)
    return {'messages': db_after}

@app.route("/status")
def print_status():
    num_messages = len(db)
    num_users = len(set(message['name'] for message in db))
    return {
        "status": "ok",
        "number_of_messages": num_messages,
        "number_of_users": num_users
    }


@app.route('/index')
def lionel(): 
    return flask.render_template('index.html')


app.run()