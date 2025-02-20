import json
import csv
import os
from ..conversores.json_para_csv import json_para_csv

def test_json_to_csv():
    dados_teste = [
        {"id": 1, "nome": "Marinelia", "email": "marinelia@email.com"}
    ]

    with open ("teste.json", "w") as json_file:
        json.dump(dados_teste, json_file)

    json_para_csv("teste.json", "teste.csv")


    with open("teste.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        linha = next(reader)
        assert linha["nome"] == "Marinelia"

    os.remove("teste.json")
    os.remove("teste.csv")