#12.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#13.o produto do dobro do primeiro com metade do segundo .
#14.a soma do triplo do primeiro com o terceiro.
#15.o terceiro elevado ao cubo.

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))


resultado1 = (int1 * 2) * (int2 / 2)
print("Resultado 1:", resultado1)

resultado2 = (int1 * 3) + real
print("Resultado 2:", resultado2)

resultado3 = real ** 3
print("Resultado 3:", resultado3)

