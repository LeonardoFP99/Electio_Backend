from flask import Flask
from flask_bcrypt import Bcrypt
from app.model.Base_Declarativa import Base
from app.db import engine

app = Flask(__name__)

app.config['SECRET_KEY'] = 'elibnom'
bcrypt = Bcrypt(app)

from app import routes

Base.metadata.create_all(engine)