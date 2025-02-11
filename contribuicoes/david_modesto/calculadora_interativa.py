while True:
    num1 = input("Digite o primeiro número (ou 'sair' para sair): ")
    if num1.lower() == "sair":
        break
    try:
        num1 = int(num1)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")
        continue

    num2 = input("Digite o segundo número (ou 'sair' para sair): ")
    if num2.lower() == "sair":
        break
    try:
        num2 = int(num2)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")
        continue

    print("Soma:", num1 + num2)
    print("Multiplicação:", num1 * num2)
    if num2 != 0:
        print("Divisão:", num1 / num2)
    else:
        print("Divisão: Não é possível dividir por zero.")
    print("Subtração:", num1 - num2)