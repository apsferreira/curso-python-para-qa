nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

if idade >= 18:
    maior_idade = True
else:
    maior_idade = False



print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nÉ maior de idade? {maior_idade} ')