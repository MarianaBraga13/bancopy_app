from . import db
from datetime import datetime, timezone

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    patrimonio = db.Column(db.Float, default=0.0)
    limite_cartao = db.Column(db.Float, default=0.0)
    limite_emprestimo = db.Column(db.Float, default=0.0)

class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    tipo = db.Column(db.String)
    valor = db.Column(db.Float)
    data = db.Column(db.DateTime, default=datetime.now(timezone.utc))
