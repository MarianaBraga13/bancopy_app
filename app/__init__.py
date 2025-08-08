from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_de_seguranca'
    app.config['JWT_SECRET_KEY'] = "jwt_secreto_muito_forte"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_py.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .models import Usuario, Transacao
        db.create_all()

# Importando as rotas

    from .routes import main
    app.register_blueprint(main)       

    return app