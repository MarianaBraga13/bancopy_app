from flask import Blueprint, request, jsonify
from .models import Usuario, Transacao
from . import db
from datetime import datetime, timezone

main = Blueprint('main', __name__)

# importante lembrar que, numa arquitetura REST quanto a query é feita
# a resposta para o user é salva temporariamente no jsonify

@main.route('/usuario', methods=['POST'])
def criar_usuario():
    dados = request.get.jason() # Pega o json da requisição
    novo_usuario = Usuario(nome=dados['nome'])
    db.session.add(novo_usuario) # Prepara para salvar
    db.session.commit() # Salva no banco
    return jsonify({'mensagem' : "Usuário (a) criado (a) com sucesso!"}), 201 # Resposta do JSON

@main.route('/usuario/<int:user_id>', methods=['GET'])
def get_usuario(user_id):   
    user = Usuario.query.get(user_id)
    if user:
        return jsonify({
            "user_id": user.id,
            "nome": user.nome,
            "patrimonio": user.patrimonio,
            "limite_cartao": user.limite_cartao,
            "limite_emprestimo": user.limite_emprestimo,
        }) # salvamos em json apenas para resposta para o usuário
    
    return jsonify({"error": "Usuário (a) não encontrado (a)"}), 404
    
  

