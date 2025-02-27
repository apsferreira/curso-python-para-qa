import pytest
from ..manipulacao_json.google_sheets import (
    carregar_dados_sheets,
    salvar_dados_sheets,
    adicionar_usuario_sheets, 
    editar_usuario_sheets,
    deletar_usuario_sheets
)

@pytest.fixture
def setup_sheets():
    # Dados de teste
    usuarios_teste = [
        {"id": 1, "nome": "Alice", "email": "alice@email.com"},
        {"id": 2, "nome": "Bob", "email": "bob@email.com"},
    ]
    
    # Enviando dados de teste para o Google Sheets
    salvar_dados_sheets(usuarios_teste)
    
    yield usuarios_teste  # Permite que os testes usem esses dados

def test_conexao_google_sheets():
    try:
        dados = carregar_dados_sheets()
        assert isinstance(dados, list)  # Deve retornar uma lista
    except Exception as e:
        pytest.fail(f"Erro ao conectar com Google Sheets: {e}")

def test_carregar_dados_sheets(setup_sheets):
    dados = carregar_dados_sheets()
    assert len(dados) == 2  # Devemos ter 2 usuários
    assert dados[0]["nome"] == "Alice"

def test_adicionar_dados_sheet(setup_sheets):
    adicionar_usuario_sheets(3, "Carlos", "carlos@email.com")

    dados = carregar_dados_sheets()
    ids = [usuario["id"] for usuario in dados]
    assert 3 in ids

def test_editar_dados_sheet(setup_sheets):
    editar_usuario_sheets(2, novo_nome="Roberto", novo_email="roberto@email.com")

    dados = carregar_dados_sheets()

    for usuario in dados:
        if usuario["id"] == 2:
            assert usuario["nome"] == "Roberto"
            assert usuario["email"] == "roberto@email.com"

def test_deletar_dados_sheet(setup_sheets):
    deletar_usuario_sheets(1)

    dados = carregar_dados_sheets()
    ids = [usuario["id"] for usuario in dados]
    assert 1 not in ids
