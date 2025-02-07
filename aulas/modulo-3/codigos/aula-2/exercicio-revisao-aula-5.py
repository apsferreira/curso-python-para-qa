import calculadora

operacao = 999

while operacao != 0:
    operacao = int(input("informe qual a operacao a ser efetuada: \n\n 1 - Soma \n 2 - Subtracao \n 3 - Multiplicaçao \n 4 - Divisão \n 0 - sair do programa \n\n:> "))
    
    resultado = None

    if operacao != 0:
        numero1 = input("informe o valor referente ao primeiro numero: ")
        numero2 = input("informe o valor referente ao segundo numero: ")

        if operacao == 1:
            resultado = calculadora.soma(int(numero1), int(numero2))
        elif operacao == 2:
            resultado = calculadora.subtracao(int(numero1), int(numero2))
        elif operacao == 3:
            resultado = calculadora.multiplicacao(int(numero1), int(numero2))
        elif operacao == 4: 
            resultado = calculadora.divisao(int(numero1), int(numero2))
        else:
            break
    else:
        break

    print(f"O Resultado da operação é: {resultado} \n\n")
    