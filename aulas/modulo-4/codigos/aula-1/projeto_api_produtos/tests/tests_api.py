import requests

BASE_URL = "http://127.0.0.1:5000"

def test_adicionar_produto():
    novo_produto = {"id": 99, "nome": "Mouse", "preco": 250.00}
    resposta = requests.post(f"{BASE_URL}/produtos", json=novo_produto)
    assert resposta.status_code == 201
    assert resposta.json()["mensagem"] == "Produto cadastrado"

def test_listar_produtos():
    resposta = requests.get(f"{BASE_URL}/produtos")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)

def test_buscar_produto():
    resposta = requests.get(f"{BASE_URL}/produtos/99")
    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Mouse"

def test_aualizar_preco():
    novo_preco = {"preco": 200}
    resposta = requests.put(f"{BASE_URL}/produtos/99", json=novo_preco)
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == "Preço Atualizado"

def test_deletar_produto():
    resposta = requests.delete(f"{BASE_URL}/produtos/99")
    assert resposta.status_code == 200
    assert resposta.json()["mensagem"] == "Produto deletado"

def test_buscar_produto_inexistente():
    resposta = requests.get(f"{BASE_URL}/produtos/75")
    assert resposta.status_code == 404
    assert resposta.json()["erro"] == "produto nao encontrado"
