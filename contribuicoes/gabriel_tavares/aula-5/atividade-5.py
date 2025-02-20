import re

def validar_cpf(cpf):
    if len(cpf) != 14:
        print("cpf não tem 11 digitos")
        return False

    if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return True
    else:
        return False

cpf = input("Digite o CPF: ")

if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")