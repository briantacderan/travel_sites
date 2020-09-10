from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# to initialize database instance (song_library.db)
# $ python3
# >>> from app import db
# >>> db.create_all()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login = LoginManager()
login.login_view = 'login'
login.init_app(app)



import routes, models