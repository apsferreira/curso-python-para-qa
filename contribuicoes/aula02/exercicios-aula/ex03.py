print("CALCULADORA - OPERAÇÕES BÁSICAS\n\n")

operacao = input("Digite a operação desejada: + | - | * | / | // | % | ^ |: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print("*********************************************\n")
print(f"Os números foram: {num1} e {num2}\n\n")

print(f'SOMA {num1} + {num2} = {round(num1+num2, 2)}')
print(f'SUBTRAÇÃO {num1} - {num2} = {round(num1-num2, 2)}')
print(f'MULTIPLICAÇÃO {num1} * {num2} = {round(num1*num2, 2)}')
if num2 == 0:
    print(f"Não é possivel realizar: DIVISÃO, DIVISÃO INTEIRA e RESTO DA DIVISAO, pois segundo número é {num2}")
else:

    print(f'DIVISÃO {num1} / {num2} = {round(num1/num2, 2)}')
    print(f'DIVISÃO INTEIRA {num1} // {num2} = {round(num1//num2, 2)}')
    print(f'RESTO DA DIVISAO {num1} % {num2} = {round(num1%num2, 2)}')

print(f'POTENCIACÃO {num1} ^ {num2} = {round(num1**num2, 2)}')

if operacao == "+":
    print(f'SOMA {num1} + {num2} = {round(num1+num2, 2)}')
elif operacao == "-":
    print(f'SUBTRAÇÃO {num1} - {num2} = {round(num1-num2, 2)}')
elif operacao == "*":
    print(f'MULTIPLICAÇÃO {num1} * {num2} = {round(num1*num2, 2)}')
elif operacao == "^":
    print(f'POTENCIACÃO {num1} ^ {num2} = {round(num1**num2, 2)}')
if num2 == 0:
    print(f"Não é possivel realizar: DIVISÃO, DIVISÃO INTEIRA e RESTO DA DIVISAO, pois segundo número é {num2}")
else:
    if operacao == "/":
        print(f'DIVISÃO {num1} / {num2} = {round(num1/num2, 2)}')
    elif operacao == "//":
        print(f'DIVISÃO INTEIRA {num1} // {num2} = {round(num1//num2, 2)}')
    elif operacao == "%":
        print(f'RESTO DA DIVISAO {num1} % {num2} = {round(num1%num2, 2)}')