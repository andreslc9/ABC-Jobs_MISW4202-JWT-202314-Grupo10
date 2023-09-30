from celery import Celery
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask import current_app
from flask import Flask


celery_app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

@celery_app.task(name='generar.token')
def generar_token(usuario):
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = 'secreto'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    with app.app_context():
        access_token = create_access_token(identity=usuario)
        return access_token