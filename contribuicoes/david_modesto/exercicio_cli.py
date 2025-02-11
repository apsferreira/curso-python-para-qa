import calculadora

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))

soma = calculadora.somar(a,b)
subtracao = calculadora.diminuir(a,b)
multiplicacao = calculadora.multiplicar(a,b)
divisao = calculadora.dividir(a,b)
print(f"A soma é: {soma}")
print(f"A subtração é: {subtracao}")
print(f"A multiplicação é: {multiplicacao}")
print(f"A divisão é: {divisao}")