dados = {"nome": "Carlos", "idade": 20, "cidade": "Salvador"}

dados["idade"] = 40
dados["estado"] = "Bahia"

for chave, valor in dados.items():
    print(f"A chave do meu dicionario é: {chave} e o valor associado a ela é: {valor}")