import os
import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

# Garante que a pasta logs/ existe
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

# Configuração do logging com caminho correto
log_file = os.path.join(log_dir, "api.log")
logging.basicConfig(filename=log_file, level=logging.INFO)

logging.info("Logger iniciado com sucesso!")


users = [{"id": 1, "nome": "Leonardo"}, {"id": 2, "nome": "Ytalo"}, {"id": 3, "nome": "Leticia"}]

@app.route("/", methods=["GET"])
def hello():
    logging.info("API funcionando corretamente")
    print("Hello world!!")
    return jsonify("Hello world!!"), 200

@app.route('/curso')
def nome_curso():
  print("O nome deste curso é Python para QA")
  return 'O nome deste curso é Python para QA'

@app.route('/usuarios')
def listar_users():
  logging.info("Usuários listados corretamente")
  return jsonify(users), 200

@app.route('/usuarios', methods=["POST"])
def add_user():
   new_user = request.json
   logging.info("Usuários inserido corretamente")
   users.append(new_user)
   return jsonify({"mensagem": "Usuário adicionado com sucesso"}), 201

@app.route('/usuarios/<int:user_id>', methods=["DELETE"])
def remove_user(user_id):
   global users
   logging.info(f"user_id: {user_id}")
   users = [user for user in users if user["id"] != user_id]
   return jsonify({"mensagem": "Usuário removido com sucesso"}), 201

if __name__ == "__main__":
    app.run(debug=True)