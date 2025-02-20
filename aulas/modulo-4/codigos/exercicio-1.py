import csv 

usuarios = [
    {"id": 1, "nome": "Antonio Pedro", "email": "contato@antoniopedr.com.br"},
    {"id": 2, "nome": "Cleide Santos", "email": "cleide@teste.com.br"},
    {"id": 3, "nome": "Marcos Castro", "email": "marcos@teste.com.br"}
]

with open("dados_usuarios.csv", mode="w", newline="") as arquivo:
    
    writer = csv.DictWriter(arquivo, fieldnames=["id", "nome", "email"])
    writer.writeheader()
    writer.writerows(usuarios)
