from app.model.Eleicao import Eleicao, EleicaoSchema
from app.model.Candidato import Candidato
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()




def registro(desc): 

    nova_eleicao = Eleicao(descricao = desc, agendada = False)

    try:

        session.add(nova_eleicao)
        session.commit()
        
        return jsonify({'msg' : 'Eleição registrada com sucesso.'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar eleição.'}), 500




def agendar(data):

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['id']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    if eleicao.agendada == True:
        return jsonify({'msg' : 'Esta eleição já foi agendada.'}), 405

    inicio = data['inicio']
    fim = data['fim']

    if inicio < datetime.datetime.utcnow() or inicio > fim:
        return jsonify({'msg' : 'Datas inválidas'}), 400

    candidatos = session.query(Candidato.count(Candidato.id)).filter(Candidato.eleicao_id == eleicao.id)

    if candidatos > 1:

        try:

            eleicao.agendada = True
            eleicao.inicio = inicio
            eleicao.fim = fim
            session.commit()

            return jsonify({'msg' : 'Eleição agendada com sucesso'}), 200

        except:

            session.rollback()
            return jsonify({'msg' : 'Erro ao agendar eleição.'}), 500

    else:

        return jsonify({'msg' : 'Não há candidatos registrados nessa eleição.'}), 409





def alterarDescricao(data):

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['id']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    try:
    
        eleicao.descricao = data['descricao']
        session.commit()

        return jsonify({'msg' : 'Descrição da eleição alterada com sucesso.'})

    except:

        session.rollback()
        return jsonify({'msg' : 'Erro ao alterar descrição da eleição.'}), 500




def retornarAgendadas():

    eleicoes = session.query(Eleicao).filter(Eleicao.agendada == True, Eleicao.inicio > datetime.datetime.utcnow()).all()
    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes).data

    return jsonify({'eleicoes' : output})




def retornarIniciadas():

    eleicoes = session.query(Eleicao).filter(Eleicao.agendada == True, Eleicao.inicio <= datetime.datetime.utcnow()).all()
    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes).data

    return jsonify({'eleicoes' : output})




def retornarFinalizadas():

    eleicoes = session.query(Eleicao).filter(Eleicao.fim < datetime.datetime.utcnow()).all()
    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes).data

    return jsonify({'eleicoes' : output})





