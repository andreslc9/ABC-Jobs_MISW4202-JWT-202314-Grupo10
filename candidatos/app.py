from candidatos import create_app

from flask_restful import Api
from flask_jwt_extended import JWTManager
from candidatos.modelos.modelos import db, Candidato, CandidatoSchema
from candidatos.vistas.commands.vistas import VistaCandidatoC, VistaCandidatosC
from candidatos.vistas.queries.vistas import VistaCandidatoQ, VistaCandidatosQ
app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api_queries = Api(app)
api_commands = Api(app)
api_commands.add_resource(VistaCandidatosC, '/comandos/candidatos')
api_commands.add_resource(VistaCandidatoC, '/comandos/candidato/<int:id_candidato>')
api_queries.add_resource(VistaCandidatosQ, '/querys/candidatos')
api_queries.add_resource(VistaCandidatoQ, '/querys/candidato/<int:id_candidato>')

jwt = JWTManager(app)