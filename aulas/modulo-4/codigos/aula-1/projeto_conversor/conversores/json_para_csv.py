import json
import csv


def json_para_csv(json_arquivo, csv_arquivo):
    with open(json_arquivo, "r") as arquivo:
        dados = json.load(arquivo)

    with open(csv_arquivo, "w", newline="") as arquivo_csv:
        fieldnames=["id", "nome", "email"]
        writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(dados)

    print("Dados convertidos de json para csv com sucesso")