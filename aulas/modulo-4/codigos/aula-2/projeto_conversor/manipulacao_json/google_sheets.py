import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

# Caminho correto para o arquivo JSON dentro do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório atual do script
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credenciais.json") 
SHEET_NAME = "Usuarios_QA"

# Configuração da API
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
client = gspread.authorize(creds)

# Acessa a planilha
spreadsheet = client.open(SHEET_NAME)
sheet = spreadsheet.sheet1

def carregar_dados_sheets():
    registros = sheet.get_all_records()
    registros_corrigidos = [
        {chave.lower(): valor for chave, valor in usuario.items()} for usuario in registros
    ]

    return registros_corrigidos

def salvar_dados_sheets(dados):
    sheet.clear()  # Apaga os dados existentes
    sheet.append_row(["ID", "Nome", "Email"])  # Reescreve o cabeçalho
    for usuario in dados:
        sheet.append_row([usuario["id"], usuario["nome"], usuario["email"]])

def adicionar_usuario_sheets(id, nome, email):
    sheet.append_row([id, nome, email])
    print(f"Usuario '{nome}' adicionado com sucesso")

def editar_usuario_sheets(id, novo_nome, novo_email):
    registros = sheet.get_all_records()

    for i, usuario in enumerate(registros, start=2):
        if usuario["ID"] == id:
            if novo_nome:
                # usuario["nome"] = novo_nome
                sheet.update_cell(i, 2, novo_nome)
            
            if novo_email:
                # usuario["email"] = novo_email
                sheet.update_cell(i, 3, novo_email)
            print(f"Usuario com ID {id} atulizado com sucesso no google sheets")
    print(f"ERRO: Usuario com ID {id} nao encontrado.")

def deletar_usuario_sheets(id):
    registros = sheet.get_all_records()

    for i, usuario in enumerate(registros, start=2):
        if usuario["ID"] == id:
            sheet.delete_rows(i)
            print(f"Usuario com o id {id}, foi removido com sucesso do google sheets.")

