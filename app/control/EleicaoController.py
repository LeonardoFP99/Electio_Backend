from app.model.Models import Eleicao, EleicaoSchema, Candidato
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()




def registro(desc): #Registra eleição, sem datas de início e fim

    nova_eleicao = Eleicao(descricao = desc, agendada = False)

    try:

        session.add(nova_eleicao)
        session.commit()
        
        return jsonify({'msg' : 'Eleição registrada com sucesso.'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar eleição.'}), 500




def agendar(data): #Registrar data de início e fim da eleição

    eleicao = session.query(Eleicao).filter(Eleicao.id == data['id']).first()

    if not eleicao:
        return jsonify({'msg' : 'Eleição não encontrada.'}), 404

    if eleicao.agendada == True:
        return jsonify({'msg' : 'Esta eleição já foi agendada.'}), 405

    inicio_s = str()
    fim_s = str()

    inicio_s = data['inicio']
    fim_s = data['fim']

    inicio = datetime.datetime.strptime(inicio_s, '%Y/%m/%d %H:%M')
    fim = datetime.datetime.strptime(fim_s, '%Y/%m/%d %H:%M')


    if inicio < datetime.datetime.now() or inicio > fim:
        return jsonify({'msg' : 'Datas inválidas.'}), 400

    candidatos = session.query(Candidato).filter(Candidato.eleicao_id == eleicao.id).count()

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




def retornarNaoAgendadas(): #Retorna eleicões não agendadas, sem data de início e fim

    eleicoes = session.query(Eleicao.id, Eleicao.descricao).filter(Eleicao.agendada == False).all()

    if not eleicoes:
        return jsonify({'msg' : 'Não foram encontradas eleições não agendadas.'}), 404

    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes)

    return jsonify({'eleicoes' : output})




def retornarAgendadas(): #Retorna eleições agendadas, mas não iniciadas

    eleicoes = session.query(Eleicao.id, Eleicao.descricao, Eleicao.inicio, Eleicao.fim).filter(
        Eleicao.agendada == True, 
        Eleicao.inicio > datetime.datetime.now()
        ).all()
    
    if not eleicoes:
        return jsonify({'msg' : 'Não foram encontradas eleições agendadas.'}), 404

    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes)

    return jsonify({'eleicoes' : output})




def retornarIniciadas(): #Retorna eleições iniciadas, finalizadas ou não

    eleicoes = session.query(Eleicao.id, Eleicao.descricao, Eleicao.inicio, Eleicao.fim).filter(
        Eleicao.agendada == True, 
        Eleicao.inicio <= datetime.datetime.now()
        ).all()
    
    if not eleicoes:
        return jsonify({'msg' : 'Não foram encontradas eleições iniciadas.'}), 404

    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes)

    return jsonify({'eleicoes' : output})




def retornarAtivas(): #Retorna eleições iniciadas, mas não finalizadas
    
    eleicoes = session.query(Eleicao.id, Eleicao.descricao, Eleicao.inicio, Eleicao.fim).filter(
        Eleicao.agendada == True, 
        Eleicao.inicio <= datetime.datetime.now(), 
        Eleicao.fim >= datetime.datetime.now()
        ).all()

    if not eleicoes:
        return jsonify({'msg' : 'Não foram encontradas eleições ativas.'}), 404

    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes)

    return jsonify({'eleicoes' : output})
    



def retornarFinalizadas(): #Retorna eleições finalizadas

    eleicoes = session.query(Eleicao).filter(Eleicao.fim < datetime.datetime.now()).all()
    
    if not eleicoes:
        return jsonify({'msg' : 'Não foram encontradas eleições finalizadas.'}), 404

    eleicoes_schema = EleicaoSchema(many = True)
    output = eleicoes_schema.dump(eleicoes)

    return jsonify({'eleicoes' : output})
