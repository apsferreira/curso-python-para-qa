
# Iterando sobre uma lista
nomes = ["Antonio", "Joao", "Maria", "Jose", "Rafael"]

for nome in nomes:
    print(f"Usuario: {nome}")

# Iterando sobre um dicionario
dados = {"nome": "Carlos", "idade": 20, "cidade": "Salvador"}

for chave, valor in dados.items():
    print(f"A chave do meu dicionario é: {chave} e o valor associado a ela é: {valor}")


# Iterando sobre uma string
palavra = "Python"

for letra in palavra:
    print(letra)
