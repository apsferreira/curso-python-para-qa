from fastapi import FastAPI, UploadFile, File, HTTPException

import json
import os

from manipulacao_json.manipular_json import(
    listar_usuarios
)

from conversores.json_para_xml import json_para_xml
from conversores.json_para_csv import json_para_csv
from conversores.xml_para_json import xml_para_json
from conversores.csv_para_json import csv_para_json

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def live():
    return {"mensagem": "Funcinando"}

@app.post("/convert")
async def converter_arquivo(file: UploadFile = File(...), formato_saida: str = "csv"):
    extensao_suportada = {"json", "csv", "xml"}

    nome_arquivo = file.filename
    extensao_entrada = nome_arquivo.split(".")[-1].lower()

    if extensao_entrada not in extensao_suportada or formato_saida not in extensao_suportada:
        raise HTTPException(status_code=400, detail="Formato do arquivo invalido")

    caminho_de_entrada = os.path.join(UPLOAD_DIR, nome_arquivo)
    with open(caminho_de_entrada, "w") as novo_arquivo:
        novo_arquivo.write(file.file.read())

    nome_convertido = f"{nome_arquivo.split(".")[0]}_convertido.{formato_saida}"
    caminho_saida = os.path.join(UPLOAD_DIR, nome_convertido)

    if extensao_entrada == "json" and formato_saida == "csv":
        json_para_csv(caminho_de_entrada, caminho_saida)
    elif extensao_entrada == "json" and formato_saida == "xml":
        json_para_xml(caminho_de_entrada, caminho_saida)
    elif extensao_entrada == "csv" and formato_saida == "json":
        csv_para_json(caminho_de_entrada, caminho_saida)
    elif extensao_entrada == "xml" and formato_saida == "json":
        xml_para_json(caminho_de_entrada, caminho_saida)
    else:
        raise HTTPException(status_code=400, detail="conversao nao suportada")

    return {"mensagem": "conversao concluida", "arquivo_saida": caminho_saida}


