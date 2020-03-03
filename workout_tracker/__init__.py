from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sandyface@localhost/workouts'
app.config['HEROKU_POSTGRESQL_WHITE_URL'] = 'postgres://azgudlzgtlhjlu:4a477fdc2a07c465ba40bde3b8930bfdf3f81c3e90a9c496d8aff4c9da2e964c@ec2-52-23-14-156.compute-1.amazonaws.com:5432/d82i4boaphj7oj'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from workout_tracker import routes



