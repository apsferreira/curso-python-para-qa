import re

cpf = input("Digite o numero do seu CPF: ")

cpf_valido = re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)

if cpf_valido:
    print("CPF Valido")
else:
    print("CPF Invalido")