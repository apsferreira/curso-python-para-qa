import requests

BASE_URL = "http://127.0.0.1:5000/"

def test_curso():
    resposta = requests.get(f"{BASE_URL}/curso")
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == "Python para QAs!"

def test_listar_usuarios():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)

def test_adicionar_usuario():
    novo_usuario = {"id": 99, "nome": "David"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=novo_usuario)
    assert resposta.status_code == 201
    assert resposta.json()["mensagem"] == "Usuário adicionado com sucesso"

def test_remover_usuario():
    resposta = requests.delete(f"{BASE_URL}/usuarios/99")
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == "Usuário removido com sucesso"