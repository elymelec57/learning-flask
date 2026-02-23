from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

def get_locale():
    #return request.accept_languages.best_match(app.config['LANGUAGES'])
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

from app import routes, models, errors