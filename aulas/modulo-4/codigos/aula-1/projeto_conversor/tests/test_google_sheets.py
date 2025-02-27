import pytest
from ..manipulacao_json.google_sheets import (
    salvar_dados
)

@pytest.fixture
def setup_sheets():
    """Criar um ambiente de testes no google sheets."""

    usuarios_teste = [
        {"id": 1, "nome": "Alice", "email": "alice@email.com"},
        {"id": 2, "nome": "Bruna", "email": "bruna@email.com"},
        {"id": 3, "nome": "Lucas", "email": "lucas@email.com"}
    ]

    salvar_dados(usuarios_teste)

    yield usuarios_teste