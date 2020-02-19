from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['DATABASE_URL'] = 'postgres://mjxxxnrahzujwy:1ed9886e0e42047b279fb88bea07f72cb3610886fac656d0c6d2cb7890508219@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d7qfpmvsev52ls'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


from workout_tracker import routes
