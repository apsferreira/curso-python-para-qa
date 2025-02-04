import random

tests_cases = ["Login", "Cadasto", "Checkout", "Busca", "Pagamento"]
results = {}

for i, case in enumerate(tests_cases, 1):
    print(f'{i}. Caso de teste: {case}')

while True:
    keyinput = input('Digite o numero do teste a ser executado ou <sair> para encerrar execucao e mostrar os resultados: ')

    if keyinput == 'sair':
        break

    if keyinput.isdigit() and 1 <= int(keyinput) <= len(tests_cases):
        selected_case = tests_cases[int(keyinput) - 1]
        result = random.choice(["Pass", "Fail"])
        results[selected_case] = result
        
    else:
        print('Opcao invalida')

print("\nRelatorio: ")
for test_case, result in results.items():
    print(f'{test_case}: {result}')
