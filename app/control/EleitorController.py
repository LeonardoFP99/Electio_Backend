from app.model.Eleitor import Eleitor
from flask import jsonify, json
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS
from app import app

app.config['JWT_SECRET_KEY'] = 'elibnom'

jwt_manager = JWTManager(app)
CORS(app)

def logarEleitor(email, senha):

    result = ""

    try:

        Eleitor.login(Eleitor, email, senha)

    except Exception as ex:

        result = jsonify({"erro":ex})

    else:

        acesso = create_access_token(identity = {'email' : email})
        result = jsonify({"token":acesso})

    finally:

        return result

    
def registrarEleitor(email, senha):

    result = ""

    try:

        Eleitor.registrar(Eleitor, email, senha)

    except Exception as ex:

        result = jsonify({"erro":ex})

    else:

        result = jsonify({
            "email" : email,
            "senha" : senha
        })

    finally:

        return result