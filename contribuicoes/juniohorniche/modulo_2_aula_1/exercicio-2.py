while(True):
    primeiro_numero = int(input("Digite o primeiro numero: "))
    operador = input("Digite a operação: ")
    segundo_numero = int(input("Digite o segundo numero: "))

    if operador == "+":
        print(f"Resultado: {primeiro_numero + segundo_numero}")
    elif operador == "-":
        print(f"Resultado: {primeiro_numero - segundo_numero}")
    elif operador == "/":
        print(f"Resultado: {primeiro_numero / segundo_numero}")
    elif operador == "*":
        print(f"Resultado: {primeiro_numero * segundo_numero}")

    print("================== <CTR + C> para sair ==========================")
