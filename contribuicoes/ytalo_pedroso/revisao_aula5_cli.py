import calculadora

teclado = input("""
                Informe qual a operaçao a ser realizada:\n
                 - 1 - Adição
                 - 2 - Subtração
                 - 3 - Multiplicação
                 - 4 - Divisão\n""")

num1 = int(input("Informe o valor do primeiro número da operação: "))
num2 = int(input("Informe o valor do segundo número da operação: "))

resultado = None
if teclado == '1': resultado = calculadora.soma(num1, num2)
elif teclado == '2': resultado = calculadora.subtracao(num1, num2)
elif teclado == '3': resultado = calculadora.multiplicacao(num1, num2)
elif teclado == '4': resultado = calculadora.divisao(num1, num2)

print(f"O resultado é {resultado}")