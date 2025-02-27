from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = []

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    novo_produto = request.json
    produtos.append(novo_produto)
    return jsonify({"mensagem": "Produto cadastrado"}), 201

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos), 200

@app.route("/produtos/<int:id_produto>", methods=["GET"])
def buscar_produto(id_produto):
    
    for produto in produtos:
        if produto["id"] == id_produto:
            return jsonify(produto), 200
    
    return jsonify({"erro": "produto nao encontrado"}), 404

@app.route("/produtos/<int:id_produto>", methods=["PUT"])
def atualizar_preco(id_produto):
    novo_preco = request.json["preco"]

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["preco"] = novo_preco
            return jsonify({"mensagem": "Preço Atualizado"}), 200
        
    return jsonify({"erro": "Produto nao encontrado"}), 404

@app.route("/produtos/<int:id_produto>", methods=["DELETE"])
def deletar_produto(id_produto):
    global produtos
    produtos = [produto for produto in produtos if produto["id"] != id_produto]
    return jsonify({"mensagem": "Produto deletado"}), 200

if __name__ == "__main__":
    app.run(debug=True)