def titulo_calculadora():
    print("CALCULADORA - OPERAÇÕES BÁSICAS\n")
    print("OPERAÇÕES: \n")
    print("SOMA -> +")
    print("SUBTRAÇÃO -> -")
    print("MULTIPLICAÇÃO -> *")
    print("DIVISÃO -> /")
    print("DIVISÃO INTEIRA -> //")
    print("RESTO DA DIVISAO -> %")
    print("POTENCIACÃO -> **\n")


def entrada_do_usuario():
    global operacao, num1, num2
    operacao = input("Digite a operação desejada: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))


def calculo_e_resultado_da_operacao():
    print("*********************************************\n")
    print(f"Os números foram: {num1} e {num2}\n\n")
    if operacao == "+":
        print(f'SOMA {num1} + {num2} = {round(num1 + num2, 2)}')
    elif operacao == "-":
        print(f'SUBTRAÇÃO {num1} - {num2} = {round(num1 - num2, 2)}')
    elif operacao == "*":
        print(f'MULTIPLICAÇÃO {num1} * {num2} = {round(num1 * num2, 2)}')
    elif operacao == "^":
        print(f'POTENCIACÃO {num1} ^ {num2} = {round(num1 ** num2, 2)}')

    elif operacao == "/" or operacao == "//" or operacao == "%":
        if num2 == 0:
            print(f"Não é possivel realizar: DIVISÃO, DIVISÃO INTEIRA e RESTO DA DIVISAO, pois segundo número é {num2}")
        else:
            if operacao == "/":
                print(f'DIVISÃO {num1} / {num2} = {round(num1 / num2, 2)}')
            elif operacao == "//":
                print(f'DIVISÃO INTEIRA {num1} // {num2} = {round(num1 // num2, 2)}')
            elif operacao == "%":
                print(f'RESTO DA DIVISAO {num1} % {num2} = {round(num1 % num2, 2)}')
    else:
        print("OPERAÇÃO INVALIDA")


titulo_calculadora()
entrada_do_usuario()
calculo_e_resultado_da_operacao()
