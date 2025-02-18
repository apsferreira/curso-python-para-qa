import csv 

with open("dados_usuarios.csv", mode="r") as arquivo:
    reader = csv.DictReader(arquivo)
    for linha in reader:
        print(linha)