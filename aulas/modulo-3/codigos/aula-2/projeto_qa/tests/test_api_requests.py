import requests

BASE_URL = "http://127.0.0.1:5000/"

def curso():
    resposta = requests.get(f"{BASE_URL}/curso")
    print(resposta.json())

def listar_usuarios():
    resposta = requests.get(f"{BASE_URL}/usuarios")
    print(resposta.json())


curso()
listar_usuarios()