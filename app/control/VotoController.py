from app.model.Voto import Voto 
from flask import jsonify, json, make_response
from flask_cors import CORS
from app import app
from app.db import Session
import datetime

CORS(app)
session = Session()



def registro(data):

    novo_voto = Voto(eleitor_id = data['eleitor'], candidato_id = data['candidato'], eleicao_id = data['eleicao'])

    try:

        session.add(novo_voto)
        session.commit()

        return jsonify({'msg' : 'Voto realizado com sucesso!'}), 200

    except:

        return jsonify({'msg' : 'Erro ao registrar voto.'}), 500
