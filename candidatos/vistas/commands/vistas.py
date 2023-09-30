from flask_restful import Resource
from candidatos.modelos.modelos import db, CandidatoSchema, Candidato
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from datetime import datetime
from celery import Celery

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')
candidato_schema = CandidatoSchema()

class VistaCandidatosC(Resource):
    @jwt_required()
    def post(self):
        nuevo_candidato = Candidato(nombre=request.json['nombre'],\
                                profesion=request.json['profesion'])
        db.session.add(nuevo_candidato)
        db.session.commit()
        return candidato_schema.dump(nuevo_candidato)
    
class VistaCandidatoC(Resource):
    @jwt_required()
    def put(self, id_candidato):
        candidato = Candidato.query.get_or_404(id_candidato)
        candidato.nombre = request.json.get('nombre', candidato.nombre)
        candidato.profesion = request.json.get('profesion', candidato.profesion)
        db.session.commit()
        return candidato_schema.dump(candidato)
    
