# Calculadora básica
print("Calculadora")

novo_calculo = True

while novo_calculo:
    print("")

    n1 = float(input("N1: "))
    operator = input("Operador (+, -, *, /): ")
    n2 = float(input("N2: "))

    if operator == "+":
        print(f"Result: {n1 + n2}\n")
    elif operator == "-":
        print(f"Result: {n1 - n2}\n")
    elif operator == "*":
        print(f"Result: {n1 * n2}\n")
    elif operator == "/":
        print(f"Result: {n1 / n2}\n")

    if input("Novo calculo? s/n: ") == "s":
         novo_calculo = True
    else:
         novo_calculo = False