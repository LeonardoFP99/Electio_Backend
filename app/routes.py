from app import app
from app.control import (
    EleitorController, 
    EleicaoController, 
    AdministradorController, 
    CandidatoController, 
    VotoController, 
    Autorizacao)
from flask import request, json, jsonify, make_response




# Endpoints do Eleitor

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




@app.route('/Eleitor/eleicoes', methods=['GET'])
def consultaEleicoesVotar():

    return EleicaoController.retornarAtivas()




@app.route('/Eleitor/eleicoes/candidatos', methods=['POST'])
def consultaEleitorEleicoesCandidatos():

    try:

        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return CandidatoController.retornarPorEleicao(eleicao_id)




@app.route('Eleitor/votos', methods=['POST'])
def consultaEleitorVotos():

    try:

        eleitor_id = request.get_json()['eleitor']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return VotoController.retornarPorEleitor(eleitor_id)




@app.route('/Eleitor/votar', methods=['POST'])
def votar():

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
def registrarEleicao():

    try:

        descricao = request.get_json()['descricao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return EleicaoController.registro(descricao)




@app.route('/Admin/eleicoes/alterar', methods=['PUT'])
def alterarDescricaoEleicao():

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
def agendarEleicao():

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
def consultaEleicoesNaoAgendadas():

    return EleicaoController.retornarNaoAgendadas()




@app.route('/Admin/eleicoes/agendadas', methods=['GET'])
def consultaEleicoesAgendadas():

    return EleicaoController.retornarAgendadas




@app.route('/Admin/eleicoes/iniciadas', methods=['GET'])
def consultaEleicoesIniciadas():

    return EleicaoController.retornarIniciadas()




@app.route('/Admin/eleicoes/ativas', methods=['GET'])
def consultaEleicoesAtivas():

    return EleicaoController.retornarAtivas




@app.route('/Admin/eleicoes/candidatos', methods=['POST'])
def consultaAdminEleicoesCandidatos():

    try:

        eleicao_id = request.get_json()['eleicao']

    except KeyError:

        return jsonify({'msg': 'Dados insuficientes ou mal-formatados'}), 400

    return CandidatoController.retornarPorEleicao(eleicao_id)




@app.route('/Admin/candidatos/adicionar', methods=['POST'])
def adicionarCandidato():

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
def removerCandidato():

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


