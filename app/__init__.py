from flask import Flask
from flask import g
from flask_socketio import SocketIO
from flask_babel import Babel

app = Flask(__name__, template_folder="templates")
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'locales'
socketio = SocketIO(app, cors_allowed_origins='*')

babel = Babel(app)


@babel.localeselector
def get_locale():
    return getattr(g, 'LOCALE', 'en')

from app import views