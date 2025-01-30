nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))


if idade >= 18:
    print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nPode ser habilitado a dirigir.')
else:
    print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nNão pode ser habilitado a dirigir.')