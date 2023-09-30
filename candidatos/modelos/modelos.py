from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    profesion = db.Column(db.String(50))
    
    def __repr__(self):
        return "{}-{}".format(self.nombre, self.profesion)
    
class CandidatoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Candidato
        load_instance = True