import json

ARQUIVO_JSON = "dados.json"

def listar_usuarios():
    dados = carregar_dados()

    print("Lista de usuarios: \n")

    print(dados)

    for usuario in dados:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Email: {usuario['email']}")

def adicionar_usuario(id, nome, email):
    dados = carregar_dados()
    novo_usuario = {"id": id, "nome": nome, "email": email}
    
    dados.append(novo_usuario)

    salvar_dados(dados)
    print("\n\nUsuario Salvo com sucesso.")

def salvar_dados(dados):
    with open(ARQUIVO_JSON, "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

def carregar_dados():
     with open(ARQUIVO_JSON, "r") as arquivo_json:
        return json.load(arquivo_json)