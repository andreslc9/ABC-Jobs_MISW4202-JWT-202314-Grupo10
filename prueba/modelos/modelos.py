from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Resultados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permisos = db.Column(db.String(50))
    acceso = db.Column(db.String(50))
    resultado = db.Column(db.Integer)
    
class ResultadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Resultados
        load_instance = True