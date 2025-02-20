import re

def valida_cpf(cpf):
    return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf))

print(valida_cpf("111.222.333-55"))