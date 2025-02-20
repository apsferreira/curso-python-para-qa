import json

usuarios = [
    {"id": 1, "nome": "Antonio Pedro", "email": "contato@antoniopedr.com.br"},
    {"id": 2, "nome": "Cleide Santos", "email": "cleide@teste.com.br"},
    {"id": 3, "nome": "Marcos Castro", "email": "marcos@teste.com.br"}
]

with open("dados_usuarios.json", "w") as arquivo:
    json.dump(usuarios, arquivo, indent=4)