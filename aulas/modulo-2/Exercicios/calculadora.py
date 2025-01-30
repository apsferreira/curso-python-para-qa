def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Erro: Divisão por zero!")
    return n1 / n2

def modulo(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Erro: Módulo por zero!")
    return n1 % n2

def divisao_inteira(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Erro: Divisão inteira por zero!")
    return n1 // n2

def calculadora_simples():

    print("Calculadora Python Simples")
    print("Operações disponíveis:")
    print("  + : Soma")
    print("  - : Subtração")
    print("  * : Multiplicação")
    print("  / : Divisão")
    print("  % : Módulo (Resto da divisão)")
    print("  //: Divisão Inteira")
    print("  sair: Para encerrar")

    while True:
        operacao = input("\nDigite a operação desejada (+, -, *, /, %, //, ou 'sair'): ").lower()

        if operacao == 'sair':
            print("Encerrando a calculadora.")
            break

        if operacao not in ['+', '-', '*', '/', '%', '//']:
            print("Operação inválida. Por favor, escolha entre +, -, *, /, %, // ou 'sair'.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = somar(num1, num2)
            elif operacao == '-':
                resultado = subtrair(num1, num2)
            elif operacao == '*':
                resultado = multiplicar(num1, num2)
            elif operacao == '/':
                resultado = dividir(num1, num2)
            elif operacao == '%':
                resultado = modulo(num1, num2)
            elif operacao == '//':
                resultado = divisao_inteira(num1, num2)

            print("Resultado:", resultado)

        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    calculadora_simples()