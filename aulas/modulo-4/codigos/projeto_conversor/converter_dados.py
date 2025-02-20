import sys
import os

from conversores.json_para_xml import json_para_xml
from conversores.json_para_csv import json_para_csv
from conversores.xml_para_json import xml_para_json
from conversores.csv_para_json import csv_para_json

def detectar_formato(arquivo):
    if arquivo.endswith(".json"):
        return "json"
    elif arquivo.endswith(".csv"):
        return "csv"
    elif arquivo.endswith(".xml"):
        return "xml"
    else:
        return None
    
def gerar_nome_arquivo_saida(arquivo_entrada, formato_saida):
    nome_base = os.path.splitext(arquivo_entrada)[0]
    return f"{nome_base}_convertido.{formato_saida}"

if len(sys.argv) != 3:
    print("uso incorreto, exemplo correto: python converter_dados.py arquivo.json csv")
    sys.exit(1)

arquivo_entrada = sys.argv[1]
formato_saida = sys.argv[2].lower()

if not os.path.exists(arquivo_entrada):
    print(f"Erro: O arquivo {arquivo_entrada} nao existe")
    sys.exit(1)

formato_entrada = detectar_formato(arquivo_entrada)

if formato_entrada is None:
    print(f"formato do arquivo '{arquivo_entrada}' não suportado")
    sys.exit(1)

arquivo_saida = gerar_nome_arquivo_saida(arquivo_entrada, formato_saida)

if formato_entrada == "json" and formato_saida == "csv":
    json_para_csv(arquivo_entrada, arquivo_saida)
elif formato_entrada == "json" and formato_saida == "xml":
    json_para_xml(arquivo_entrada, arquivo_saida)
elif formato_entrada == "csv" and formato_saida == "json":
    csv_para_json(arquivo_entrada, arquivo_saida)
elif formato_entrada == "xml" and formato_saida == "json":
    xml_para_json(arquivo_entrada, arquivo_saida)
else:
    print(f"Erro de conversao de {formato_entrada} para {formato_saida} nao suportado")


print(f"Conversao finalizada com sucesso: Arquivo salvo como {arquivo_saida}")