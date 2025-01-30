# Peça nome, idade e altura para o usuário, informe na saída e adicione se ele é maior de idade ou não.
print("Por favor, informe:")
nome = input(f"Nome: ")
idade = int(input(f"Idade: "))
altura = float(input(f"Altura (em cm): "))
ehMaiorDeIdade = "maior de idade" if idade >= 18 else "menor de idade"
print(f"\n{nome}, você tem {idade} anos, {altura/100}m de altura e é {ehMaiorDeIdade}.")
