from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from google import genai

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'es'

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')

mail = Mail(app)

moment = Moment(app)

babel = Babel(app, locale_selector=get_locale)

# Configuración del nuevo cliente de Google Gen AI
key = app.config.get('MS_TRANSLATOR_KEY')
print(f"DEBUG: API Key exists: {key is not None}")
genai_client = genai.Client(api_key=key)
# El modelo "Flash" es ideal para APIs por su velocidad. 
# Nota: gemini-2.0-flash es el modelo estable más reciente de la serie 2.
model_name = 'gemini-2.5-flash' 

from app import routes, models, errors