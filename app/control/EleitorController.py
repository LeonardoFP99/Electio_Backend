from app.model.Eleitor import Eleitor
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app, bcrypt
from app.db import Session
import jwt
import datetime

CORS(app)
session = Session()




def login(auth):

    eleitor = session.query(Eleitor).filter(Eleitor.email == auth['email']).first()

    if not eleitor:
        return make_response('Eleitor não encontrado.', 401, {'WWW-Authenticate' : 'Basic realm = "Login requerido!"'})

    if bcrypt.check_password_hash(eleitor.senha, auth['senha']):

        token = jwt.encode({'email' : eleitor.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')}), 200

    else:
        return make_response('Senha incorreta.', 401, {'WWW-Authenticate' : 'Basic realm = "Login requerido!"'})



    
def registro(data):

    eleitor = session.query(Eleitor).filter(Eleitor.email == data['email']).first()

    if eleitor:
        return jsonify({'msg' : 'Este email já está sendo usado.'}), 409

    hash_senha = bcrypt.generate_password_hash(data['senha']).decode('utf-8')

    novo_eleitor = Eleitor(email=data['email'], senha=hash_senha)

    try:

        session.add(novo_eleitor)
        session.commit()

        return jsonify({'msg' : 'Novo usuário eleitor criado.'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar eleitor.'}), 500

        

