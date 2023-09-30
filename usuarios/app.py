from usuarios import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from usuarios.vistas.vistas import VistaLogIn, VistaUsuarios
from usuarios.modelos.modelos import db
import requests


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaLogIn, '/login')

jwt = JWTManager(app)
