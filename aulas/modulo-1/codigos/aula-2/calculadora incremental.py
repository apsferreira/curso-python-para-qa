from math import floor

def calculadora_sequencial():
    resultado_atual = 0.0 
    primeira_vez = True

    print("Operações disponíveis: +, -, *, /, %, //, = (definir), sair")
    print("Digite 'sair' como operação para encerrar.")

    while True:
        print("\nResultado Atual:", resultado_atual)

        try:
            if primeira_vez:
                num1 = float(input("Digite o primeiro número: "))
                resultado_atual = num1
                primeira_vez = False
            else:
                num1 = resultado_atual


            operacao = input("Digite a operação (+, -, *, /, %, //, =, ou 'sair'): ").lower()

            if operacao == 'sair':
                print("Encerrando a calculadora sequencial.")
                break
            elif operacao == '=':
                novo_valor = float(input("Digite o novo valor para substituir o resultado atual: "))
                resultado_atual = novo_valor
                continue

            if operacao not in ['+', '-', '*', '/', '%', '//']:
                print("Operação inválida. Por favor, escolha entre +, -, *, /, %, //, =, ou 'sair'.")
                continue

            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado_atual = num1 + num2
            elif operacao == '-':
                resultado_atual = num1 - num2
            elif operacao == '*':
                resultado_atual = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero!")
                resultado_atual = num1 / num2
            elif operacao == '%':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Módulo por zero!")
                resultado_atual = num1 % num2
            elif operacao == '//':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão inteira por zero!")
                resultado_atual = floor(num1 / num2)

        except ValueError:
            print("Entrada inválida. Por favor, digite números e operações válidas.")
            primeira_vez = False
        except ZeroDivisionError as e:
            print(e)
            primeira_vez = False
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            primeira_vez = False

if __name__ == "__main__":
    calculadora_sequencial()