from flask import Blueprint, request, jsonify
from .models import Usuario, Transacao
from . import db
from datetime import datetime, timezone
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main = Blueprint('main', __name__)

# Rota inicial
@main.route('/')
def index():
    return jsonify({"msg": "Bem vindo(a) ao BancoPY"})

@main.route('/registro', methods=['POST'])
def registro():
    dados = request.get_json()
    if Usuario.query.filter_by(nome=dados['nome']).first():
        return jsonify({"erro": "User já cadastrado (a)"}), 400
    novo_usuario = Usuario(nome=dados['nome'], nome=dados['nome'])
    novo_usuario.set_senha(dados['senha']) # senha segura
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify ({"msg": "User cadastrado (a) com sucesso!"}), 201

@main.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = Usuario.query.filter_by(nome=dados['nome']).first()

    if not usuario or not usuario.checar_senha(dados['senha']):
        return jsonify({"erro": "E-mail ou senha incorretos"}), 401
    
    token = create_access_token(identity=usuario.id)
    return jsonify({"token": token}), 200

# protegendo a rota com JWT (middleware)
@main.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    user_id = get_jwt_identity()
    usuario = Usuario.query.get(user_id)
    return jsonify({
        'id': usuario.id,
        'nome': usuario.nome,
    })






# Rota para novo user
# @main.route('/usuarios', methods=['POST'])

# def criar_usuario():
#     dados = request.get_json() # Pega o json da requisição
#     novo_usuario = Usuario(nome=dados['nome'])
#     db.session.add(novo_usuario) # Prepara para salvar
#     db.session.commit() # Salva no banco
#     return jsonify({'mensagem' : "Usuário (a) criado (a) com sucesso!"}), 201 # Resposta do JSON

# @main.route('/usuario/<int:user_id>', methods=['GET'])
# def get_usuario(user_id):   
#     user = Usuario.query.get(user_id)
#     if user:
#         return jsonify({
#             "user_id": user.id,
#             "nome": user.nome,
#             "patrimonio": user.patrimonio,
#             "limite_cartao": user.limite_cartao,
#             "limite_emprestimo": user.limite_emprestimo,
#         }) # salvamos em json apenas para resposta para o usuário
    
#     return jsonify({"error": "Usuário (a) não encontrado (a)"}), 404
    
# @main.route('/usuario/<int:user_id>', methods=['DELETE'])
# def delete_usuario(user_id):
#     user = Usuario.query.get(user_id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({"mensagem": "Usuário (a) excluído (a) com sucesso!"}), 200
#     else:
#         return jsonify({"error": "Usuário (a) não encontrado (a)"}), 404
