import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(filename="logs/api.log", level=logging.INFO)

usuarios = [{"id": 1, "nome": "Jose"}, {"id": 2, "nome": "Marlene"}, {"id": 3, "nome": "Paula"}]

@app.route("/", methods=["GET"])
def hello():
    logging.info("API funcionando corretamente")
    return jsonify("Hello World!!!"), 200

@app.route("/curso", methods=["GET"])
def curso():
    logging.info("Curso consultado")
    return jsonify({"mensagem": "Python para QAs!"}), 200

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    logging.info("Usuários Listados com sucesso")
    return jsonify(usuarios), 200

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    novo_usuario = request.json
    usuarios.append(novo_usuario)
    logging.info(f"Requisicao POST: Uusario: {novo_usuario['nome']} foi inserido")
    return jsonify({"mensagem": "Usuário adicionado com sucesso"}), 201

@app.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def remover_usuario(id_usuario):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id_usuario]
    logging.info(f"Requisicao DELETE: Usuario: {id_usuario} removido")
    return jsonify({"mensagem" : "Usuário removido com sucesso"})



if __name__ == "__main__":
    app.run(debug=True)