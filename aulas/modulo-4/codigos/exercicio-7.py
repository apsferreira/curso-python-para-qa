import json
import csv

with open("dados_usuarios.csv", "r", newline="") as arquivo_csv:
    reader = csv.DictReader(arquivo_csv)

    dados = [linha for linha in reader]

with open("usuarios.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)

print("Dados convertidos com sucesso")