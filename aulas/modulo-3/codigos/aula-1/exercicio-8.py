status_teste = "Em execução"

def exibir_mensagem():
    mensagem = "Este é um escopo local"
    print(mensagem)

def verificar_status():
    status_teste = "Fail"
    print(f"O status do teste é: {status_teste}")

# exibir_mensagem()
# print(mensagem)
verificar_status()
print(status_teste)