from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__, template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins='*')

from app import views