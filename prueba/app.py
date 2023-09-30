from prueba import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from prueba.modelos.modelos import Resultados, ResultadoSchema, db
import requests

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
api = Api(app)

resultado_schema = ResultadoSchema()

def editar_candidato():
    for i in range (1000):
        crear_usuario='http://127.0.0.1:5000/usuarios'
        login_usuario='http://127.0.0.1:5000/login'
        consultar_candidato='http://127.0.0.1:9000/querys/candidatos'
        datos_usuario={
            'usuario':'usuario{}'.format(i),
            'contrasena':'12345'
        }
        response_ingreso = requests.post(crear_usuario, json=datos_usuario, headers={'Content-Type':'application/json'})
        
        if response_ingreso.status_code == 200:
            data = response_ingreso.json()
            print(data)
            response_login = requests.post(login_usuario, json=datos_usuario, headers={'Content-Type':'application/json'})
            if response_login.status_code == 200:
                token = response_login.json()
                token_formateado = token['token']
                print(token_formateado)
                response_consulta = requests.get(consultar_candidato, headers={'Authorization':'Bearer {}'.format(token_formateado)})
                if response_consulta.status_code == 200:
                    nuevo_resultado = Resultados(permisos="candidato",acceso="permitido",resultado="positivo")
                    db.session.add(nuevo_resultado)
                    db.session.commit()
                    print("Tiene permiso")
                else:
                    nuevo_resultado = Resultados(permisos="usuario",acceso="denegado",resultado="negativo")
                    db.session.add(nuevo_resultado)
                    db.session.commit()
                    print("No tiene permiso") 
            else:
                nuevo_resultado = Resultados(permisos="empresa",acceso="denegado",resultado="positivo")
                db.session.add(nuevo_resultado)
                db.session.commit()
                print("Sesión iniciada, sin permisos")
        else:
            print(f'Error:{response_ingreso.status_code}')
            print(response_ingreso.text)
            
editar_candidato()