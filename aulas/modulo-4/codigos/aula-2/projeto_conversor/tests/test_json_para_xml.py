import json
import xml.etree.ElementTree as ET
import os

from ..conversores.json_para_xml import json_para_xml

def test_json_para_xml():
    dados_teste = [
        {"id": 1, "nome": "Mauricio", "email":"mauricio@email.com"}
    ]

    with open("testes.json", "w") as json_file:
        json.dump(dados_teste, json_file)

    json_para_xml("testes.json", "testes.xml")

    tree = ET.parse("testes.xml")
    root = tree.getroot()

    assert root.tag == "usuarios"
    assert root[0].find("nome").text == "Mauricio"

    os.remove("testes.json")
    os.remove("testes.xml") 