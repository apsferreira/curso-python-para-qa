casos_teste = {
    "Login": "Passou",
    "Cadastro": "Falhou",
    "Busca": "Falhou",
    "Pagamento": "Passou"
}

for caso, status in casos_teste.items():
    if status == "Falhou":
        print(f"O caso de teste {caso} falhou")