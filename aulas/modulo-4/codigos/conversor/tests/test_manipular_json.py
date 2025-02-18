import json
import os
from manipulacao_json import listar_usuarios

TEST_FILE = "dados_teste.json"

def setup_json():
    dados_teste = [
        {"id": 1, "nome": "Alice", "email": "alice@email.com"},
        {"id": 2, "nome": "Bruna", "email": "bruna@email.com"},
        {"id": 3, "nome": "Lucas", "email": "lucas@email.com"}
    ]

    with open(TEST_FILE, "w") as arquivo_json:
        json.dump(dados_teste, arquivo_json, indent=4)

    yield TEST_FILE

    os.remove(TEST_FILE)

    
def test_listar_usuarios(setup_json, capsys):
    listar_usuarios()

    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "Bruna" in captured.out
    assert "Lucas" in captured.out