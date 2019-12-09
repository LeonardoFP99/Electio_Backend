from app import app
from app.control import EleitorController
from flask import request, json, jsonify, make_response



@app.route('/Eleitor/login', methods=['POST'])
def loginEleitor():

    try:

        log_email = request.get_json()['email']
        log_senha = request.get_json()['senha']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    auth = {
        "email": log_email,
        "senha": log_senha
    }

    return EleitorController.login(auth)



@app.route('/Eleitor/registro', methods=['POST'])
def registroEleitor():

    try:

        reg_email = request.get_json()['email']
        reg_senha = request.get_json()['senha']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "email": reg_email,
        "senha": reg_senha
    }

    return EleitorController.registro(data)



