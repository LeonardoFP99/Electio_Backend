from app.model.Eleicao import Eleicao
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()




def registro(data):

    inicio = data['inicio']
    fim = data['fim']

    if inicio > fim:
        return jsonify({'msg' : 'Data de início inválida.'}), 422

    nova_eleicao = Eleicao(descricao = data['descricao'], inicio = data['inicio'], fim = data['fim'])

    try:

        session.add(nova_eleicao)
        session.commit()

        return jsonify({'msg' : 'Nova eleição registrada.'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar eleição.'}), 500




def alteracao(data):

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['id']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    try:
    
        eleicao.descricao = data['descricao']
        session.commit()

        return jsonify({'msg' : 'Descrição da eleição alterada com sucesso.'})

    except:

        return jsonify({'msg' : 'Erro ao alterar descrição da eleição.'}), 500
