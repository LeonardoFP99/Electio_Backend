from app.model.Models import Eleitor, Administrador
from flask import jsonify, json, make_response, request
from flask_cors import CORS
from app import app
from app.db import Session
from functools import wraps
import jwt

CORS(app)
session = Session()




def admin_req(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'msg' : 'Você não possui o token de acesso.'}), 401

        data = jwt.decode(token, app.config['SECRET_KEY'])

        if not data['type'] == 'administrador':
            return jsonify({'msg' : 'Você não tem permissões de administrador.'}), 401

        user = session.query(Administrador).filter(Administrador.id == data['id']).first()

        if not user:
            return jsonify({'msg' : 'Token de acesso inválido.'}), 401

        return f(user, *args, **kwargs)

    return decorated




def eleitor_req(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'msg' : 'Você não possui o token de acesso.'}), 401

        data = jwt.decode(token, app.config['SECRET_KEY'])

        if not data['type'] == 'eleitor':
            return jsonify({'msg' : 'Você não tem permissões de eleitor.'}), 401

        user = session.query(Eleitor).filter(Eleitor.id == data['id']).first()

        if not user:
            return jsonify({'msg' : 'Token de acesso inválido.'}), 401

        return f(user, *args, **kwargs)

    return decorated




def anon_req(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        if 'x-access-token' in request.headers:
            return jsonify({'msg' : 'Você não pode estar logado para executar esta ação.'}), 401

        return f(*args, **kwargs)   

    return decorated    