================== 🏦 BANCO PY =================
Bem vindo (a) ao Banco PY versão Web Interface!

Instruções:
1. Clone o repositório na sua máquina
2. instale o requirements.txt no terminal como:
pip install -r requirements.txt

Então, é só rodar no app.py.

Importante:
Esta versão é uma release do projeto de transacoes em CLI (Comand Line Interface).

Resumo:
Ideia geral:

 Esta release busca aproveitar o código do projeto de CLI para desenvolver uma interface gráfica utilizando Bootstrap, e o framework Flask (jinja), utilizando rotas com Blueprints, arquitetura estilo API REST (métodos GET, POST, DELETE), migrando os dados de JSON para o banco de dados SQLite (SQLALchemy), análise de dados e treinamento de modelos de Rregressão Linear como o scikit-learn (o treinamento será feito com ajustes visando a maior eficiência do modelo de ML)

## Histórico de versões

- ✅ **v1.0**: Criação da estrutura: 1. banco de dados (SQLite), 2. conexão do banco de dados com app.py, 3. inicialização e configuração do app com __init__.py. 4. Criação de rotas para usuário. 5. CRUD com arquitetura RESTFul, 6. utilização de blueprints para registro das rotas, 7. testes das rotas com sistemas Insomnia e Postman.

- 👉 Próxima versão: login com JWT, hash e segurança.

RESUMO DOS PRÓXIMOS PASSOS:
*Reaproveitamento do back-end de um projeto próprio em CLI (você poderá encontrá-lo no repositório: transacoes v6.0)
*Conectar ao Banco de Dados com SQLALchemy (SQLite)
*Segurança da Informação e boas práticas usando JWT / hash.
*Inserir uma interface Web, Blueprint em rotas, métodos GET, POST, DELETE (Padrão API REST)
*Popular o Banco de Dados usando seed.py
*Segurança da Informação dos dados do cliente com @login_admin
*Análise de dados usando Estatística Aplicada a Ciência de Dados (pandas)
*Análise de crédito em IA (Regressão Linear | Naive Bayes)
*Representação com dashboards usando matplotlib

Este sistema é a Versão 1.0.
