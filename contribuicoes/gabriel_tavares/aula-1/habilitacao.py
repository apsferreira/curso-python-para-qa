# Escreva um programa que a entrada será a idade do usuario e o retorno do
# programa será uma mensagem informando se o usuario pode possuir uma permissao para dirigir ou nao

idade = int(input("Informe sua idade: "))

eh_maior_de_idade = idade >= 18

print("\n*** Detalhes da Pessoa ***")
print(f"Idade: {idade} anos")

if eh_maior_de_idade:
    print("A pessoa tem permissão para dirigir.")
else:
    print("A pessoa não tem permissão para dirigir.")
