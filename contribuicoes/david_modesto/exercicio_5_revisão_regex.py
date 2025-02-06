import re

def validar_cpf(cpf):
    """
    Função para validar o formato de um CPF utilizando regex.

    Args:
        cpf: O CPF a ser validado.

    Returns:
        True se o CPF tiver um formato válido, False caso contrário.
    """

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 14:
        print("cpf não tem 11 digitos")
        return False

    if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return True
    else:
        return False

cpf_input = input("Digite o CPF (com ou sem formatação): ")

if validar_cpf(cpf_input):
    print("CPF válido")
else:
    print("CPF inválido")