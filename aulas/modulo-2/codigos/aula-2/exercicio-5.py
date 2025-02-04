import csv

# matriz = [[1,2,3],[4,5,6],[7,8,9]]

# for i in matriz:
#     for j in i:
#         print(j, end=" ")
#     print()

with open("casos_teste.csv") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    
    for linha in leitor:
        print(f"Executando Teste: {linha[0]} - Esperado: {linha[1]} - Obtido: {linha[2]}")
