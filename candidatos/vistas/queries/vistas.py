from flask_restful import Resource
from candidatos.modelos.modelos import db, CandidatoSchema, Candidato
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from datetime import datetime
from celery import Celery
import requests


celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')
candidato_schema = CandidatoSchema()

class VistaCandidatosQ(Resource):
    @jwt_required()
    def get(self):
        candidatos = Candidato.query.all()
        return [candidato_schema.dump(candidato) for candidato in candidatos],200
    
class VistaCandidatoQ(Resource):
    @jwt_required()
    def get(self, id_candidato):
        return candidato_schema.dumps(Candidato.query.get_or_404(id_candidato)),200
    
