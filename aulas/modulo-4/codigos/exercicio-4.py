import json

with open("dados_usuarios.json", "r") as arquivo:
    dados = json.load(arquivo)

    for dado in dados:
        print(dado)