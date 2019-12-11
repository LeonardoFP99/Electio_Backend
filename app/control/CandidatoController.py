from app.model.Models import Candidato, CandidatoSchema, Eleicao
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()




def adicionar(data):

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['eleicao']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    if eleicao.agendada == True:
        return jsonify({'msg' : 'Esta eleição já foi agendada.'}), 405

    novo_candidato = Candidato(nome = data['nome'], partido = data['partido'], eleicao_id = data['eleicao'])

    try:

        session.add(novo_candidato)
        session.commit()

        return jsonify({'msg' : 'Candidato adicionado com sucesso.'}), 200

    except:

        session.rollback()
        return jsonify({'msg' : 'Erro ao adicionar candidato.'}), 500




def remover(data):

    candidato = session.query(Candidato).filter(Candidato.id == data['candidato']).first()

    if not candidato:
        return jsonify({'msg' : 'Candidato não encontrado.'}), 404

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['eleicao']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    if eleicao.agendada == True:
        return jsonify({'msg' : 'Esta eleição já foi agendada.'}), 405

    try:
    
        session.delete(candidato)
        session.commit()

        return jsonify({'msg' : 'Candidato removido com sucesso.'}), 200

    except:

        session.rollback()
        return jsonify({'msg' : 'Erro ao remover candidato.'}), 500


    

def retornarPorEleicao(id):

    eleicao = session.query(Eleicao).filter(Eleicao.id == id).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    candidatos = session.query(Candidato.id, Candidato.nome, Candidato.partido).filter(Candidato.eleicao_id == id).all()
    
    if not candidatos:
        return jsonify({'msg' : 'Não foram encontrados candidatos nesta eleição.'}), 404

    candidatos_schema = CandidatoSchema(many = True)
    output = candidatos_schema.dump(candidatos)

    return jsonify({'candidatos' : output}), 200
