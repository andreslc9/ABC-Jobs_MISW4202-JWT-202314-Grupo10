from flask_restful import Resource
from usuarios.modelos.modelos import db, Usuario, UsuarioSchema
from flask import request
from flask import jsonify
import random

from celery import Celery

celery_app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

usuario_schema = UsuarioSchema

@celery_app.task(name='generar.token')
def generar_token(usuario):
    pass

def numero_aleatorio():
    return round(random.random())


# Función para obtener permisos por usuario y contraseña
def obtener_permisos(u_usuario, u_contrasena):
    usuario = Usuario.query.filter_by(usuario=u_usuario, contrasena=u_contrasena).first()
    if usuario:
        permisos = usuario.permisos
        return permisos
    else:
        return None

class VistaUsuarios(Resource):
    
    def get(self):
        return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
    
    def post(self):
        permisos=numero_aleatorio()
        print(permisos)
        nuevo_usuario = Usuario(usuario=request.json['usuario'],\
                                contrasena=request.json['contrasena'],\
                                permisos=permisos)
        #token_de_acceso = create_access_token(identity = request.json['usuario'])
        #identificador = request.json['usuario']
        #args=(identificador,)
        #generar_token.apply_async(args=args)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {'mensaje':'usuario creado exitosamente'}, 200
    
class VistaLogIn(Resource):
    def post(self):
        u_usuario = request.json['usuario']
        u_contrasena = request.json['contrasena']
        usuario = Usuario.query.filter_by(usuario=u_usuario, contrasena=u_contrasena)
        permisos_obtenidos = obtener_permisos(u_usuario, u_contrasena)
        print(permisos_obtenidos)
        if usuario:
            if permisos_obtenidos==0:
                identificador = request.json['usuario']
                args=(identificador,)
                tarea=generar_token.apply_async(args=args)
                resultado=tarea.get()
                #return {'mensaje':'Inicio de sesión exitoso','token':access_token}, 200
                return {'token':resultado}, 200
            else:
                return {'mensaje':'Inicio de sesión exitoso'}, 201
        else:
            return {'mensaje':'Nombre de usuario o contraseña incorrecta'}, 400