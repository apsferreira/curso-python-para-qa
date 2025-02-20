import requests

BASE_URL = "http://127.0.0.1:5000"

def test_curso():
    resposta = requests.get(f"{BASE_URL}/curso")
    assert resposta.status_code == 200
    # assert resposta.json()["mensagem"] == "O nome deste curso é Python para QA"

def test_listar_users():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)

def test_adicionar_usuario():
    new_user = {"id": 99, "nome":"Gabriel"}
    resposta = requests.post(f"{BASE_URL}/usuarios", json=new_user)
    assert resposta.status_code == 201
    assert resposta.json()["mensagem"] == "Usuário adicionado com sucesso"

def test_remove_user():
    resposta = requests.delete(f"{BASE_URL}/usuarios/99")
    assert resposta.status_code == 201
    assert resposta.json()["mensagem"]=="Usuário removido com sucesso"
