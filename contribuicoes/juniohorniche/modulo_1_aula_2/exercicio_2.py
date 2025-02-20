# escreva um programa que a entrada será a idade do usuario e o retorno do programa será uma mensagem informando se o
# usuario pode possuir uma permissao para dirigir ou nao

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print('Você possui idade suficiente para dirigir')
else:
    print('Você ainda não possui idade suficiente para dirigir')
