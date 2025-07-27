from flask import Blueprint, request, jsonify
from .models import Usuario, Transacao
from . import db
from datetime import datetime, timezone

main = Blueprint('main', __name__)

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
    
    

