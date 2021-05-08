from flask import Flask

#Create a flask instance
app = Flask(__name__)
#Loads flask configurations from config.py
app.secret_key = app.config['SECRET_KEY']
app.config.from_object("config")

#Setup the Flask SocketIO integration (Required only for asynchronous scenarios)
from flask_socketio import SocketIO
socketio = SocketIO(app,logger=True,engineio_logger=True,message_queue=app.config['BROKER_URL'])
