nome = input("Qual é seu nome? ")
idade = int(input("Digite sua idade (exemplo: 7): "))
altura = float(input("Digite sua altura (exemplo: 1.70): "))

if idade >= 18:
    maior_idade = True
else:
    maior_idade = False


print("\n*** INFORMAÇÕES DO USUARIO ***\n")

print(f'Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nÉ maior de idade? {maior_idade} ')
