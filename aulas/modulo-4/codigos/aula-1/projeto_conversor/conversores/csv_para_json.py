import json
import csv

def csv_para_json(csv_file, json_file):
    with open(csv_file, "r", newline="") as arquivo_csv:
        reader = csv.DictReader(arquivo_csv)

        dados = [linha for linha in reader]

    with open(json_file, "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

    print("Dados convertidos com sucesso")