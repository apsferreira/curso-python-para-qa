numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("Soma:", numero1 + numero2)
print("Multiplicação:", numero1 * numero2)

if numero2 != 0:
    print("Divisão:", numero1 / numero2)
else:
    print("Não foi possível realizar a divisão, o segundo número é 0.")

print("Subtração:", numero1 - numero2)