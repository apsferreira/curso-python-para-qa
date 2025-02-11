calcular_media = lambda nota1, nota2: (nota1 + nota2) / 2
validar_teste = lambda status: "Sucesso" if status == "Pass" else "Falha"
testes = ["Login: Pass", "Cadastro: Fail", "Pagamento: Pass"]
teste_filter = list(filter(lambda teste: "Pass" in teste, testes))

print(calcular_media(6, 8))
print(validar_teste("Fail"))
print(validar_teste("Pass"))
print(teste_filter)