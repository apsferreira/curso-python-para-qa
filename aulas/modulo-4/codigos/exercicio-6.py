import json
import csv

with open("dados_usuarios.json", "r") as arquivo:
    dados = json.load(arquivo)

with open("usuarios.csv", "w", newline="") as arquivo_csv:
    fieldnames=["id", "nome", "email"]
    writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dados)

print("Dados convertidos com sucesso")