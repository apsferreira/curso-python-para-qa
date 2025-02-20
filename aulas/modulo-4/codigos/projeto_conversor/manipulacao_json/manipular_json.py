import json

ARQUIVO_JSON = "dados.json"

def listar_usuarios(arquivo_json=ARQUIVO_JSON):
    dados = carregar_dados(arquivo_json)

    print("Lista de usuarios: \n")

    print(dados)

    for usuario in dados:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Email: {usuario['email']}")

def carregar_dados(arquivo_json=ARQUIVO_JSON):
     with open(arquivo_json, "r") as arquivo_json:
        return json.load(arquivo_json)

def adicionar_usuario(id, nome, email, arquivo_json=ARQUIVO_JSON):
    dados = carregar_dados(arquivo_json)
    novo_usuario = {"id": id, "nome": nome, "email": email}
    
    dados.append(novo_usuario)

    salvar_dados(dados)
    print("\n\nUsuario Salvo com sucesso.")

def salvar_dados(dados, arquivo_json=ARQUIVO_JSON):
    with open(ARQUIVO_JSON, "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

