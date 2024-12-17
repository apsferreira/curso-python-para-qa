nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em m: "))

maioridade = False
if(idade > 18):
    maioridade = True
if maioridade:
    print(f'{nome}, voce tem {idade} e é maior de idade. Sua altura é {altura}m')
else:
    print(f'{nome}, voce tem {idade} e é  menor de idade. Sua altura é {altura}m')