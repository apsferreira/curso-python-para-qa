import random

casos_teste = ["Login", "Cadastro", "Checkout", "Busca", "Pagamento"]
resultados = {}


for idx, caso in enumerate(casos_teste, 1):
    print(f"{idx}. Caso de teste: {caso}")
    
while True:
    teclado = input("Digite o numero do teste para rodar ou 'sair' para encerrar: ")

    if teclado == "sair":
        break

    if teclado.isdigit() and 1 <= int(teclado) <= len(casos_teste):
        caso_selecionado = casos_teste[int(teclado) - 1]
        resultado = random.choice(["Pass", "Fail"])
        resultados[caso_selecionado] = resultado
        print(f"O caso '{caso_selecionado}' executado - Resultado: '{resultado}'")
    else:
        print("escollha invalida")

print("Resultado final: ")

for caso,resultado in resultados.items():
    print(f"{caso}: {resultado}")