# Escreva um programa que a entrada será a idade do usuário e o retorno do programa será uma mensagem, informando
# se o usuário pode possuir uma permissão para dirigir ou não.
print("Por favor, informe: ")
nome = input("Nome: ")
idade = int(input("Idade: "))
ehPermitidoDirigir = "você tem permissão para dirigir" if idade >= 18 else "você não tem permissão para dirigir."
print(f"{nome}, {ehPermitidoDirigir}. ")