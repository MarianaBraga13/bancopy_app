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

# @app.route('/usuario/<user_id>', methods=['GET'])
# def get_usuario(user_id):
#     user = Usuario.query.get(user_id)
#     if user:
#         return jsonify({
#             "user_id": user.id,
#             "nome": user.nome,
#             "patrimonio": user.patrimonio,
#             "limite_cartao": user.limite_cartao,
#             "limite_emprestimo": user.limite_emprestimo,
#         })
#     return jsonify({"error": "Usuário não encontrado"}), 404

# @app.route('/usuario/<user_id>/depositar', methods=['POST'])
# def depositar(user_id):
#     valor = request.json.get('valor')
#     user = Usuario.query.get(user_id)
#     if user and valor and valor > 0:
#         user.patrimonio += valor
#         transacao = Transacao(usuario_id=user.id, tipo='depósito', valor=valor)
#         db.session.add(transacao)
#         db.session.commit()
#         return jsonify({"message": f"Depósito de R${valor} realizado."})
#     return jsonify({"error": "Erro no depósito."}), 400

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)



