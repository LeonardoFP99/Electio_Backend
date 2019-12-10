from app.model.Voto import Voto, VotoSchema
from app.model.Eleitor import Eleitor
from app.model.Candidato import Candidato
from app.model.Eleicao import Eleicao
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()



def registro(data):

    eleitor = session.query(Eleitor).filter(Eleitor.id == data['eleitor']).first()

    if not eleitor:
        return jsonify({'msg' : 'Eleitor não encontrado.'}), 404

    candidato = session.query(Candidato).filter(Candidato.id == data['candidato']).first()

    if not candidato:
        return jsonify({'msg' : 'Candidato não encontrado.'}), 404

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['eleicao']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    novo_voto = Voto(eleitor_id = data['eleitor'], candidato_id = data['candidato'], eleicao_id = data['eleicao'])

    try:

        session.add(novo_voto)
        session.commit()

        return jsonify({'msg' : 'Voto realizado com sucesso!'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar voto.'}), 500




def retornarPorEleitor(id):

    eleitor = session.query(Eleitor).filter(Eleitor.id == id).first()

    if not eleitor:
        return jsonify({'msg' : 'Eleitor não encontrado.'}), 404

    votos = session.query(Voto).filter(Voto.eleitor_id == id).all()

    if not votos:
        return jsonify({'msg' : 'Não foram encontrados votos deste eleitor.'}), 404

    votos_schema = VotoSchema(many = True)
    output = votos_schema.dump(votos).data

    return jsonify({'votos' : output})



def retornarPorCandidato(id):

    candidato = session.query(Candidato).filter(Candidato.id == id).first()

    if not candidato:
        return jsonify({'msg' : 'Candidato não encontrado.'}), 404

    votos = session.query(Voto).filter(Voto.candidato_id == id).all()

    if not votos:
        return jsonify({'msg' : 'Não foram encontrados votos deste candidato.'}), 404

    votos_schema = VotoSchema(many = True)
    output = votos_schema.dump(votos).data

    return jsonify({'votos' : output})




def retornarPorEleicao(id):

    eleicao = session.query(Eleicao).filter(Eleicao.id == id).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    votos = session.query(Voto).filter(Voto.eleicao_id == id).all()

    if not votos:
        return jsonify({'msg' : 'Não foram encontrados votos desta eleição.'}), 404

    votos_schema = VotoSchema(many = True)
    output = votos_schema.dump(votos).data

    return jsonify({'votos' : output})

    