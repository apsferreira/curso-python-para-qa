soma = 0
for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota
media = soma / 4
print(f"A média é {media}")