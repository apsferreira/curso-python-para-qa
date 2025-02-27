import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIAL_FILE = os.path.join(BASE_DIR, "credenciais-v2.json")
SHEET_NAME = "Usuarios_QA"

SCOPE = ["https://spreadsheets.google.com/feeds", "https://wwww.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIAL_FILE, SCOPE)
client = gspread.authorize(creds)

# Acessar a planilha
spreadsheet = client.open(SHEET_NAME)
sheet = spreadsheet.sheet1

def salvar_dados(dados):
    sheet.append_row(["ID", "Nome", "Email"])

    for dado in dados:
        sheet.append_row(dado["id"], dado["nome"], dado["email"])

    print("Dados Sincronizados com sucesso")