nome = input("Qual é seu nome? ")
idade = int(input("Digite sua idade (exemplo: 7): "))
altura = float(input("Digite sua altura (exemplo: 1.70): "))

print("\n*** INFORMAÇÕES DO USUARIO ***\n")

if idade >= 18:
    print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nPode ser habilitado a dirigir.')
else:
    print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nNão pode ser habilitado a dirigir.')
