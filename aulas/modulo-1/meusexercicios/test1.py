print("Hello World!")

# nome = input("Seu nome: ")
# idade = input("Sua idade: ")
# print(f"Olá {nome} bem vindo, feliz {idade} anos!")

# Tipo de dados
# int = inteiro
# ano_nascimento = int(input("Informe o ano de nascimento: "))
# idade = 2024 - ano_nascimento
# print(f"Você tem {idade} anos")

# float = ponto flutuante
# str = string
# bool = booleano

# Operadores aritméticos
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
# + = adição
print(f"A soma de {n1} + {n2} é {n1 + n2}")
print(f"A soma de {n1} + {n2} é {n1 + n2}")
# - = subtração
print(f"A subtração de {n1} - {n2} é {n1 - n2}")
# * = multiplicação
print(f"A multiplicação de {n1} * {n2} é {n1 * n2}")
# / = divisão
print(f"A divisão de {n1} / {n2} é {n1 / n2}")
# // = divisão inteira
print(f"A divisão inteira de {n1} // {n2} é {n1 // n2}")
# % = módulo
# ** = exponenciação

# Desafio: criar um programa que calcule o IMC de uma pessoal, com uma mensagem formatada de saída
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso / ((altura/100) ** 2)
print(f"O seu IMC é {imc:.2f}")
