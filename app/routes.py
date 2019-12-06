from app import app
from app.control import EleitorController
from flask import request, json, jsonify

@app.route('/')
@app.route('/index')
def index():
    return "Início"


@app.route('/Eleitor/login', methods=['POST'])
def loginEleitor():

    email = request.get_json()['email']
    senha = request.get_json()['senha']

    return EleitorController.logarEleitor(email, senha)


@app.route('/Eleitor/registro', methods=['POST'])
def registroEleitor():

    email = request.get_json()['email']
    senha = request.get_json()['senha']

    result = jsonify(EleitorController.registrarEleitor(email, senha))
    return result



