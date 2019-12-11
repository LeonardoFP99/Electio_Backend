from app.model.Models import Administrador
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app, bcrypt
from app.db import Session
import jwt
import datetime

CORS(app)
session = Session()




def login(auth):

    admin = session.query(Administrador).filter(Administrador.email == auth['email']).first()

    if not admin:
        return make_response('Admin. não encontrado.', 401, {'WWW-Authenticate' : 'Basic realm = "Login requerido!"'})

    if bcrypt.check_password_hash(admin.senha, auth['senha']):

        token = jwt.encode({'id': admin.id, 'email' : admin.email, 'type' : 'administrador', 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')}), 200

    else:
        return make_response('Senha incorreta.', 401, {'WWW-Authenticate' : 'Basic realm = "Login requerido!"'})



    
def registro(data):

    admin = session.query(Administrador).filter(Administrador.email == data['email']).first()

    if admin:
        return jsonify({'msg' : 'Este email já está sendo usado.'}), 409

    hash_senha = bcrypt.generate_password_hash(data['senha']).decode('utf-8')

    novo_admin = Administrador(email=data['email'], senha=hash_senha)

    try:

        session.add(novo_admin)
        session.commit()

        return jsonify({'msg' : 'Novo usuário administrador criado.'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar administrador.'}), 500

        

