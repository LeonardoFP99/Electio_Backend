from app import app
from app.control import (
    EleitorController, 
    EleicaoController, 
    AdministradorController, 
    CandidatoController, 
    VotoController)
from app.control.Autorizacao import admin_req, eleitor_req, anon_req
from flask import request, json, jsonify, make_response




# Endpoints do Eleitor

@app.route('/Eleitor/login', methods=['POST'])
@anon_req
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
@anon_req
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




@app.route('/Eleitor/eleicoes', methods=['GET'])
@eleitor_req
def consultaEleicoesVotar(user):

    return EleicaoController.retornarAtivas()




@app.route('/Eleitor/eleicoes/candidatos', methods=['POST'])
@eleitor_req
def consultaEleitorEleicoesCandidatos(user):

    try:

        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return CandidatoController.retornarPorEleicao(eleicao_id)




@app.route('/Eleitor/votos', methods=['POST'])
@eleitor_req
def consultaEleitorVotos(user):

    try:

        eleitor_id = request.get_json()['eleitor']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return VotoController.retornarPorEleitor(eleitor_id)




@app.route('/Eleitor/votar', methods=['POST'])
@eleitor_req
def votar(user):

    try:

        eleitor_id = request.get_json()['eleitor']
        candidato_id = request.get_json()['candidato']
        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "eleitor" : eleitor_id,
        "candidato" : candidato_id,
        "eleicao" : eleicao_id
    }

    return VotoController.registro(data)

    


# Apuração

@app.route('/Apuracao', methods=['GET'])
def apuracao():

    return EleicaoController.retornarFinalizadas()



    
# Endpoints do Administrador

@app.route('/Admin/login', methods=['POST'])
@anon_req
def loginAdmin():

    try:

        log_email = request.get_json()['email']
        log_senha = request.get_json()['senha']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    auth = {
        "email": log_email,
        "senha": log_senha
    }

    return AdministradorController.login(auth) 




@app.route('/Admin/registro', methods=['POST'])
@anon_req
def registroAdmin():

    try:

        reg_email = request.get_json()['email']
        reg_senha = request.get_json()['senha']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "email": reg_email,
        "senha": reg_senha
    }

    return AdministradorController.registro(data)




@app.route('/Admin/eleicoes/registro', methods=['POST'])
@admin_req
def registrarEleicao(user):

    try:

        descricao = request.get_json()['descricao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return EleicaoController.registro(descricao)




@app.route('/Admin/eleicoes/alterar', methods=['PUT'])
@admin_req
def alterarDescricaoEleicao(user):

    try:

        eleicao_id = request.get_json()['id']
        descricao = request.get_json()['descricao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "id" : eleicao_id,
        "descricao" : descricao
    }

    return EleicaoController.alterarDescricao(data)




@app.route('/Admin/eleicoes/agendar', methods=['PUT'])
@admin_req
def agendarEleicao(user):

    try:

        eleicao_id = request.get_json()['id']
        inicio = request.get_json()['inicio']
        fim = request.get_json()['fim']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "id" : eleicao_id,
        "inicio" : inicio,
        "fim" : fim
    }

    return EleicaoController.agendar(data)




@app.route('/Admin/eleicoes/naoAgendadas', methods=['GET'])
@admin_req
def consultaEleicoesNaoAgendadas(user):

    return EleicaoController.retornarNaoAgendadas()




@app.route('/Admin/eleicoes/agendadas', methods=['GET'])
@admin_req
def consultaEleicoesAgendadas(user):

    return EleicaoController.retornarAgendadas




@app.route('/Admin/eleicoes/iniciadas', methods=['GET'])
@admin_req
def consultaEleicoesIniciadas(user):

    return EleicaoController.retornarIniciadas()




@app.route('/Admin/eleicoes/ativas', methods=['GET'])
@admin_req
def consultaEleicoesAtivas(user):

    return EleicaoController.retornarAtivas




@app.route('/Admin/eleicoes/candidatos', methods=['POST'])
@admin_req
def consultaAdminEleicoesCandidatos(user):

    try:

        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return CandidatoController.retornarPorEleicao(eleicao_id)




@app.route('/Admin/candidatos/adicionar', methods=['POST'])
@admin_req
def adicionarCandidato(user):

    try:

        eleicao_id = request.get_json()['eleicao']
        nome = request.get_json()['nome']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    try:

        partido = request.get_json()['partido']

    except KeyError:

        partido = None

    data = {
        "eleicao" : eleicao_id,
        "nome" : nome,
        "partido" : partido
    }

    return CandidatoController.adicionar(data)




@app.route('/Admin/candidatos/remover', methods=['DELETE'])
@admin_req
def removerCandidato(user):

    try:

        candidato_id = request.get_json()['candidato']
        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    data = {
        "candidato" : candidato_id,
        "eleicao" : eleicao_id
    }

    return CandidatoController.remover(data)


