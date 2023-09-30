from autenticador.vistas.vistas import AuthResource
from flask_restful import Api
from flask_jwt_extended import JWTManager
from autenticador import create_app

app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)

api.add_resource(AuthResource, '/autenticador')

jwt = JWTManager(app)