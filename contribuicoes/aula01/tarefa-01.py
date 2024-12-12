print("\n*** CALCULADORA DE IMC ***\n")

peso = float(input("Digite seu peso (exemplo: 70.2): \n"))
altura = float(input("Digite sua altura (exemplo: 1.70): \n"))

imc = peso / altura ** 2

print(f'\nSeu IMC:', end=" ")
if imc < 18.5:
    print(f'\033[1m{round(imc, 2)}\033[0m - CLASSIFICAÇÃO: \033[1mMAGREZA\033[0m - OBESIDADE (GRAU): \033[1m0\033[0m')
elif 18.5 <= imc <= 24.9:
    print(
        f'\033[1m{round(imc, 2)}\033[0m - CLASSIFICAÇÃO: \033[1mNORMAL\033[0m - OBESIDADE (GRAU): \033[1m0\033[0m')
elif 24.9 < imc <= 29.0:
    print(
        f'\033[1m{round(imc, 2)}\033[0m - CLASSIFICAÇÃO: \033[1mSOBREPESO\033[0m - OBESIDADE (GRAU): \033[1mI\033[0m')
elif 29 < imc <= 39.9:
    print(
        f'\033[1m{round(imc, 2)}\033[0m - CLASSIFICAÇÃO: \033[1mOBESIDADE\033[0m - OBESIDADE (GRAU): \033[1mII\033[0m')
else:
    print(
        f'\033[1m{round(imc, 2)}\033[0m - CLASSIFICAÇÃO: \033[1mOBESIDADE GRAVE\033[0m - OBESIDADE (GRAU): \033[1mIII\033[0m')

# Site utilizado para pegar os limites de classificação de cada grupo:
# https://www.programasaudefacil.com.br/calculadora-de-imc
